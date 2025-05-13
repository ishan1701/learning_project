import click



@click.command(name='hello')
@click.option('--name', default='World', help='Name to greet')
@click.argument('something')
def say_hello(name, something):
    """Say hello to the user."""
    click.echo(f"Hello, {name}!")
    click.echo(f"Hello, {something}!")


@click.command(name='goodbye')
@click.option('--name', default='World', help='Name to bid farewell')
@click.argument('something')
def say_goodbye(name, something):
    """Bid farewell to the user."""
    click.echo(f"Goodbye, {name}!")
    click.echo(f"Goodbye, {something}!")


# cli.add_command(say_goodbye)
# cli.add_command(say_hello)
