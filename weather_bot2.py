import pyowm
import telebot

owm = pyowm.OWM('58e7f93e74e24c88a096481301bf4c51')
mgr = owm.weather_manager()
bot = telebot.TeleBot("5400543143:AAEDyyQmuCuGjLNg9Bq0z4kj_-2eZbuytRQ", parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place( message.text )
    w = observation.weather
    temp = w.temperature('celsius')['temp']

    answer = "In the city " + message.text + " now is " + w.detailed_status + "\n"
    answer += "Temperature now is about " + str(temp) + " celsius" + "\n\n"

    if temp < 10:
        answer += "Now it`s too cold, wear the warm clothes!"
    elif temp < 20:
        answer += "It`s cold, don`t forget the scarf :) "
    else:
        answer += "So good outside :) "
    bot.send_message(message.chat.id, answer)

bot.infinity_polling( none_stop = True )