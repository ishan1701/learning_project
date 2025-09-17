from datetime import datetime

import click
from helpers.file_handlers import write_json_file


@click.command(name="add-expense")
@click.argument("amount", type=click.FLOAT)
@click.argument("category", type=click.STRING)
@click.option("--note", type=click.STRING, help="Optional note for the expense")
@click.pass_context
def add_expense(
    ctx: click.Context, amount: click.FLOAT, category: click.STRING, note: click.STRING
):
    if len(ctx.obj["expense"]) == 0:
        ctx.obj["expense"] = [
            {
                "id": 1,
                "amount": amount,
                "category": category,
                "note": note,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        ]
    else:
        ctx.obj["expense"].append(
            {
                "id": ctx.obj["expense"][-1]["id"] + 1,
                "amount": amount,
                "category": category,
                "note": note,
                "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            }
        )

    write_json_file(
        path=ctx.obj["output_file_path"],
        data={"expense": ctx.obj["expense"], "budget": ctx.obj["budget"]},
    )
    click.echo(f"the expense added successfully")


@click.command(name="list-expenses")
@click.pass_context
def list_expenses(ctx: click.Context):
    data = ctx.obj["expense"]
    for expense in data:
        click.echo(
            f"ID: {expense['id']}, Amount: {expense['amount']}, Category: {expense['category']}, Note: {expense['note']}, Date: {expense['date']}"
        )


@click.command(name="delete-expense")
@click.option("--id", type=click.INT, required=True, help="ID of the expense to delete")
@click.pass_context
def delete_expense(ctx, id):
    expense = ctx.obj["expense"]
    budget = ctx.obj["budget"]

    print(expense)

    expense = [item for item in expense if item["id"] != id]

    write_json_file(
        path=ctx.obj["output_file_path"],
        data={"expense": expense, "budget": ctx.obj["budget"]},
    )
    click.echo(f"the expense has been deleted successfully")
