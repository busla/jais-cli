import json
import csv
from typing import Annotated, Any, Iterable, Optional
from rich import print
from rich.console import Console
from rich.table import Table

import typer
import httpx

console = Console()


from jais.models.business import Business, Response

app = typer.Typer()


def get_base_url() -> str:
    return "https://api.ja.is/skra/v1"


def get_business_url() -> str:
    return f"{get_base_url()}/businesses"


def get_business(**params) -> Response:
    url = get_business_url()
    token = params.pop("token")
    res = httpx.get(
        url,
        headers={"Accept": "application/json", "Authorization": token},
        params=params,
    )
    data = Response.parse_obj(res.json())
    return data


def get_simple_table(data: list[Business]):
    table = Table(title="Company search results")

    for header in ["name", "ssn", "address", "type", "code"]:
        table.add_column(
            header,
            justify="left",
            style="cyan",
            no_wrap=True,
        )
    for b in data:
        if b.is_company:
            table.add_row(
                *[
                    b.full_name[:30],
                    b.kennitala,
                    b.address_out,
                    b.business_type_out,
                    b.business_type_code_out,
                ]
            )

    return table


def store(data: Iterable[Business]):
    fields = list(Business.schema()["properties"].keys())

    with open("test.csv", "w") as fp:
        writer = csv.DictWriter(fp, fieldnames=fields)
        writer.writeheader()
        for b in data:
            writer.writerow(json.loads(Business(**b.dict()).json()))


@app.callback()
def callback():
    """
    ja.is cli tool
    """


@app.command(name="search")
def cmd_business(
    ctx: typer.Context,
    token: Annotated[str, typer.Argument(envvar="JAIS_API_KEY")],
    name: Annotated[str, typer.Option("--name", "-n")] = "",
    postal_code: Annotated[str, typer.Option("--postal-code", "-p")] = "",
    start: Annotated[int, typer.Option("--start")] = 1,
    count: Annotated[int, typer.Option("--count", "-c")] = 1000,
    street: Annotated[str, typer.Option("--street", "-s")] = "",
    municipality: Annotated[str, typer.Option("--municipality", "-m")] = "",
    business_type: Annotated[str, typer.Option("--business-type", "-b")] = "",
    export: Annotated[bool, typer.Option("--export", "-e")] = True,
):
    """
    Search businesses
    """

    data = get_business(**ctx.params)

    simple = get_simple_table(data.items)
    if export:
        store(data.items)
    print(simple)
