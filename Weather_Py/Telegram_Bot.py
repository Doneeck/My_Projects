import telebot
from pyowm import OWM

bot = telebot.TeleBot("1193919433:AAH6l9-X9k22Q-TiNKHUkaJ6Ly3FtJIjWEM")
owm = OWM('08ad8dd304a83c052977dc6431e6f10e')
mgr = owm.weather_manager()
text = open("text.txt", "a")


@bot.message_handler(content_types=['text'])
def send_weather(message):
    try:
        observation = mgr.weather_at_place(message.text)
        text.write(message.text)
    except:
        bot.send_message(message.chat.id, "This city/country not found, try again!")
    else:
        w = observation.weather
        sky_status = w.status
        temp = w.temperature('celsius')["temp"]
        answer = "Sky In " + message.text + " " + sky_status + " and temperature is " + str(temp) + "° now" + "\n"
        prediction = ""
        if temp > 30:
            prediction = "You can go out in shorts and T-shirt, weather is hot"
        elif 30 > temp > 20:
            prediction = "Wear anything, weather is warm"
        elif 20 > temp > 10:
            prediction = "Wear warmer clothes, weather is cool"
        elif -5 >= temp > 10:
            prediction = "Wear very warm clothes, weather is frost"
        elif temp < -6:
            prediction += "Bro where are you? In Alaska?"
        bot.send_message(message.chat.id, answer)
        bot.send_message(message.chat.id, prediction)


bot.polling(none_stop=True)
