import telebot
import constants
from getweather import search_temperature
import database
from flask import Flask, request
import os
server = Flask(__name__)


bot = telebot.TeleBot(constants.TOKEN_NAME)


@bot.message_handler(commands=["start"])
def introduction(message):
    bot.send_message(message.chat.id, "Добро пожаловать в погодного Бота, напишите /help для списка доступных команд")


@bot.message_handler(commands=["help"])
def explain(message):
    bot.send_message(message.chat.id, "Для получения необходимой температуры вам достаточно написать название города ")


@bot.message_handler(content_types=["text"])
def post_temperature(message):
    bot.send_message(message.chat.id, search_temperature(message.text))
    database.addtodb(message.text)


@server.route('/' + constants.TOKEN_NAME, methods=['POST'])
def getMessage():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    return "!", 200


@server.route("/")
def webhook():
    bot.remove_webhook()
    bot.set_webhook(url='https://telegobot.herokuapp.com/' + constants.TOKEN_NAME)
    return "!", 200


if __name__ == "__main__":
    server.run(host="0.0.0.0", port=int(os.environ.get('PORT', 5000)))
