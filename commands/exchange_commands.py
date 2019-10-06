import click
from classes.exchange import Exchange
from services.exchange_services import Exchange_services
@click.group()
def exchanges():
    """Manages currencies lifecycle"""
    pass


@exchanges.command()
@click.option('-e','--exchange',type=str,prompt=True,help='currency acronym')
@click.option('-v','--value',type=float,prompt=True,help='currency value')
@click.option('-c','--country',type=str,prompt=True,help='currency country')
@click.pass_context
def create(ctx,exchange,value,country):
    """Add a new currency to our system""" 
    exchange = Exchange(exchange,value,country)
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    exists = exc_service.exist_exchange(exchange)
    if(exists):
        exc_service.create_exchange(exchange)
        click.echo('Currency created')
    else:
        click.echo('The currency already exists')

@exchanges.command()
@click.pass_context
def listE(ctx):
    """List all currencies"""
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    exchanges = exc_service.list_exchanges()
    click.echo('-'*112)
    click.echo('| {uid} |  {exchange} |  {value} |  {country} |'.format(
        uid = 'UID'.center(36,' '),
        exchange = 'Currencies'.center(20,' '),
        value = 'VALUE'.center(20,' '),
        country = 'COUNTRY'.center(20,' ')
    ))
    click.echo('-'*112)
   
    for exchange in exchanges:
        click.echo('| {uid} |  {exchange} |  {value} |  {country} |'.format(
            uid = exchange['uid'].center(20,' '),
            exchange = exchange['exchange'].center(20,' '),
            value = exchange['value'].center(20,' '),
            country = exchange['country'].center(20,' ')
        ))
        click.echo('-'*112)


@exchanges.command()
@click.option('-e','--exchange',type=str,prompt=True,help='currency acronym')
@click.option('-v','--value',type=float,prompt=True,help='currency value')
@click.option('-c','--country',type=str,prompt=True,help='currency country')
@click.pass_context
def update(ctx,exchange,value,country):
    """Updates an currency"""
    exchange = Exchange(exchange,value,country)
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    message= exc_service.update_exchange(exchange)
    click.echo(message)


@exchanges.command()
@click.option('-e','--exchange',type=str,prompt=True,help='currency acronym')
@click.pass_context
def delete(ctx,exchange):
    """Delete an currency"""
    exc_temp = Exchange(exchange,0,None)
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    message=exc_service.delete_exchange(exc_temp)    
    click.echo(message)


@exchanges.command()
@click.pass_context
def export(ctx):
    """Create an csv file for analysis"""
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    exc_service.export()


all = exchanges