import telebot
from peewee import *
from controller import *

db = SqliteDatabase('people.db')

class Person(Model):
    name = CharField()

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
#db.create_tables([Person])

Person(name='Bob').save()
print Person.get(Person.name == 'Bob').name


bot = initialize_bot()

bot.polling()
