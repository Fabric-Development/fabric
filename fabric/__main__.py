import click
from fabric.client import get_fabric_session_bus


@click.group()
def main():
    pass


@click.command(name="info", help="info about running fabric service")
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def info(json: bool = False):
    try:
        bus_object = get_fabric_session_bus()
        file = str(bus_object.file())
    except:
        return (
            click.echo("fabric service is not running.")
            if json is False
            else click.echo({"file": "", "error": "fabric service is not running."})
        )
    return (
        click.echo(f"fabric service is running at file: {file}")
        if json is False
        else click.echo({"file": str(get_fabric_session_bus().get_file())})
    )


@click.command(
    "execute", help="executes a python code within the running fabric service"
)
@click.argument("source")
@click.option(
    "--raise-on-exception",
    "-r",
    is_flag=True,
    help="to raise the exception (if any), else it will return it (and suppress the exception)",
)
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def execute(source: str, raise_on_exception: bool = False, json: bool = False):
    try:
        bus_object = get_fabric_session_bus()
        data = bus_object.execute("(sb)", source, raise_on_exception)
    except:
        return (
            click.echo("fabric service is not running.")
            if json is False
            else click.echo(
                {
                    "source": source,
                    "exception": "",
                    "error": "fabric service is not running.",
                }
            )
        )
    return (
        click.echo(data)
        if json is False
        else click.echo(
            {
                "source": source,
                "exception": data[1] if isinstance(data, (tuple, list)) else data,
            }
        )
    )


if __name__ == "__main__":
    main.add_command(info)
    main.add_command(execute)

    main()
