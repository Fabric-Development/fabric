import ast
import click
from fabric.client import get_fabric_session_bus


@click.group()
def main():
    pass


@click.command(name="info", help="info about running fabric service")
@click.option("--json", "-j", is_flag=True, help="to return the output in json format")
def info(json: bool = False):
    bus_object = get_fabric_session_bus()
    if bus_object is None:
        return (
            click.echo("fabric service is not running.")
            if json is False
            else click.echo({"file": "", "error": "fabric service is not running."})
        )
    file = str(bus_object.file())
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
    bus_object = get_fabric_session_bus()
    if bus_object is None:
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
    data = bus_object.execute(source, raise_on_exception)
    try:
        decoded_data = ast.literal_eval(data)
    except:
        decoded_data = data
    return (
        click.echo(decoded_data)
        if json is False
        else click.echo(
            {
                "source": source,
                "exception": decoded_data[1]
                if isinstance(decoded_data, (tuple, list))
                else decoded_data,
            }
        )
    )


if __name__ == "__main__":
    main.add_command(info)
    main.add_command(execute)

    main()
