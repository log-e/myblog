from myblog import app, db
from .models import User, Article
import click

@app.cli.command()
def forge():
    """ fake data to database """
    db.create_all()
    pass


@app.cli.command()
@click.option('--drop', is_flag=True, help="Create after drop")
def initdb(drop):
    ''' init the database '''
    if drop:
        db.drop_all()
    db.create_all()
    click.echo("Initialized database")


@app.cli.command()
@click.option('--username', prompt = True, help="the username of login")
@click.option('--password', prompt = True, hide_input = True, confirmation_prompt = True, help = "The password to login")
def admin(username, password):
    """ create an admin account"""
    db.create_all()
    user = db.query.first()
    if user is not None:
        click.echo("updating user...")
        user.username = username
        user.set_password(password)
    else:
        click.echo("Creating user...")
        user = User(username = username, name = 'Admin')
        user.set_password(password)
    db.session.commit()
    click.echo('Done')