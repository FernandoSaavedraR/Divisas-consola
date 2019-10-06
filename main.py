import click
from commands import exchange_commands as exchanges_commands
@click.group()
@click.pass_context
def ini(ctx):
    ctx.obj = {}

ini.add_command(exchanges_commands.all)

