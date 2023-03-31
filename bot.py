import telebot
import requests
api_key = ""
bot_token = ""
bot = telebot.TeleBot(bot_token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,"Привіт, яку Гіфку знайти? Напиши будь-яке слово: cats,dogs,etc... ")
@bot.message_handler(content_types=['text'])
def search_gif(message):
    search_term = message.text
    endpoint = f"http://api.giphy.com/v1/gifs/search?api_key={api_key}&q={search_term}&limit=10"
    response = requests.get(endpoint)
    data = response.json()
    for gif in data["data"]:
        bot.send_message(message.chat.id, gif["url"])
bot.infinity_polling()
