import telebot
from telebot import types
import time
from heart import frame
from anim import people
from anim import skull
bot = telebot.TeleBot('TG_BOT_TOKEN')


@bot.message_handler(commands=["start"])
def inline(message):
    print("has started")
    key = types.InlineKeyboardMarkup()
    but_1 = types.InlineKeyboardButton(text="Love❤️", callback_data="Love")
    but_2 = types.InlineKeyboardButton(text="OR", callback_data="OR")
    but_3 = types.InlineKeyboardButton(text="Death☠", callback_data="Death")
    key.add(but_1, but_2, but_3)
    bot.send_message(message.chat.id, "Love or Death?", reply_markup=key)


@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == 'Love':
        print("love")
        msg = bot.send_message(c.message.chat.id, "i love you")
        time.sleep(0.03)
        txt = ""
        for y in range(13):
            txt = txt + "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=txt)
            time.sleep(0.463)
            txt = txt + "\n"
        time.sleep(0.063)
        for count in range(len(people)):
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=people[count])
            time.sleep(0.068)
        time.sleep(0.09)
        for count in range(len(frame)):
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=frame[count])
            time.sleep(0.068)
        # bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=frame[-1])

    if c.data == 'Death':
        print("death")
        msg = bot.send_message(c.message.chat.id, "Oooops...")
        time.sleep(0.03)
        txt = ""
        for y in range(13):
            txt = txt + "⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪⚪"
            bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=txt)
            time.sleep(0.463)
            txt = txt + "\n"
        bot.edit_message_text(chat_id=c.message.chat.id, message_id=msg.message_id, text=skull[0])


    # if c.data == 'NumberTree':
    #     key = types.InlineKeyboardMarkup()
    #     but_1 = types.InlineKeyboardButton(text="NumberOne", callback_data="NumberOne")
    #     but_2 = types.InlineKeyboardButton(text="NumberTwo", callback_data="NumberTwo")
    #     but_3 = types.InlineKeyboardButton(text="NumberTree", callback_data="NumberTree")
    #     key.add(but_1, but_2, but_3)
    #     bot.send_message(c.message.chat.id, 'Это кнопка 3', reply_markup=key)


bot.polling(none_stop=True, interval=0)
