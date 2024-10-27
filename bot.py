import telebot

# Yahan apna bot token daalein
bot_token = "7272105972:AAFozSILjDYbeiKMm_XHkEEuekRZRf1MjS8"
bot = telebot.TeleBot(bot_token)

# Start command ka response
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Welcome! Main aapka Telegram bot hoon. Aap kuch bhi puch sakte hain!")

# Help command ka response
@bot.message_handler(commands=['help'])
def send_help(message):
    bot.reply_to(message, "Commands:\n/start - Bot ko start karne ke liye\n/help - Madad ke liye")

# Normal text messages ka response
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Aapne ye likha hai: {message.text}")

# Bot ko run karna
bot.polling()
