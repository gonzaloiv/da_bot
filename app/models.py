from peewee import *
from main import *

class User(Model):
    name = CharField()

    class Meta:
        database = main.db # This model uses the "people.db" database.