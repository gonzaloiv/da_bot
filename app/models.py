from peewee import *

from config import DATABASE_NAME

# from main import db

db = SqliteDatabase(DATABASE_NAME)
db.connect()

class BaseModel(Model):
  class Meta:
    database = db

class User(BaseModel):
  name = CharField()
  telegram_id = TextField(unique=True)

db.drop_tables([User])
db.create_tables([User])
