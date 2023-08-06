import os
import telebot

API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands= ['Greet'])
def greetMe(message):
    bot.reply_to(message, "Jambo! How are you?")

@bot.message_handler(commands = ['Hey'])
def greetMe(message):
    bot.send_message(message, "Hey!")
bot.polling()