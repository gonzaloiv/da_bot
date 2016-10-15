import telebot
from peewee import *
import datetime

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
  level = IntegerField()
  experience = IntegerField()
  money = IntegerField()
  fans = IntegerField()
  lastRecolect = TimestampField()
  joinDate = TimestampField()

  def collect(self):
    if(self.lastRecolect < datetime.datetime.now() - datetime.timedelta(minutes=1)):
      self.update(money = self.money + self.fans * 1).where(self.telegram_id == message.from_user.id).execute()
      self.update(lastRecolect = datetime.datetime.now()).where(self.telegram_id == message.from_user.id).execute()
      #self.update(fans = 2).where(self.telegram_id == message.from_user.id).execute()
      return "Recolectado!"
    else:
      return "Debes esperar 1 min desde la ultima vez para recolectar"

  def status(self):
      return (
        u"\U0001F464" + " Nombre: " + self.name + "\n"
        + "Nivel: " + str(self.level) + "\n"
        + "Experiencia: " + str(self.experience) + "\n"
        + "Dinero: " + str(self.money) + "\n"
        + "Socios: " + str(self.fans) + "\n"
        + "Rec: " + str(self.lastRecolect)
      )

db.drop_tables([User])
db.create_tables([User])
