import gi
import json
import inspect
import traceback
from loguru import logger
from collections.abc import Iterable, Callable
from typing import Literal, overload
from fabric.widgets.widget import Widget
from fabric.utils.helpers import get_relative_path

gi.require_version("Gtk", "3.0")
gi.require_version("WebKit2", "4.1")
from gi.repository import Gtk, GLib, WebKit2


def get_javascript_bridge_code() -> str:
    with open(get_relative_path("./javascript_bridge.js"), "r") as f:
        return f.read()


JAVASCRIPT_BRIDGE_CODE = get_javascript_bridge_code()


class JavaScriptBridge:
    def __init__(
        self,
        webview: "WebView",
        content_manager: WebKit2.UserContentManager,
        *args,
        **kwargs,
    ):
        super().__init__(*args, **kwargs)
        self._registered_functions: dict[str, Callable] = {}
        self._bridge_initialized: bool = False

        self.webview = webview
        self.content_manager = content_manager
        self.content_manager.register_script_message_handler("fabricJsBridge")
        self.content_manager.connect("script-message-received", self.on_javascript_call)
        self.webview.connect("load_changed", self.on_load_finish)  # odd signal name

    def on_load_finish(self, _: WebKit2.WebView, status: WebKit2.LoadEvent):
        # inject javascript bridge as soon as the page is loaded
        if status == WebKit2.LoadEvent.FINISHED:
            self.webview.run_javascript(
                JAVASCRIPT_BRIDGE_CODE,
                callback=lambda *args: [
                    self.expose_function(
                        func, func_name
                    )  # handle unregistered functions (exposed before bridge init)
                    for func_name, func in self._registered_functions.items()
                ],
            )
            self._bridge_initialized = True
        return

    def expose_function(self, func: Callable, func_name: str | None = None):
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
        _: WebKit2.UserContentManager,
        js_result: WebKit2.JavascriptResult,
    ):
        func_name, func_args, value_id = json.loads(
            js_result.get_js_value().to_string()  # a serialized json string is what we expect
        )
        func_name: str
        func_args: dict[str, str]
        value_id: int
        func = self._registered_functions.get(func_name)
        if not func:
            return logger.warning(
                f"[WebView][JavaScriptBridge] javascript is trying to call a function ({func_name}) that doesn't exist"
            )
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

    def do_javascript_callback(
        self, func_name: str, func: Callable, args: dict[str, str], value_id: int
    ):
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
    it provides a bridge to communicate with python from javascript (and vice versa)
    ---
    ## `.bridge`
    this object will hold a field for interacting with the javascript
    bridge, the field name is `bridge`, it will be set only if you set `open_bridge` to `True`
    otherwise it will be set to `None`

    ## exposing functions
    to expose a python function you can use the method `expose_function` which's a member of the `bridge` field

    ### security warning
    using the bridge with non-local pages is not recommended for security reasons
    """

    @overload
    def __init__(
        self,
        url: None = None,
        html: None = None,
        open_bridge: bool = True,
        open_inspector: bool = False,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ): ...
    @overload
    def __init__(
        self,
        url: str | None = None,
        html: None = None,
        open_bridge: bool = True,
        open_inspector: bool = False,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ): ...
    @overload
    def __init__(
        self,
        url: None = None,
        html: str | None = None,
        open_bridge: bool = True,
        open_inspector: bool = False,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ): ...

    def __init__(
        self,
        url: str | None = None,
        html: str | None = None,
        open_bridge: bool = True,
        open_inspector: bool = False,
        name: str | None = None,
        visible: bool = True,
        all_visible: bool = False,
        style: str | None = None,
        style_classes: Iterable[str] | str | None = None,
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
        size: Iterable[int] | int | None = None,
        **kwargs,
    ):
        WebKit2.WebView.__init__(
            self,  # type: ignore
            user_content_manager=WebKit2.UserContentManager(),
        )
        Widget.__init__(
            self,
            name,
            visible,
            all_visible,
            style,
            style_classes,
            tooltip_text,
            tooltip_markup,
            h_align,
            v_align,
            h_expand,
            v_expand,
            size,
            **kwargs,
        )
        if url is not None and html is not None:
            raise ValueError("you can't pass both url and html")

        self.bridge = (
            JavaScriptBridge(self, self.get_user_content_manager())
            if open_bridge is True
            else None
        )

        if url is not None:
            if self.bridge is not None and url.startswith(("http://", "https://")):
                logger.warning(
                    "[WebView] it's not generally a good idea to expose a javascript interface for the world wide web, consider closing the javascript bridge"
                )
            self.load_uri(url)
        elif html is not None:
            self.load_html(html, None)

        self.get_settings().set_enable_developer_extras(True)
        if open_inspector is True:
            self.open_inspector()

    def open_inspector(self):
        self.get_inspector().show()
