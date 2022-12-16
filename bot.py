import telebot

TOKEN = open('token.txt', 'r').read()
if TOKEN[-1] == '\n':
	TOKEN = TOKEN[:-1]
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=["start"])
def start (msg):
	bot.send_message(msg.chat.id, 'Привет, это стартовое сообщение *редачится*')

if __name__ == "__main__":
	bot.infinity_polling()