import click
from faker import Faker
from faker.providers import lorem
from myblog import app, db
from .models import User, Article
import datetime

@app.cli.command()
@click.option("--count", help = "the number of ariticle you gernerate", type = click.INT)
def forge(count):
    """ fake data to database """
    db.create_all()
    fake = Faker('zh_CN')
    fake.add_provider(lorem)
    title_list = fake.sentences(nb=100)
    for i in range(0,count):
        article = Article(title=title_list[i], content = fake.text(3000), time = datetime.datetime.now())
        db.session.add(article)
    click.echo("created %d articles" % count)
    db.session.commit()
    click.echo(".Done")
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
    user = User.query.first()
    if user is not None:
        click.echo("updating user...")
        user.username = username
        user.set_password(password)
    else:
        click.echo("Creating user...")
        user = User(username = username, name = 'Admin')
        user.set_password(password)
        db.session.add(user)
    db.session.commit()
    click.echo('Done')