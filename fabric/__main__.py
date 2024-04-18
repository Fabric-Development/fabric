import click
from fabric.client import get_fabric_dbus_proxy


@click.group()
def main():
    pass


@click.command(
    name="info", help="gets info about the currently running fabric instance"
)
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def info(json: bool = False):
    try:
        bus_object = get_fabric_dbus_proxy()
        file = str(bus_object.get_cached_property("File").unpack())
    except:
        return (
            click.echo("fabric instance is not running.")
            if json is False
            else click.echo({"file": "", "error": "fabric instance is not running."})
        )
    return (
        click.echo(f"fabric instance is running at file: {file}")
        if json is False
        else click.echo({"file": file})
    )


@click.command(
    "execute", help="executes a python code within the running fabric instance"
)
@click.argument("source")
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def execute(source: str, json: bool = False):
    try:
        bus_object = get_fabric_dbus_proxy()
        exc = bus_object.Execute("(s)", source)
    except:
        return (
            click.echo("fabric instance is not running.")
            if json is False
            else click.echo(
                {
                    "source": source,
                    "exception": "",
                    "error": "fabric instance is not running.",
                }
            )
        )
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


@click.command(
    "evaluate", help="evaluates a python code within the running fabric instance"
)
@click.argument("code")
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def evaluate(code: str, json: bool = False):
    try:
        bus_object = get_fabric_dbus_proxy()
        result, exc = bus_object.Evaluate("(s)", code)
    except:
        return (
            click.echo("fabric instance is not running.")
            if json is False
            else click.echo(
                {
                    "code": code,
                    "result": "",
                    "exception": "",
                    "error": "fabric instance is not running.",
                }
            )
        )
    return (
        click.echo(
            "result: " + (result + "\nexception: " + exc if exc != "" else result)
        )
        if json is False
        else click.echo(
            {
                "code": code,
                "result": result,
                "exception": exc,
            }
        )
    )


if __name__ == "__main__":
    main.add_command(info)
    main.add_command(execute)
    main.add_command(evaluate)

    main()
