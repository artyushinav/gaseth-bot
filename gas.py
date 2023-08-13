import requests
from bs4 import BeautifulSoup
import telebot
from telebot import types

#токен бота
bot = telebot.TeleBot('6201830922:AAETvNm4onehtfZCnJHCK6XvFlaFeEDrkoU')

#функция по определению газа
def gass():
    url = "https://coinmarketcap.com/ru/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "lxml")
    data = soup.find("div", class_="sc-16891c57-0 kIbwws glo-stat-item")
    price = data.find("a", class_="sc-16891c57-0 OKpOL base-text").text
    return price

#узнаем цену газа через start
@bot.message_handler(commands=['start'])
def start(message):
        bot.send_message(message.chat.id, gass())

#узнаем цену газа через меню
@bot.message_handler(commands=['gas'])
def gas(message):
    bot.send_message(message.chat.id, gass())

#непрерывная работа
bot.polling(none_stop=True)