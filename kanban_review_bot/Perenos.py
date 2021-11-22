# import telebot
# from telebot import types
# import sqlite3
# import database
# from datetime import datetime
#
#
# token = '2088217444:AAEwq4TpDJ0m5rGAVAoeDkSO174ao4MnxKc'
#
#
# bot = telebot.TeleBot(token)
#
# class Perenos():
#
# @bot.message_handler(commands=['start'])
# def start(message):
#     global user_name
#     user_name = database.get_user_name(message.chat.id)
#     markup=types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
#     item1=types.KeyboardButton("Перенос")
#     item2 = types.KeyboardButton("Блокер")
#     markup.add(item1)
#     markup.add(item2)
#     bot.send_message(message.chat.id,f'Привет, {user_name}\nChoose:',reply_markup=markup)
#     bot.register_next_step_handler(message, get_type_of_sticker)
#
# def get_type_of_sticker(message):
#     global type_of_sticker
#     if message.text == 'Перенос':
#
#         type_of_sticker = 'Перенос'
#
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
#         cause_1 = types.KeyboardButton("Defocus")
#         cause_2 = types.KeyboardButton("Decomposition")
#         cause_3 = types.KeyboardButton("Nuance")
#         cause_4 = types.KeyboardButton("Tired")
#         markup.add(cause_1, cause_2, cause_3, cause_4)
#         bot.send_message(message.chat.id, 'Cause:', reply_markup=markup)
#
#         bot.register_next_step_handler(message, get_cause)
#
#     # elif message.text == 'Блокер':
#     #
#     #     type_of_sticker = 'Блокер'
#     #
#     #     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     #     for name_ in names:
#     #         markup.add(types.KeyboardButton(f'{name_}'))
#     #     bot.send_message(message.chat.id, 'Your name :', reply_markup=markup)
#
#
# def get_cause(message):
#     global defocus
#     global decompos
#     global nuance
#     global tired
#
#     defocus = 0
#     decompos = 0
#     nuance = 0
#     tired = 0
#
#
#     keyboard = types.InlineKeyboardMarkup()
#     key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')  # кнопка «Да»
#     keyboard.add(key_yes)  # добавляем кнопку в клавиатуру
#     key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
#     keyboard.add(key_no)
#
#     if message.text == 'Defocus':
#         defocus = 1
#         question = f'Имя: {user_name}\nПричина переноса задачи: Расфокус\nДата: {date}'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#     elif message.text == 'Decomposition':
#         decompos = 1
#         question = f'Имя: {user_name}\nПричина переноса задачи: Плохая декомпозиция\nДата: {date}'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#     elif message.text == 'Nuance':
#         nuance = 1
#         question = f'Имя: {user_name}\nПричина переноса задачи: Нюансы\nДата: {date}'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#     elif message.text == 'Tired':
#         tired = 1
#         question = f'Имя: {user_name}\nПричина переноса задачи: Устал\nДата: {date}'
#         bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)
#
#
# @bot.callback_query_handler(func=lambda call: True)
# def callback_worker(call):
#     if call.data == "yes": #call.data это callback_data, которую мы указали при объявлении кнопки
#         database.insert_cause(user_name, defocus, decompos, nuance, tired ,date)
#         bot.send_message(call.message.chat.id, 'Запомню : )')
#     elif call.data == "no":
#         markup = types.ReplyKeyboardMarkup(resize_keyboard=True,one_time_keyboard=True)
#         markup.add(types.KeyboardButton('/start'))
#         bot.send_message(call.message.chat.id, 'Заполни заново, нажми на /start:', reply_markup=markup)
