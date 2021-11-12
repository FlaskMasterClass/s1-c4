from app import app
import click 



@click.Group
def cli():
    pass

@cli.command('runserver')
def runserver():
    app.run()

if __name__ == '__main__':
    cli()