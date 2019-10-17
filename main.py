import click
import os
from commands.convert_commands import all as com_all
from commands.exchange_commands import all as exc_all
EXCHANGE_TABLE = 'data\.divisas.csv'
@click.group()
@click.pass_context
def ini(ctx):
    """The base currency of 
        the system is mxn
    """
    ctx.obj = {}
    ctx.obj['exchange_table']=EXCHANGE_TABLE

ini.add_command(com_all)
ini.add_command(exc_all)