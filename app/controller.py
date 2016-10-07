import telebot
from helper import *

def initialize_bot():

	bot = telebot.TeleBot("269247137:AAFkNU_uW9IlZN8svGGisMP3TFNdIQAXm1Q")

	@bot.message_handler(commands=['start', 'help'])
	def send_welcome(message):
		bot.reply_to(message, "Wat da bot?")

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
