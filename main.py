import click
from commands import exchange_commands as exchanges_commands

EXCHANGE_TABLE = 'data/.divisas.csv'
@click.group()
@click.pass_context
def ini(ctx):
    ctx.obj = {}
    ctx.obj['exchange_table']=EXCHANGE_TABLE

ini.add_command(exchanges_commands.all)

