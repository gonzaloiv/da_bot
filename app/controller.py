import telebot
from telebot import types
from peewee import *

from config import API_KEY

from helper import *
from models import User

def initialize_bot():

	bot = telebot.TeleBot(API_KEY)

	@bot.message_handler(commands=['help'])
	def send_welcome(message):
		bot.send_message(message.chat.id, "Futbol Manager  \n Registrar Jugador - /register")

	@bot.message_handler(commands=['start'])
	def send_start(message):
		try:
			user = User(name=message.from_user.first_name, telegram_id=message.from_user.id, level=0, experience=0, money=0, fans=1)
			user.save()
			bot.send_message(message.chat_id, "Usuario registrado:  " + user.name)
		except:
			bot.reply_to(message, "Usuario ya registrado:  " + user.name)

	@bot.message_handler(commands=['status'])
	def send_status(message):
		try:
			user = User.get(User.telegram_id == message.from_user.id)
			bot.reply_to(message, user.status())
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))

	@bot.message_handler(commands=['collect'])
	def send_status_collect(message):
		try:
			user = User.get(User.telegram_id == message.from_user.id)
			bot.reply_to(message, user.collect())
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))

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
		markup = types.ReplyKeyboardMarkup()
		markup.add('Collect', 'Status')
		bot.register_next_step_handler(msg, process_keyboard_input)
	def process_keyboard_input(message):
		user = User.get(User.telegram_id == message.from_user.id)
		try:
			if(message.text == u'Collect'):
				bot.reply_to(message, user.collect())
			if(message.text == u'Status'):
				bot.reply_to(message, user.status())
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))


	return bot
