import telebot
from peewee import *
import controller

if __name__ == '__main__':
    controller.initialize_bot().polling()