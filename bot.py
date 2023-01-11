import telebot
import random
import distribution
import json

from distribution import *
from telebot import types
from random import choice

#Токен телеграм-бота
token = "example_token"
bot = telebot.TeleBot(token, threaded=False)

# Cloud Function Handler
def handler(event,context):
    body = json.loads(event['body'])
    update = telebot.types.Update.de_json(body)
    bot.process_new_updates([update])
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)

item_theme = types.KeyboardButton('Темы')
item_love = types.KeyboardButton('Любовь')
item_faith = types.KeyboardButton('Вера')
item_wisdom = types.KeyboardButton('Мудрость')
item_stupidity = types.KeyboardButton('Глупость')
item_prayer = types.KeyboardButton('Молитва')
item_sin = types.KeyboardButton('Грех')
item_modesty = types.KeyboardButton('Скромность')
item_peace = types.KeyboardButton('Мир')
item_God = types.KeyboardButton('Бог')
item_forgiveness = types.KeyboardButton('Прощение')
item_loyalty = types.KeyboardButton('Верность')
item_pride = types.KeyboardButton('Гордость')
#-------------------------------------------------------------
item_feeling = types.KeyboardButton('Эмоции')
item_abandoned = types.KeyboardButton('Одиночество')
item_funky = types.KeyboardButton('Тревога')
item_alarmed = types.KeyboardButton('Беспокойство')
item_nervous = types.KeyboardButton('Нервность')
item_tired = types.KeyboardButton('Усталость')
item_annoyed = types.KeyboardButton('Раздражение')
item_angry = types.KeyboardButton('Гнев')
item_happy = types.KeyboardButton('Счастье')
item_grateful = types.KeyboardButton('Благодарность')
item_peaceful = types.KeyboardButton('Умиротворение')
item_hoping = types.KeyboardButton('Надежда')
item_jealous = types.KeyboardButton('Ревность')
item_satisfied = types.KeyboardButton('Удовлетворение')
item_exultant = types.KeyboardButton('Ликование')
item_peace = types.KeyboardButton('Мир')

item_back = types.KeyboardButton('Вернуться в главное меню')
item_support = types.KeyboardButton('Техническая поддержка')
item_donation = types.KeyboardButton('Поддержать проект')

