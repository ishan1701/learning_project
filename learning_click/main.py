import click

@click.command("first_command")
@click.option('--name', default='World', help='Name to greet')
@click.argument('something')
def cli(name, something):
    """Main entry point for the CLI."""
    click.echo(f"Hello World! I am {name}")
    click.echo(f"Hello World! I am {something}")



