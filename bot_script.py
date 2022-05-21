import telebot
from telebot import types
from excel_script import read_timetable
import settings
from groups import groups
"""
You must create settings.py with 
token = 'your token'
admins = [telegram_user_id: int]
"""
token = settings.token

bot = telebot.TeleBot(token)


def send_long_text(timetable: str, message):
    """Send second message if len more than 4096 because of Telegram limit symbols"""
    if len(timetable) > 4096:
        bot.send_message(message.chat.id, timetable[4096:].format(message.from_user))


def telegram_bot():
    """Send weekly schedule"""
    @bot.message_handler(commands=['start'])
    def start(message):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        select_group_do = types.KeyboardButton('ДО')
        select_group_isip = types.KeyboardButton('ИСиП')
        select_group_at = types.KeyboardButton('АТ')
        select_group_kp = types.KeyboardButton('КП')
        select_group_ibas = types.KeyboardButton('ИБАС')
        select_group_osatpip = types.KeyboardButton('ОСАТПиП')
        select_group_ssa = types.KeyboardButton('ССА')
        select_group_pdott = types.KeyboardButton('ПДО ТТ')

        markup.add(select_group_do, select_group_isip, select_group_at, select_group_kp, select_group_ibas,
                   select_group_osatpip, select_group_ssa, select_group_pdott)
        bot.send_message(message.chat.id, 'Выбери специальность'.format(message.from_user), reply_markup=markup)

    @bot.message_handler(content_types=['text'])
    def bot_message(message):
        if message.text == 'Назад к специальностям ➪':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_do = types.KeyboardButton('ДО')
            select_group_isip = types.KeyboardButton('ИСиП')
            select_group_at = types.KeyboardButton('АТ')
            select_group_kp = types.KeyboardButton('КП')
            select_group_ibas = types.KeyboardButton('ИБАС')
            select_group_osatpip = types.KeyboardButton('ОСАТПиП')
            select_group_ssa = types.KeyboardButton('ССА')
            select_group_pdott = types.KeyboardButton('ПДО ТТ')
            markup.add(select_group_do, select_group_isip, select_group_at, select_group_kp, select_group_ibas,
                       select_group_osatpip, select_group_ssa, select_group_pdott)
            bot.send_message(message.chat.id, 'Выбери специальность'.format(message.from_user), reply_markup=markup)

        # ------------ИСИП------------
        elif message.text == 'ИСиП':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_isip19111 = types.KeyboardButton('ИСиП 19-11-1')
            select_group_isip19112 = types.KeyboardButton('ИСиП 19-11-2')

            select_group_isip20111 = types.KeyboardButton('ИСиП 20-11-1')
            select_group_isip20112 = types.KeyboardButton('ИСиП 20-11-2')
            select_group_isip20113 = types.KeyboardButton('ИСиП 20-11-3')

            select_group_isip21111 = types.KeyboardButton('ИСиП 21-11-1')
            select_group_isip21112 = types.KeyboardButton('ИСиП 21-11-2')
            select_group_isip21113 = types.KeyboardButton('ИСиП 21-11-3')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.row(select_group_isip19111, select_group_isip19112)
            markup.add(select_group_isip20111, select_group_isip20112, select_group_isip20113, select_group_isip21111,
                       select_group_isip21112, select_group_isip21113, special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------ДО------------
        elif message.text == 'ДО':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_do19111 = types.KeyboardButton('ДО 19-11-1')
            select_group_do19112 = types.KeyboardButton('ДО 19-11-2')

            select_group_do20111 = types.KeyboardButton('ДО 20-11-1')
            select_group_do20112 = types.KeyboardButton('ДО 20-11-2')

            select_group_do21111 = types.KeyboardButton('ДО 21-11-1')
            select_group_do21112 = types.KeyboardButton('ДО 21-11-2')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_do19111, select_group_do19112, select_group_do20111, select_group_do20112,
                       select_group_do21111, select_group_do21112)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------ИБАС------------
        elif message.text == 'ИБАС':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_ibas2111 = types.KeyboardButton('ИБАС 21-11')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_ibas2111)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------АТ------------
        elif message.text == 'АТ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_at1911 = types.KeyboardButton('АТ 19-11')

            select_group_at2011 = types.KeyboardButton('АТ 20-11')

            select_group_at2111 = types.KeyboardButton('АТ 21-11')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_at1911, select_group_at2011, select_group_at2111)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------КП------------
        elif message.text == 'КП':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_kp19111 = types.KeyboardButton('КП 19-11-1')
            select_group_kp19112 = types.KeyboardButton('КП 19-11-2')
            select_group_kp19113 = types.KeyboardButton('КП 19-11-3')

            select_group_kp20111 = types.KeyboardButton('КП 20-11-1')
            select_group_kp20112 = types.KeyboardButton('КП 20-11-2')
            select_group_kp20113 = types.KeyboardButton('КП 20-11-3')
            select_group_kp20114 = types.KeyboardButton('КП 20-11-4')

            select_group_kp21111 = types.KeyboardButton('КП 21-11-1')
            select_group_kp21112 = types.KeyboardButton('КП 21-11-2')
            select_group_kp21113 = types.KeyboardButton('КП 21-11-3')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_kp19111, select_group_kp19112, select_group_kp19113)
            markup.row(select_group_kp20111, select_group_kp20112, select_group_kp20113, select_group_kp20114, )
            markup.add(select_group_kp21111, select_group_kp21112, select_group_kp21113)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------ОСАТПиП------------
        elif message.text == 'ОСАТПиП':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_osatpip19111 = types.KeyboardButton('ОСАТПиП 19-11-1')
            select_group_osatpip19112 = types.KeyboardButton('ОСАТПиП 19-11-2')

            select_group_osatpip20111 = types.KeyboardButton('ОСАТПиП 20-11-1')
            select_group_osatpip20112 = types.KeyboardButton('ОСАТПиП 20-11-2')

            select_group_osatpip21111 = types.KeyboardButton('ОСАТПиП 21-11')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_osatpip19111, select_group_osatpip19112)
            markup.row(select_group_osatpip20111, select_group_osatpip20112)
            markup.row(select_group_osatpip21111)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------ССА------------
        elif message.text == 'ССА':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_ssa19111 = types.KeyboardButton('ССА 19-11-1')
            select_group_ssa19112 = types.KeyboardButton('ССА 19-11-2')
            select_group_ssa19113 = types.KeyboardButton('ССА 19-11-3')

            select_group_ssa20111 = types.KeyboardButton('ССА 20-11-1')
            select_group_ssa20112 = types.KeyboardButton('ССА 20-11-2')
            select_group_ssa20113 = types.KeyboardButton('ССА 20-11-3')

            select_group_ssa21111 = types.KeyboardButton('ССА 21-11-1')
            select_group_ssa21112 = types.KeyboardButton('ССА 21-11-2')
            select_group_ssa21113 = types.KeyboardButton('ССА 21-11-3')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_ssa19111, select_group_ssa19112, select_group_ssa19113, select_group_ssa20111,
                       select_group_ssa20112, select_group_ssa20113, select_group_ssa21111, select_group_ssa21112,
                       select_group_ssa21113)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        # ------------ПДО ТТ------------
        elif message.text == 'ПДО ТТ':
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

            select_group_pdott19111 = types.KeyboardButton('ПДО ТТ 19-11')
            select_group_pdott19112 = types.KeyboardButton('ПДО ТТ 20-11')
            select_group_pdott20111 = types.KeyboardButton('ПДО ТТ 21-11')

            special_back = types.KeyboardButton('Назад к специальностям ➪')

            markup.add(select_group_pdott19111, select_group_pdott19112, select_group_pdott20111)
            markup.row(special_back)
            bot.send_message(message.chat.id, 'Выбери свою группу'.format(message.from_user), reply_markup=markup)

        elif message.text == 'ПДО ТТ 19-11':
            timetable = read_timetable('Groups/PDOTT/PDOTT19-11')
            bot.send_message(message.chat.id, timetable[:4096].format(message.from_user))
            send_long_text(timetable, message)

        elif message.text == 'ПДО ТТ 20-11':
            timetable = read_timetable('Groups/PDOTT/PDOTT20-11')
            bot.send_message(message.chat.id, timetable[:4096].format(message.from_user))
            send_long_text(timetable, message)

        elif message.text == 'ПДО ТТ 21-11':
            timetable = read_timetable('Groups/PDOTT/PDOTT21-11')
            bot.send_message(message.chat.id, timetable[:4096].format(message.from_user))
            send_long_text(timetable, message)
        else:
            timetable_file = groups.get(message.text, 'Нет такого варианта ответа')
            if timetable_file != 'Нет такого варианта ответа':
                timetable = read_timetable(timetable_file)
                bot.send_message(message.chat.id, timetable[:4096].format(message.from_user))
                send_long_text(timetable, message)
            else:
                bot.send_message(message.chat.id, timetable_file.format(message.from_user))
    bot.polling(none_stop=True)


telegram_bot()
