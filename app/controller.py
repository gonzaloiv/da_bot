import pdb as d
from peewee import *

import telebot
from telebot import types

from config import API_KEY

from helper import *
from models import User

def initialize_bot():

	bot = telebot.TeleBot(API_KEY)

	markup = types.ReplyKeyboardMarkup(row_width=3, one_time_keyboard=True)
	markup.add(u"\U0001F464" + 'Collect', u"\U0001F464" + 'Status', u"\U0001F464" + 'Options')

	@bot.message_handler(commands=['help'])
	def send_welcome(message):
		bot.send_message(message.chat.id, "Futbol Manager  \n Registrar Jugador - /register")

	@bot.message_handler(commands=['start'])
	def send_start(message):
		try:
			user = User(name=message.from_user.first_name, telegram_id=message.from_user.id)
			user.save()
			bot.reply_to(message, "Usuario registrado:  " + user.name)
		except:
			user =  User.get(User.telegram_id == message.from_user.id)
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
			bot.send_photo(message.chat.id, open('./standing.jpg', 'rb'))
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))

	@bot.message_handler(func=lambda m: True)
	def echo_all(message):
		msg = bot.send_message(message.chat.id, "Y ahora que quieres hacer?", reply_markup=markup)
		bot.register_next_step_handler(msg, process_keyboard_input)
	def process_keyboard_input(message):
		user = User.get(User.telegram_id == message.from_user.id)
		try:
			if(message.text ==  u"\U0001F464" + 'Collect'):
				bot.reply_to(message, user.collect())
			if(message.text == u"\U0001F464" + 'Status'):
				bot.reply_to(message, user.status())
			if(message.text == u"\U0001F464" + 'Quien soy?'):
				bot.reply_to(message, user.name)
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))

	return bot
