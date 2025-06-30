import telebot
bot = telebot.TeleBot("8125997574:AAEJEbydft8APtEA03MRqo_bSK3FpiKKAgA")

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "Привіт! Я DeutschNinjaBot 🤖")

bot.polling()
