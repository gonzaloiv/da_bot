import telebot
from config import API_KEY
from helper import *
from peewee import *


def initialize_bot(db):

	class User(Model):
			name = CharField()
			telegram_id = TextField()

			class Meta:
					database = db # This model uses the "people.db" database.

	db.drop_tables([User])
	db.create_tables([User])

	bot = telebot.TeleBot(API_KEY)

	@bot.message_handler(commands=['start', 'help'])
	def send_welcome(message):
			User(name=message.from_user.first_name, telegram_id=message.from_user.id).save()
			bot.reply_to(message, "Wat da bot? " + User.get(User.telegram_id == message.from_user.id).name)

	@bot.message_handler(commands=['foto'])
	def send_photo(message):
		try:
			photo_git = open('./standing.jpg', 'rb')
			bot.send_photo(message.chat.id, photo_git)
			bot.send_photo(message.chat.id, "photo_git_123abc.")
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))

	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		bot.reply_to(message, message.text + message.from_user.first_name)



	return bot