#Приветственное сообщение при команде '/start'
@bot.message_handler(commands = ['start'])
def greetings(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    markup.add(item_theme)
    markup.add(item_feeling)
    markup.add(item_support)#, item_donation)
    bot.send_message(message.chat.id, 'Привет, рад видеть тебя!)\nЯ могу отправить тебе текст из Библии, надеюсь он ободрит тебя и вдохновит)\nВыберите тему или эмоцию\n\n/info - информация о боте\n/support - техническая поддержка бота', reply_markup=markup )



#Основные кнопки(реплай)
@bot.message_handler(content_types = ['text', 'photo'])
def messagelist(message):
    if message.text == 'Темы':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(item_peace, item_wisdom)
        markup.add(item_faith, item_stupidity)
        markup.add(item_prayer, item_modesty)
        markup.add(item_sin, item_love)
        markup.add(item_God, item_loyalty)
        markup.add(item_forgiveness, item_pride)
        markup.add(item_back)
        bot.send_message(message.chat.id, text = 'Выберите тему', reply_markup = markup)
    elif message.text == 'Эмоции':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add (item_abandoned, item_happy)
        markup.add (item_alarmed,  item_grateful,)
        markup.add(item_nervous, item_peaceful)
        markup.add(item_angry, item_hoping)
        markup.add(item_funky, item_jealous)
        markup.add(item_tired, item_satisfied)
        markup.add(item_annoyed, item_exultant)
        markup.add (item_back)
        bot.send_message(message.chat.id, text = 'Опишите свои чувства', reply_markup=markup)
    elif message.text == 'Любовь':
        markup_inline = types.InlineKeyboardMarkup()
        item_love_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_love')
        markup_inline.add(item_love_more)
        bot.send_message(message.chat.id, text = '\n'.join(love[0:4]), reply_markup = markup_inline)
    elif message.text == 'Вера':
        markup_inline = types.InlineKeyboardMarkup()
        item_faith_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_faith')
        markup_inline.add(item_faith_more)
        bot.send_message(message.chat.id, text = '\n'.join(faith[0:4]), reply_markup = markup_inline)
    elif message.text == 'Мудрость':
        markup_inline = types.InlineKeyboardMarkup()
        item_wisdom_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_wisdom')
        markup_inline.add(item_wisdom_more)
        bot.send_message(message.chat.id, text = '\n'.join(wisdom[0:4]), reply_markup = markup_inline)
    elif message.text == 'Молитва':
        markup_inline = types.InlineKeyboardMarkup()
        item_prayer_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_prayer')
        markup_inline.add(item_prayer_more)
        bot.send_message(message.chat.id, text = '\n'.join(prayer[0:4]), reply_markup = markup_inline)
    elif message.text == 'Грех':
        markup_inline = types.InlineKeyboardMarkup()
        item_sin_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_sin')
        markup_inline.add(item_sin_more)
        bot.send_message(message.chat.id, text = '\n'.join(sin[0:4]), reply_markup = markup_inline)
    elif message.text == 'Глупость':
        markup_inline = types.InlineKeyboardMarkup()
        item_stupidity_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_stupidity')
        markup_inline.add(item_stupidity_more)
        bot.send_message(message.chat.id, text = '\n'.join(stupidity[0:4]), reply_markup = markup_inline)
    elif message.text == 'Скромность':
        markup_inline = types.InlineKeyboardMarkup()
        item_modesty_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_modesty')
        markup_inline.add(item_modesty_more)
        bot.send_message(message.chat.id, text = '\n'.join(modesty[0:4]), reply_markup = markup_inline) 
    elif message.text == 'Мир':
        markup_inline = types.InlineKeyboardMarkup()
        item_peace_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_peace')
        markup_inline.add(item_peace_more)
        bot.send_message(message.chat.id, text = '\n'.join(peace[0:4]), reply_markup = markup_inline)
    elif message.text == 'Бог':
        markup_inline = types.InlineKeyboardMarkup()
        item_God_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_God')
        markup_inline.add(item_God_more)
        bot.send_message(message.chat.id, text = '\n'.join(God[0:3]), reply_markup = markup_inline) 
    elif message.text == 'Прощение':
        markup_inline = types.InlineKeyboardMarkup()
        item_forgiveness_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_forgiveness')
        markup_inline.add(item_forgiveness_more)
        bot.send_message(message.chat.id, text = '\n'.join(forgiveness[0:4]), reply_markup = markup_inline)
    elif message.text == 'Гордость':
        markup_inline = types.InlineKeyboardMarkup()
        item_pride_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_pride')
        markup_inline.add(item_pride_more)
        bot.send_message(message.chat.id, text = '\n'.join(pride[0:4]), reply_markup = markup_inline)
    elif message.text == 'Верность':
        markup_inline = types.InlineKeyboardMarkup()
        item_loyalty_more = types.InlineKeyboardButton(text = 'Еще', callback_data = 'more_info_loyalty')
        markup_inline.add(item_loyalty_more)
        bot.send_message(message.chat.id, text = '\n'.join(loyalty[0:4]), reply_markup = markup_inline)
    elif message.text == 'Одиночество':
        bot.send_message(message.chat.id, random.choice(abandoned))
    elif message.text == 'Тревога':
        bot.send_message(message.chat.id, random.choice(funky))
    elif message.text == 'Беспокойство':
        bot.send_message(message.chat.id, random.choice(alarmed))
    elif message.text == 'Нервность':
        bot.send_message(message.chat.id, random.choice(nervous))
    elif message.text == 'Усталость':
        bot.send_message(message.chat.id, random.choice(tired))
    elif message.text == 'Счастье':
        bot.send_message(message.chat.id, random.choice(happy))
    elif message.text == 'Благодарность':
        bot.send_message(message.chat.id, random.choice(grateful))
    elif message.text == 'Раздражение':
        bot.send_message(message.chat.id, random.choice(annoyed))
    elif message.text == 'Гнев':
        bot.send_message(message.chat.id, random.choice(angry))
    elif message.text == 'Умиротворение':
        bot.send_message(message.chat.id, random.choice(peaceful))
    elif message.text == 'Ревность':
        bot.send_message(message.chat.id, random.choice(jealous))
    elif message.text == 'Надежда':
        bot.send_message(message.chat.id, random.choice(hoping))
    elif message.text == 'Удовлетворение':
        bot.send_message(message.chat.id, random.choice(satisfied))
    elif message.text == 'Ликование':
        bot.send_message(message.chat.id, random.choice(exultant))
    elif message.text == 'Вернуться в главное меню':
        markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
        markup.add(item_theme)
        markup.add(item_feeling)
        markup.add(item_support)#, item_donation)
        bot.send_message(message.chat.id, text = 'Ты вернулся в главное меню\n\nСнова можешь выбрать тему или эмоцию', reply_markup=markup)
    elif message.text == 'Поддержать проект':
        bot.send_message(message.chat.id, text = 'Здесь будут реквизиты для денежной поддержки проекта')
    elif message.text == '/support' or message.text == 'Техническая поддержка':
        markup_inline = types.InlineKeyboardMarkup()
        item_support_inline = types.InlineKeyboardButton("Техподдержка", url='https://t.me/bible_support')
        markup_inline.add(item_support_inline)
        bot.send_message(message.chat.id, text = 'Нажми для перехода в техподдержку. Сюда ты можешь написать свои предложения или задать вопросы о работе бота', reply_markup = markup_inline)
    elif message.text == '/info':
        bot.send_message(message.chat.id, text = 'Этот бот умеет присылать отрывки на разные темы из Библии или опираясь на твое настроение)')
    else:
        bot.send_message(message.chat.id, text = "Этого я ещё не умею, но в будущем все возможно\n/support - Здесь ты можешь задать любые вопросы или оставить свои предложения")


#Кнопки ответа(инлайн)
@bot.callback_query_handler(func = lambda call: True)
def answer(call):
    if call.data == 'more_info_love':
        markup_inline = types.InlineKeyboardMarkup()
        item_love_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_love')
        markup_inline.add(item_love_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(love[4:8]), reply_markup = markup_inline)

    #if call.data == 'more_info_love' or call.data == 'back_back_info_love':
        #markup_inline = types.InlineKeyboardMarkup()
        #item_love_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_love')
        #markup_inline.add(item_love_more_more)
        #bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text = '\n'.join(love[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_love':
        bot.send_message(call.message.chat.id, text = '\n'.join(love[8:(len(love))]))

    #elif call.data == 'more_more_info_love':
       #markup_inline = types.InlineKeyboardMarkup()
        #item_love_back_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'back_back_info_love')
        #markup_inline.add(item_love_back_back)
        #bot.edit.message_text(call_id=call.message.chat.id, message_id = call.message.message_id, text = '\n'.join(love[8:(len(love))]), reply_markup = markup_inline)
        #markup_inline = types.InlineKeyboardButton()
        #item_love_back_back = types.InlineKeyboardButton(text = 'Назад', callback_data = 'back_back_info_love')
        #markup_inline.add(item_love_back_back)
        #bot.send_message(call.message.chat.id, text = '\n'.join(love[8:(len(love))]), reply_markup = markup_inline)
    elif call.data == 'more_info_faith':
        markup_inline = types.InlineKeyboardMarkup()
        item_faith_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_faith')
        markup_inline.add(item_faith_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(faith[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_faith':
        bot.send_message(call.message.chat.id, text = '\n'.join(faith[8:(len(faith))]))
    elif call.data == 'more_info_wisdom':
        markup_inline = types.InlineKeyboardMarkup()
        item_wisdom_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_wisdom')
        markup_inline.add(item_wisdom_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(wisdom[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_wisdom':
        bot.send_message(call.message.chat.id, text = '\n'.join(wisdom[8:(len(wisdom))])) 
    elif call.data == 'more_info_prayer':
        markup_inline = types.InlineKeyboardMarkup()
        item_prayer_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_prayer')
        markup_inline.add(item_prayer_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(prayer[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_prayer':
        bot.send_message(call.message.chat.id, text = '\n'.join(prayer[8:(len(prayer))]))
    elif call.data == 'more_info_sin':
        markup_inline = types.InlineKeyboardMarkup()
        item_sin_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_sin')
        markup_inline.add(item_sin_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(sin[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_sin':
        bot.send_message(call.message.chat.id, text = '\n'.join(sin[8:(len(sin))]))
    elif call.data == 'more_info_stupidity':
        markup_inline = types.InlineKeyboardMarkup()
        item_stupidity_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_stupidity')
        markup_inline.add(item_stupidity_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(stupidity[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_stupidity':
        bot.send_message(call.message.chat.id, text = '\n'.join(stupidity[8:(len(stupidity))]))
    elif call.data == 'more_info_modesty':
        markup_inline = types.InlineKeyboardMarkup()
        item_modesty_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_modesty')
        markup_inline.add(item_modesty_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(modesty[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_modesty':
        bot.send_message(call.message.chat.id, text = '\n'.join(modesty[8:(len(modesty))]))
    elif call.data == 'more_info_peace':
        markup_inline = types.InlineKeyboardMarkup()
        item_peace_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_peace')
        markup_inline.add(item_peace_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(peace[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_peace':
        bot.send_message(call.message.chat.id, text = '\n'.join(peace[8:(len(peace))]))
    elif call.data == 'more_info_God':
        markup_inline = types.InlineKeyboardMarkup()
        item_God_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_God')
        markup_inline.add(item_God_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(God[3:9]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_God':
        bot.send_message(call.message.chat.id, text = '\n'.join(God[9:(len(God))])) 
    elif call.data == 'more_info_forgiveness':
        markup_inline = types.InlineKeyboardMarkup()
        item_forgiveness_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_forgiveness')
        markup_inline.add(item_forgiveness_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(forgiveness[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_forgiveness':
        bot.send_message(call.message.chat.id, text = '\n'.join(forgiveness[8:(len(forgiveness))])) 
    elif call.data == 'more_info_loyalty':
        markup_inline = types.InlineKeyboardMarkup()
        item_loyalty_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_loyalty')
        markup_inline.add(item_loyalty_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(loyalty[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_loyalty':
        bot.send_message(call.message.chat.id, text = '\n'.join(loyalty[8:(len(loyalty))]))
    elif call.data == 'more_info_pride':
        markup_inline = types.InlineKeyboardMarkup()
        item_pride_more_more = types.InlineKeyboardButton(text = 'Еще больше', callback_data = 'more_more_info_pride')
        markup_inline.add(item_pride_more_more)
        bot.send_message(call.message.chat.id, text = '\n'.join(pride[4:8]), reply_markup = markup_inline)
    elif call.data == 'more_more_info_pride':
        bot.send_message(call.message.chat.id, text = '\n'.join(pride[8:(len(pride))]))
