import gi
import json
import inspect
import traceback
from loguru import logger
from typing import Literal, Callable
from fabric.service import *
from fabric.widgets.widget import Widget
from fabric.utils import get_relative_path

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")
from gi.repository import Gtk, GLib, WebKit2


def get_javascript_bridge_code() -> str:
    with open(get_relative_path("./javascript_bridge.js"), "r") as f:
        return f.read()


JAVSCRIPT_BRIDGE_CODE = get_javascript_bridge_code()


class JavaScriptBridge(Service):
    def __init__(
        self,
        webview: "WebView",
        content_manager: WebKit2.UserContentManager,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._registered_functions = {}
        self._bridge_initialized = False
        self.webview = webview
        self.content_manager = content_manager
        self.content_manager.register_script_message_handler("fabricJsBridge")
        self.webview.connect("load_changed", self.on_load_finish)  # odd signal name
        self.content_manager.connect("script-message-received", self.on_javascript_call)

    def on_load_finish(self, webview: WebKit2.WebView, status: WebKit2.LoadEvent):
        # inject javascript bridge as soon as the page is loaded
        if status == WebKit2.LoadEvent.FINISHED:
            self.webview.run_javascript(
                JAVSCRIPT_BRIDGE_CODE,
                callback=lambda *args: [
                    self.expose_function(
                        func, func_name
                    )  # handle unregistered functions (exposed before bridge init)
                    for func_name, func in self._registered_functions.items()
                ],
            )
            self._bridge_initialized = True
        return

    def expose_function(self, func: Callable, func_name: str = None):
        name = func_name or func.__name__
        self._registered_functions[name] = func
        args = list(inspect.getfullargspec(func).args)
        if self._bridge_initialized:
            return self.webview.run_javascript(
                f"window.fabric.createBridge([{{func: '{name}', args: {args}}}])"
            )
        return  # on_load_finish should handle this

    def on_javascript_call(
        self,
        content_manager: WebKit2.UserContentManager,
        js_result: WebKit2.JavascriptResult,
    ):
        func_name, func_args, value_id = json.loads(
            js_result.get_js_value().to_string()
        )
        func = self._registered_functions.get(func_name)

        if func is not None:
            try:
                GLib.Thread.new(
                    "call-from-js",
                    self.do_javascript_callback,
                    func_name,
                    func,
                    func_args,
                    value_id,
                )
            except Exception as e:
                logger.warning(
                    f"[WebView][JavaScriptBridge] can't create a thread for calling a function {func_name}: {e}"
                )
        else:
            logger.warning(
                f"[WebView][JavaScriptBridge] javascript is trying to call a function ({func_name}) that doesn't exist"
            )
        return

    def do_javascript_callback(self, func_name, func, args, value_id):
        logger.debug(
            f"[WebView][JavaScriptBridge] calling python function from javascript, function name {func_name} with args {args}"
        )
        try:
            result = func(*args.values())
            result = json.dumps(result).replace("\\", "\\\\").replace("'", "\\'")
            code = f'window.fabric._pool["{func_name}"]["{value_id}"] = {{value: \'{result}\'}}'
        except Exception as e:
            print(traceback.format_exc())
            error = {
                "message": str(e),
                "name": type(e).__name__,
                "stack": traceback.format_exc(),
            }
            result = json.dumps(error).replace("\\", "\\\\").replace("'", "\\'")
            code = f"window.fabric._pool['{func_name}']['{value_id}'] = {{error: true, value: '{result}'}}"
        return self.webview.run_javascript(code)


class WebView(WebKit2.WebView, Widget):
    """
    a widget for loading a web page, it can load local and remote pages
    it provides a bridge to communicate with python from javascript
    to expose python functions to javascript, use the `expose_function` method of the `bridge` property
    NOTE: using the bridge with non-local pages is not recommended for security reasons
    """

    def __init__(
        self,
        url: str = None,
        open_inspector: bool = False,
        open_bridge: bool = True,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_compiled: bool = True,
        style_append: bool = False,
        style_add_brackets: bool = True,
        tooltip_text: str | None = None,
        tooltip_markup: str | None = None,
        h_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        v_align: Literal["fill", "start", "end", "center", "baseline"]
        | Gtk.Align
        | None = None,
        h_expand: bool = False,
        v_expand: bool = False,
        name: str | None = None,
        size: tuple[int] | int | None = None,
        **kwargs,
    ):
        """
        :param url: the url to load, defaults to None
        :type url: str, optional
        :param open_inspector: whether the inspector window should be opened or not, defaults to False
        :type open_inspector: bool, optional
        :param open_bridge: whether the python to javascript bridge should be opened or not (useful for security reasons), defaults to True
        :type open_bridge: bool, optional
        :param visible: whether the widget is initially visible, defaults to True
        :type visible: bool, optional
        :param all_visible: whether all child widgets are initially visible, defaults to False
        :type all_visible: bool, optional
        :param style: inline css style string, defaults to None
        :type style: str | None, optional
        :param style_compiled: whether the passed css should get compiled before applying, defaults to True
        :type style_compiled: bool, optional
        :param style_append: whether the passed css should be appended to the existing css, defaults to False
        :type style_append: bool, optional
        :param style_add_brackets: whether the passed css should be wrapped in brackets if they were missing, defaults to True
        :type style_add_brackets: bool, optional
        :param tooltip_text: the text added to the tooltip, defaults to None
        :type tooltip_text: str | None, optional
        :param tooltip_markup: the markup added to the tooltip, defaults to None
        :type tooltip_markup: str | None, optional
        :param h_align: the horizontal alignment, defaults to None
        :type h_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param v_align: the vertical alignment, defaults to None
        :type v_align: Literal["fill", "start", "end", "center", "baseline"] | Gtk.Align | None, optional
        :param h_expand: the horizontal expansion, defaults to False
        :type h_expand: bool, optional
        :param v_expand: the vertical expansion, defaults to False
        :type v_expand: bool, optional
        :param name: the name of the widget it can be used to style the widget, defaults to None
        :type name: str | None, optional
        :param size: the size of the widget, defaults to None
        :type size: tuple[int] | int | None, optional
        """
        self.content_manager = WebKit2.UserContentManager()
        WebKit2.WebView.__init__(
            self,
            user_content_manager=self.content_manager,
            **self.do_get_filtered_kwargs(kwargs),
        )
        Widget.__init__(
            self,
            visible,
            all_visible,
            style,
            style_compiled,
            style_append,
            style_add_brackets,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            name,
            size,
        )
        self.bridge = (
            JavaScriptBridge(self, self.content_manager)
            if open_bridge is True
            else None
        )
        self.load_uri(url) if url is not None else None
        if open_inspector is True:
            self.get_settings().set_enable_developer_extras(True)
            self.get_inspector().show()
        self.do_connect_signals_for_kwargs(kwargs)
