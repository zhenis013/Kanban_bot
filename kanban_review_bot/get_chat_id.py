import telebot
from telebot import types
import sqlite3
import database
from datetime import datetime


token = '2088217444:AAEwq4TpDJ0m5rGAVAoeDkSO174ao4MnxKc'


bot = telebot.TeleBot(token)

name = ''
chat_id = 0

@bot.message_handler(commands=['start'])
def get_users(message):
    global chat_id
    chat_id = 0
    bot.send_message(message.chat.id,'Ввести имя:')
    bot.register_next_step_handler(message, get_name)
    chat_id = message.chat.id


def get_name(message):
    name = message.text
    database.get_chat_id(chat_id, name)
    bot.send_message(message.chat.id,f'Имя: {name}\nChat_id: {chat_id}')


bot.polling(none_stop=True, interval=0)
