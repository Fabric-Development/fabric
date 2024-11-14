import click
from gi.repository import GLib, Gio

FABRIC_DBUS_INTERFACE_NAME = "org.Fabric.fabric"
FABRIC_DBUS_OBJECT_PATH = "/org/Fabric/fabric"


def get_dbus_names() -> GLib.Variant:
    return (
        Gio.bus_get_sync(Gio.BusType.SESSION)
        .call_sync(
            "org.freedesktop.DBus",
            "/org/freedesktop/DBus",
            "org.freedesktop.DBus",
            "ListNames",
            GLib.Variant("()", ()),
            GLib.VariantType("(as)"),  # type: ignore
            Gio.DBusCallFlags.NONE,
            -1,
            None,
        )
        .get_child_value(0)
    )


def name_running(name: str) -> bool:
    return (
        Gio.bus_get_sync(Gio.BusType.SESSION)
        .call_sync(
            "org.freedesktop.DBus",
            "/org/freedesktop/DBus",
            "org.freedesktop.DBus",
            "NameHasOwner",
            GLib.Variant("(s)", (name,)),
            GLib.VariantType("(b)"),  # type: ignore
            Gio.DBusCallFlags.NONE,
            -1,
            None,
        )
        .get_child_value(0)
        .get_boolean()
    )


def get_instance_proxy(iface_name: str) -> Gio.DBusProxy:
    return Gio.DBusProxy.new_for_bus_sync(
        Gio.BusType.SESSION,
        Gio.DBusProxyFlags.NONE,
        None,
        iface_name,
        FABRIC_DBUS_OBJECT_PATH,
        FABRIC_DBUS_INTERFACE_NAME,
        None,
    )


def check_and_get_instance_proxy(config_name: str, json: bool = False) -> Gio.DBusProxy:
    if config_name.startswith(FABRIC_DBUS_INTERFACE_NAME):
        iface_name = config_name
    else:
        iface_name = FABRIC_DBUS_INTERFACE_NAME + (
            f".{config_name}" if config_name else ""
        )
    if not name_running(iface_name):
        message = f"couldn't find a running Fabric instance with the name {config_name}"
        if not json:
            click.echo(message)
        else:
            click.echo({"error": message})
        exit(1)
    return get_instance_proxy(iface_name)


def command(
    name: str,
    help: str = "",
    needs_instance: bool = True,
    with_json: bool = True,
    *extra,
):
    def decorator(func) -> click.Command:
        func = click.command(name=name, help=help)(func)
        if needs_instance:
            func = click.argument(
                "instance",  # help="the name of the instance to execute this command on"
            )(func)

        for ext in extra:
            func = ext(func)  # type: ignore

        if with_json:
            func = click.option(
                "--json", "-j", is_flag=True, help="to return the output in json format"
            )(func)
        return func

    return decorator


@command(
    name="list-all",
    help="list all currently running fabric instances",
    needs_instance=False,
)
def list_all(json: bool = False):
    filtered_names = filter(
        lambda x: x.startswith(FABRIC_DBUS_INTERFACE_NAME),  # type: ignore
        get_dbus_names(),  # type: ignore
    )
    if json:
        return click.echo({"instances-dbus-names": list(filtered_names)})
    for dbus_name in filtered_names:
        config_name: str = dbus_name.removeprefix(FABRIC_DBUS_INTERFACE_NAME + ".")
        # print(dbus_name)
        proxy = get_instance_proxy(dbus_name)
        click.echo(
            f"{config_name}: {str(proxy.get_cached_property('File').unpack())}"
        ) if proxy is not None else None
    return


@command(
    "execute",
    "executes a python code within the running fabric instance",
    True,
    True,
    click.argument(
        "source",
        # help="python source code to execute"
    ),
)
def execute(instance: str, source: str, json: bool = False):
    bus_object = check_and_get_instance_proxy(instance, json)
    exc = bus_object.Execute("(s)", source)
    return (
        click.echo("exception: " + exc)
        if exc != ""
        else None
        if json is False
        else click.echo(
            {
                "source": source,
                "exception": exc,
            }
        )
    )


@command(
    "evaluate",
    "evaluate a python code within a running fabric instance and return the result",
    True,
    True,
    click.argument(
        "code",
        # help="python code to execute"
    ),
)
def evaluate(instance: str, code: str, json: bool = False):
    bus_object = check_and_get_instance_proxy(instance, json)
    result, exc = bus_object.Evaluate("(s)", code)
    return (
        click.echo(
            "result: " + (result + "\nexception: " + exc if exc != "" else result)
        )
        if not json
        else click.echo(
            {
                "code": code,
                "result": result,
                "exception": exc,
            }
        )
    )


@click.group()
def main():
    pass


if __name__ == "__main__":
    main.add_command(list_all)
    main.add_command(execute)
    main.add_command(evaluate)

    main()
