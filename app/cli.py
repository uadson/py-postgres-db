import typer
from typing import Optional
from rich.console import Console
from rich.table import Table
from rich import print

from core import add_car_to_database

main = typer.Typer(help="Car Management Application")
console = Console()


@main.command()
def add(
    brand: str,
    model: str,
    price: float,
):
    """Adds a new car to the database"""
    if add_car_to_database(brand, model, price):
        print(":car_mug: Car added !!")
    else:
        print(":no_entry: - Cannot add car.")
