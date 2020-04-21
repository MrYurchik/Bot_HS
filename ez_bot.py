import time

from scrape import y, z, deck_code
import telebot
from telebot import types
start_time = time.time()

bot = telebot.TeleBot("")


#.format( message.from_user, bot.get_me()

msg_ids = []


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):

    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("🎲 Топ 5 архетипов")
    item2 = types.KeyboardButton("😊 ДАРОУ")

    markup.add(item1, item2)
    msg = bot.send_message(message.chat.id,
                     "Добро пожаловать, тут вы можете посмотреть топ колод по версии HSREPLAY", reply_markup=markup)
    msg_ids.append(msg.message_id)


@bot.message_handler(content_types=['text'])
def lalala(message):

    if message.chat.type == 'private':
        if message.text == '🎲 Топ 5 архетипов':
            msg_ids.append(message.message_id)
            for i in range(5):

                keyboard = types.InlineKeyboardMarkup()
                callback_button = types.InlineKeyboardButton(text="ПОСМОТРЕТЬ КОЛОДУ", callback_data="test"+str(i))
                keyboard.add(callback_button)
                text = '{0}----><b>{1}</b>\n <a href="{2}">Ссылка на колоду</a>'.format(y[i][0], y[i][1], y[i][2])
                msg = bot.send_message(message.chat.id, text, parse_mode='html', reply_markup=keyboard)
                #msg = bot.send_message(message.chat.id, "---->".join(y[i]), reply_markup=keyboard)
                msg_ids.append(msg.message_id)

                # bot.send_message(message.chat.id, "---->".join(first_five[i]))

        elif message.text == '😊 ДАРОУ':

            mas = bot.send_message(message.chat.id, "ДАроу)))")
            msg_ids.append(message.message_id)
            msg_ids.append(mas.message_id)
            print(msg_ids)
            for i in range(len(msg_ids)):
                bot.delete_message(chat_id=message.chat.id, message_id=msg_ids[i])
            print(len(msg_ids))
            for i in range(len(msg_ids)):
                msg_ids.pop()
            print(len(msg_ids))
            print(msg_ids)
            # markup = types.InlineKeyboardMarkup(row_width=2)
            # item1 = types.InlineKeyboardButton("Хорошо", callback_data='good')
            # item2 = types.InlineKeyboardButton("Не очень", callback_data='bad')
            #
            # markup.add(item1, item2)
            #
            # bot.send_message(message.chat.id, 'Отлично, сам как?', reply_markup=markup)
        else:
            mas = bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
            msg_ids.append(message.message_id)
            msg_ids.append(mas.message_id)

        # print(msg_ids)


@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    chat_id = call.message.chat.id

    # Если сообщение из чата с ботом
    # for i in range(len(msg_id)):

    for i in range(5):
        if call.data == "test"+str(i):

            mas = bot.send_photo(chat_id=chat_id, photo=open('images/{}.jpg'.format(i), 'rb'))
            msg_ids.append(mas.message_id)
            mas = bot.send_message(chat_id, text="`{}`".format(deck_code[i]), parse_mode='markdown')
            msg_ids.append(mas.message_id)



print("My program took", time.time() - start_time, "to run")

if __name__ == '__main__':
    bot.polling(none_stop=True)