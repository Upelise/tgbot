import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext

# Включаем логирование
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Определяем команду /start
def start(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Привет! Я ваш Telegram-бот. Как я могу помочь?')

# Определяем команду /help
def help_command(update: Update, context: CallbackContext) -> None:
    update.message.reply_text('Команды:\n/start - Приветственное сообщение
/help - Список доступных команд')

# Основная функция для запуска бота
def main() -> None:
    # Замените 'YOUR_TOKEN_HERE' на ваш токен, который вы получили от @BotFather
    updater = Updater("YOUR_TOKEN_HERE")

    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher

    # Находим команды
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # Запускаем бота
    updater.start_polling()

    # Бот будет работать до тех пор, пока не будет прерван (например, Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
