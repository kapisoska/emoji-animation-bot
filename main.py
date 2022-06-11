import telebot
from telebot import types
import time
from frames import frame
from anim import people
bot = telebot.TeleBot('5111638907:AAFA0tQ10eHJFngD5bvdM3umUc7B4J2hAP8')


def icon(count):
    output = "00000\n" * count
    return output


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "/start":
        msg = bot.send_message(message.chat.id, "hi")
        time.sleep(0.03)
        txt = ""
        for y in range(13):
            txt = txt + "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=txt)
            time.sleep(0.043)
            txt = txt + "\n"
        time.sleep(0.043)
        for count in range(len(people)):
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=people[count])
            time.sleep(0.048)
        time.sleep(0.09)
        for count in range(len(frame)):
            bot.edit_message_text(chat_id=message.chat.id, message_id=msg.message_id, text=frame[count])
            time.sleep(0.048)

@bot.message_handler(commands="random")
async def cmd_random(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(types.InlineKeyboardButton(text="Нажми меня", callback_data="random_value"))
    await message.answer("Нажмите на кнопку, чтобы бот отправил число от 1 до 10", reply_markup=keyboard)

bot.polling(none_stop=True, interval=0)













