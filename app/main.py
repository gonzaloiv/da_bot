import telebot
import pdb
from peewee import *
from controller import *
# from user import User

db = SqliteDatabase('bot.db')

db.connect()

bot = initialize_bot(db)

bot.polling()
