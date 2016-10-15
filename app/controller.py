import telebot
from peewee import *

from config import API_KEY

from helper import *
from models import User
from telebot import types
import datetime

def initialize_bot():

	bot = telebot.TeleBot(API_KEY)


	@bot.message_handler(commands=['help'])
	def send_welcome(message):
		bot.send_message(message.chat.id, "Futbol Manager  \n Registrar Jugador - /register")

		
	@bot.message_handler(commands=['start'])
	def send_start(message):
		try:
			User(name=message.from_user.first_name, telegram_id=message.from_user.id, level=0, experience=0, money=0, fans=1).save()
			bot.reply_to(message, "Usuario registrado:  " + User.get(User.telegram_id == message.from_user.id).name)
			#bot.reply_to(message,"hola")
		except:
			bot.reply_to(message, "Usuario ya registrado: " + User.get(User.telegram_id == message.from_user.id).name 
			+ "Estado del usuario: /status")

	@bot.message_handler(commands=['status'])
	def send_status(message):
		try:
			bot.send_message(message.chat.id, u"\U0001F464" + " Nombre: " + User.get(User.telegram_id == message.from_user.id).name + "\n" 
			+ "Nivel: " + str(User.get(User.telegram_id == message.from_user.id).level) + "\n" 
			+ "Experiencia: " + str(User.get(User.telegram_id == message.from_user.id).experience) + "\n" 
			+ "Dinero: " + str(User.get(User.telegram_id == message.from_user.id).money) + "\n"
			+ "Socios: " + str(User.get(User.telegram_id == message.from_user.id).fans) + "\n"
			+ "Rec: " + str(User.get(User.telegram_id == message.from_user.id).lastRecolect)
			)

			#bot.send_message(message.chat.id, "Nombre: " + User.get(User.telegram_id == message.from_user.id).name)
		except Exception as e:
			bot.reply_to(message, cowsay(e.message))



	@bot.message_handler(commands=['collect'])
	def send_status(message):
		try:
			if(User.get(User.telegram_id == message.from_user.id).lastRecolect < datetime.datetime.now() - datetime.timedelta(minutes=1)):
				User.update(money = User.money + User.fans * 1).where(User.telegram_id == message.from_user.id).execute()
				User.update(lastRecolect = datetime.datetime.now()).where(User.telegram_id == message.from_user.id).execute()
				#User.update(fans = 2).where(User.telegram_id == message.from_user.id).execute()
				bot.send_message(message.chat.id, u"\U0001F464" + " Nombre: " + User.get(User.telegram_id == message.from_user.id).name + "\n" 
				+ "Nivel: " + str(User.get(User.telegram_id == message.from_user.id).level) + "\n" 
				+ "Experiencia: " + str(User.get(User.telegram_id == message.from_user.id).experience) + "\n" 
				+ "Dinero: " + str(User.get(User.telegram_id == message.from_user.id).money) + "\n"
				+ "Socios: " + str(User.get(User.telegram_id == message.from_user.id).fans) + "\n"
				+ "Rec: " + str(User.get(User.telegram_id == message.from_user.id).lastRecolect)
				)
			else:
				bot.send_message(message.chat.id, "Debes esperar 1 min desde la ultima vez para recolectar")	

			#bot.send_message(message.chat.id, "Nombre: " + User.get(User.telegram_id == message.from_user.id).name)
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
		bot.reply_to(message, message.text + message.from_user.first_name)

	return bot
