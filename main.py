import telebot
import psutil

# Инициализация бота
TOKEN = "8154789926:AAFf8xRcgANcXBmJOBStrFHrRelvyxXSAEY"
bot = telebot.TeleBot(TOKEN)

# Команда /start
@bot.message_handler(commands=["start"])
def start_handler(message):
    bot.reply_to(message, "Привет! Используй команду /status, чтобы узнать состояние системы.")

# Команда /status
@bot.message_handler(commands=["status"])
def status_handler(message):
    # Получение данных о системе
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    total_memory = memory_info.total // (1024 ** 2)  # Перевод в МБ
    available_memory = memory_info.available // (1024 ** 2)  # Перевод в МБ
    used_memory = memory_info.used // (1024 ** 2)  # Перевод в МБ

    # Формирование сообщения
    status_message = (
        f"📊 Состояние системы:\n"
        f"🔹 Загрузка CPU: {cpu_usage}%\n"
        f"🔹 Память:\n"
        f"   Общая: {total_memory} МБ\n"
        f"   Используется: {used_memory} МБ\n"
        f"   Доступно: {available_memory} МБ"
    )

    bot.reply_to(message, status_message)

# Запуск бота
if __name__ == "__main__":
    bot.polling(none_stop=True)