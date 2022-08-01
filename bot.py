import requests
from bs4 import BeautifulSoup as b
import random
import telebot

URL = "https://www.anekdot.ru/last/good/"
API_Key = "5403583311:AAG1uPi9a93xhbI4PS2ZAnJQF5EmbEdH_N8"


def parser(url):
    r = requests.get(url)
    soup = b(r.text, "html.parser")
    anekdots = soup.find_all("div", class_="text")
    return [s.text for s in anekdots]


list_of_jokes = parser(URL)
random.shuffle(list_of_jokes)

bot = telebot.TeleBot(API_Key)
@bot.message_handler(commands=["start"])


def hello(message):
    bot.send_message(message.chat.id, "Привет, чтобы посмеяться, нажми любую цифру")


@bot.message_handler(content_types=['text'])
def jokes(message):
    if message.text.lower() in "0123456789":
        bot.send_message(message.chat.id, list_of_jokes[0])
        del list_of_jokes[0]
    else:
        bot.send_message(message.chat.id, 'введите цифру')


bot.polling()
