import click
from services.convert_services import convert_service
from classes.exchange import Exchange
from services.exchange_services import Exchange_services

@click.group()
def convert():
    """Convert the currency to another"""
    pass
@convert.command()
@click.option('-e','--exchange',type=str,prompt=True,help='currency acronym',default="mxn")
@click.option('-q','--quantity',type=float,prompt=True,help='quantity to convert',default=1)
@click.option('-r','--release',type=str,prompt=True,help='Export to a csv file',default="No")
@click.pass_context
def ota(ctx,exchange,quantity,release):
    """show the value of a currency in all the values saved"""
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    con_service = convert_service(ctx.obj['exchange_table'])
    listE = exc_service.list_exchanges()
    exchanges = con_service.one_to_all(listE,exchange,quantity,release)
    click.echo('-'*73)
    click.echo('|  {exchange} |  {value} |  {country} |'.format(
        #uid = 'UID'.center(36,' '),
        exchange = 'Currencies'.center(20,' '),
        value = 'BASE/VALUE'.center(20,' '),
        country = 'COUNTRY'.center(20,' ')
    ))
    click.echo('-'*73)
   
    for exchange in exchanges:
        click.echo('|  {exchange} |  {value} |  {country} |'.format(
            #uid = exchange['uid'].center(20,' '),
            exchange = exchange['exchange'].center(20,' '),
            value = str(exchange['value']).center(20,' '),
            country = exchange['country'].center(20,' ')
        ))
        click.echo('-'*73)

@convert.command()
@click.option('-e','--exchange',type=str,prompt=True,help='currency acronym',default="mxn")
@click.option('-c','--conversion',type=str,prompt=True,help='currency acronym',default="mxn")
@click.option('-q','--quantity',type=float,prompt=True,help='quantity to convert',default=1)
@click.pass_context
def oto(ctx,exchange,conversion,quantity):
    """convert in one currency"""
    exc_service = Exchange_services(ctx.obj['exchange_table'])
    con_service = convert_service(ctx.obj['exchange_table'])
    listE = exc_service.list_exchanges()
    exchanges = con_service.one_to_one(listE,exchange,conversion,quantity)
    if exchanges:
        click.echo('-'*93)
        click.echo('| {baseP} | {conversionP} | {quantityP} | {conversionD} |'.format(
            baseP = "exchange".center(20,' ').upper(),
            conversionP = "conversion".center(20, ' ').upper(),
            quantityP= "quantity".center(20, ' ').upper(),
            conversionD = "value".center(20,' ').upper(),
        ))
        click.echo('-'*93)
        click.echo('| {baseP} | {conversionP} | {quantityP} | {conversionD} |'.format(
            baseP = exchange.center(20,' '),
            conversionP = conversion.center(20, ' '),
            quantityP= str(quantity).center(20, ' '),
            conversionD = str(exchanges["value"]).center(20,' '),
        ))
        click.echo('-'*93)
    else:
        click.echo('empty data')


#@convert.command()
#@click.pass_context
def fta(ctx):
    """load the data from an external file and convert to all currencies"""
    pass


#@convert.command()
#@click.pass_context
def fto(ctx):
    """load the data from an external file and convert to a currency"""
    pass


all = convert