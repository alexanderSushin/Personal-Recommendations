import telebot

TOKEN = open('token.txt', 'r').read()
bot = telebot.telebot(TOKEN=TOKEN)

if __name__ == "__main__":
	bot.infinity_polling()
