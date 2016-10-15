import telebot
from peewee import *
from controller import *
from models import *

bot = initialize_bot()
bot.polling()
