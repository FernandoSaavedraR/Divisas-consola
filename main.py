import click
from commands import exchange_commands as exchanges_commands
from commands import convert_commands as convert_commands
EXCHANGE_TABLE = 'data/.divisas.csv'
@click.group()
@click.pass_context
def ini(ctx):
    """The base currency of 
        the system is mxn
    """
    ctx.obj = {}
    ctx.obj['exchange_table']=EXCHANGE_TABLE

ini.add_command(exchanges_commands.all)
ini.add_command(convert_commands.all)
