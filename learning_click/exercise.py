import click
import json
from pathlib import Path

PATH= Path(__file__).parent.joinpath('data', 'task.json')

@click.group(name='taskman')
@click.option('--debug', default=False, help='Enable debug mode')
@click.pass_context
def cli(ctx, debug):
    if PATH.exists():
        with open(PATH, 'r') as file:
            data = json.load(file)
        TASKS = data['tasks']
        ctx.obj = {'debug': debug, 'tasks': TASKS}
    else:
        ctx.obj = {'debug': debug, 'tasks': list()}
    if debug:
        click.echo('Debug mode is on')

# this is one of the group commands
@cli.group(name='manage')
def manage():
    pass


@manage.command(name='add-task')
@click.argument('description')
@click.option('--priority', default='low')
@click.pass_context
def add_task(ctx, description, priority):
    task = {'description': description,
            'priority': priority,
            'completed': False}

    tasks = ctx.obj.get('tasks')
    tasks.append(task)
    with open(PATH, 'w') as file:
        file.write(json.dumps({'tasks': tasks}, indent=4))
    click.echo(f'Added task with description: {description} and priority: {priority}')

@manage.command(name='list-tasks')
@click.pass_context
def list_tasks(ctx):
    if not PATH.exists():
        click.echo('No data found')
        return
    with open(PATH, 'r') as f:
        tasks = json.load(f)
        if not tasks:
            click.echo('No tasks found')
            return
        else:
            for task in tasks['tasks']:
                click.echo(f"Task: {task['description']}, Priority: {task['priority']}, Completed: {task['completed']}")

@manage.command(name='complete-task')
@click.argument('index', type=int)
@click.pass_context
def complete_task(ctx, index):
    with open(PATH, 'r') as f:
        data = json.load(f)
    if not data:
        click.echo('No tasks found')
        return
    else:
        tasks = data['tasks']
        tasks[index]['completed'] = True
        with open(PATH, 'w') as f:
            f.write(json.dumps(data, indent=4))


# completed


# another grouo of command

@cli.command(name='status')
@click.pass_context
def status(ctx):
    click.echo(ctx.obj.get('debug'))
    for k ,v in ctx.obj.items():
        click.echo(f"{k}: {v}")




if __name__ == '__main__':
    cli()