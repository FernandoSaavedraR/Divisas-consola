import click

@click.group()
def exchanges():
    """Manages de currencies lifecycle"""
    pass


@exchanges.command()
@click.pass_context
def create(ctx,exchange,value,country):
    """Add a new currency to our system""" 
    pass


@exchanges.command()
@click.pass_context
def list(ctx):
    """List all currencies"""
    pass


@exchanges.command()
@click.pass_context
def update(ctx,exchange_id):
    """Updates an exchange"""
    pass


@exchanges.command()
@click.pass_context
def delete(ctx,exchange_id):
    """Delete an exchange"""
    pass


all = exchanges