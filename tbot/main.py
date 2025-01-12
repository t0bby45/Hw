import telebot  # Импортируем библиотеку telebot

API_TOKEN = '7510098776:AAGYszBkpoYgm-4mGbcYblgbRMGSSWbg_mY'  # Укажите токен вашего бота

# Создаем объект бота
bot = telebot.TeleBot(API_TOKEN)

# Храним состояние диалога
user_state = {}

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_state[message.chat.id] = "asking_name"
    bot.reply_to(message, "Привет! Как тебя зовут?")  # Бот начинает диалог

# Обработчик текстовых сообщений
@bot.message_handler(func=lambda message: True)
def handle_dialog(message):
    chat_id = message.chat.id

    if chat_id not in user_state:
        user_state[chat_id] = "asking_name"

    state = user_state[chat_id]

    if state == "asking_name":
        bot.reply_to(message, f"Приятно познакомиться, {message.text}! Сколько тебе лет?")
        user_state[chat_id] = "asking_age"
    elif state == "asking_age":
        bot.reply_to(message, f"Круто! Тебе {message.text} лет? А печенье любишь?")
        user_state[chat_id] = "asking_cookies"
    elif state == "asking_cookies":
        if "да" in message.text.lower():
            bot.reply_to(message, "Я тоже люблю печенье! Спасибо за разговор! 😊")
        else:
            bot.reply_to(message, "Жаль, что ты не любишь печенье! Спасибо за разговор! 😊")
        user_state.pop(chat_id)  # Удаляем состояние, диалог окончен
    else:
        bot.reply_to(message, "Начни с команды /start, чтобы поговорить заново!")

# Запуск бота
bot.polling()
