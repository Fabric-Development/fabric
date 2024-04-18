import gi
import atexit
from loguru import logger
from fabric.client import get_fabric_dbus_proxy, get_dbus_client

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def start(open_client: bool = True, raise_on_client_error: bool = True):
    def on_client_error(hook, _, error):
        if error is not None and raise_on_client_error is not False:
            raise error
        return

    def on_exit():
        # assuming clean exit
        return logger.info("[Fabric] exiting...")

    atexit.register(on_exit)

    if open_client is True:
        logger.info("[Fabric] starting the DBus client")
        try:
            old_client = get_fabric_dbus_proxy()
            old_client.Log(
                "(ys)",
                2,
                "[Fabric] another client instance tried to run, but this instance is already running",
            )
            logger.warning(
                "[Fabric] another client instance is already running, skipping starting a DBus client"
            )
        except:
            client = get_dbus_client()
            client._hook.connect("execute-error", on_client_error)
            client._hook.connect("evaluate-error", on_client_error)
    try:
        Gtk.main()
    except KeyboardInterrupt:
        pass
