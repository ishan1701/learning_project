import click
from helpers.file_handlers import write_json_file


@click.command(name="set-budget")
@click.argument("category", type=click.STRING)
@click.argument("amount", type=click.FLOAT)
@click.pass_context
def set_budget(ctx: click.Context, category: str, amount: float):
    if len(ctx.obj["budget"]) == 0:
        ctx.obj["budget"] = [
            {
                category: amount,
            }
        ]
    else:
        ctx.obj["budget"].append(
            {
                category: amount,
            }
        )

    write_json_file(
        path=ctx.obj["output_file_path"],
        data={"expense": ctx.obj["expense"], "budget": ctx.obj["budget"]},
    )
    click.echo(f"the budget added successfully")


@click.command(name="view-budget")
@click.option("--category", type=click.STRING)
@click.pass_context
def view_budget(ctx: click.Context, category: str):
    budget = ctx.obj["budget"]
    if len(budget) == 0:
        click.echo("no budget")
        return
    for item in budget:
        for k, v in item.items():
            if k == category:
                click.echo(f"Category: {k}, Amount: {v}")
                return
    else:
        for item in budget:
            click.echo(item)
