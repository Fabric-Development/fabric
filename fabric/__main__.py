import click
from json import dumps as serialize_json
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
        if with_json:
            command = click.command(name=name, help=help)(
                lambda *args, json=False, **kwargs: (
                    rval := func(*args, json=json, **kwargs),
                    click.echo(serialize_json(rval) if json else rval)
                    if rval
                    else None,
                )
            )
        else:
            command = click.command(name=name, help=help)(func)

        if needs_instance:
            command = click.argument("instance")(command)

        for ext in extra:
            command = ext(command)  # type: ignore

        if with_json:
            command = click.option(
                "--json", "-j", is_flag=True, help="to return the output in json format"
            )(command)

        return command

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
        return {"instances-dbus-names": list(filtered_names)}
    for dbus_name in filtered_names:
        config_name: str = dbus_name.removeprefix(FABRIC_DBUS_INTERFACE_NAME + ".")
        proxy = get_instance_proxy(dbus_name)
        click.echo(
            f"{config_name}: {str(proxy.get_cached_property('File').unpack())}"
        ) if proxy is not None else None
    return


@command(
    name="list-actions",
    help="list actions in a currently running fabric instance",
    needs_instance=True,
)
def list_actions(instance: str, json: bool = False):
    bus_object = check_and_get_instance_proxy(instance, json)
    actions: dict[str, list[str]] = dict(bus_object.get_cached_property("Actions"))  # type: ignore

    if json:
        return actions

    for name, args in actions.items():
        click.echo(f"{name} ({', '.join(args)})")
    return


@command(
    "invoke-action",
    "invoke an action within a running fabric instance",
    True,
    True,
    click.argument("action-name"),
    click.argument("arguments", nargs=-1),
)
def invoke_action(
    instance: str, action_name: str, arguments: tuple[str, ...], json: bool = False
):
    bus_object = check_and_get_instance_proxy(instance, json)
    err, msg = bus_object.InvokeAction("(sas)", action_name, arguments)

    if json:
        return {"error": err, "message": msg}

    if err:
        return f"couldn't invoke action\nerror: {msg}"

    return f"action invoked\nreturn message: {msg}"


@command(
    "execute",
    "executes a python code within the running fabric instance",
    True,
    True,
    click.argument("source"),
)
def execute(instance: str, source: str, json: bool = False):
    bus_object = check_and_get_instance_proxy(instance, json)
    exc = bus_object.Execute("(s)", source)
    if json:
        return {"source": source, "exception": exc}
    if exc:
        return f"exception: {exc}"
    return


@command(
    "evaluate",
    "evaluate a python code within a running fabric instance and return the result",
    True,
    True,
    click.argument("code"),
)
def evaluate(instance: str, code: str, json: bool = False):
    bus_object = check_and_get_instance_proxy(instance, json)
    result, exc = bus_object.Evaluate("(s)", code)

    if json:
        return {"code": code, "result": result, "exception": exc}

    return "result: " + (result + "\nexception: " + exc if exc != "" else result)


@click.group()
def main():
    pass


if __name__ == "__main__":
    main.add_command(list_all)
    main.add_command(list_actions)
    main.add_command(execute)
    main.add_command(evaluate)
    main.add_command(invoke_action)

    main()
