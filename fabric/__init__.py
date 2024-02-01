import gi
from loguru import logger
from fabric.client import get_fabric_session_bus, get_client

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


def on_exec(client, hook, code, error):
    if error is not None:
        raise error
    return


def start(open_client: bool = True):
    if open_client is True:
        logger.info("[Fabric] starting the DBus client")
        try:
            old_client = get_fabric_session_bus()
            old_client.log(
                "(si)",
                "[Fabric] another client instance tried to run, but this instance is already running",
                2,
            )
            logger.warning(
                "[Fabric] another client instance is already running, skipping starting a DBus client"
            )
        except:
            client = get_client()
            client.connect("exec", on_exec)
    try:
        Gtk.main()
    except KeyboardInterrupt:
        logger.info("[Fabric] exiting")
