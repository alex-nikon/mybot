# Создаем лог
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Добавление файла для скрытия паролей и ключей
import settings

# Настройка логирования
logging.basicConfig(filename='bot.log', level=logging.INFO)

# Настройки прокси
PROXY = {'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password': settings.PROXY_PASSWORD}}

# Функция приветствия. Update -  что пришло от Телеграм, context - отдавать команды боту
def greet_user(update, context):
    print('вызван старт')
    print(update)
    # Ответ пользователю
    update.message.reply_text('Привет!')

# Функция по возврату введенного текста
def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)


def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)
    # Добавляем диспетчеру обработчик, который будет реагировать на комнду старт и вызывать функцию приветствия
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('бот запущен')
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()
# Вызов функции
if __name__ == '__main__':
    main()