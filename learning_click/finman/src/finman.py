import click
from helpers.file_handlers import read_json_file, write_json_file, if_file_exists
from cons import OUTPUT_FILE_PATH
from expense import add_expense, list_expenses, delete_expense
from budget import set_budget, view_budget


@click.group(name="finman")
@click.option("--verbose", default=False)
@click.pass_context
def cli(ctx, verbose):
    data = read_json_file(OUTPUT_FILE_PATH)

    expense = list() if data.get("expense", None) is None else data["expense"]
    budget = list() if data.get("budget", None) is None else data["budget"]
    verbose = verbose
    output_file_path = OUTPUT_FILE_PATH

    ctx.obj = {
        "expense": expense,
        "budget": budget,
        "verbose": verbose,
        "output_file_path": output_file_path,
    }


## here i wil define the group
@cli.group(name="expense")
@click.pass_context
def expense(ctx):
    pass


## here I will define the group
@cli.group(name="budget")
@click.pass_context
def budget(ctx):
    pass


if __name__ == "__main__":
    ## add the commands to the expense
    expense.add_command(add_expense)
    expense.add_command(list_expenses)
    expense.add_command(delete_expense)

    ## add the commands for budget
    budget.add_command(set_budget)
    budget.add_command(view_budget)
    cli()
