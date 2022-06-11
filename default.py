import telebot
import time

bot = telebot.TeleBot('5111638907:AAFA0tQ10eHJFngD5bvdM3umUc7B4J2hAP8')


def icon(count):
    output = "00000\n" * count
    return output


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        print("Message received")
        msg = bot.send_message(message.chat.id, "Hello")
        time.sleep(0.1)


bot.polling(none_stop=True, interval=0)
