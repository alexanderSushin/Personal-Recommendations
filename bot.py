import telebot

def readFileUtf8(name):
	file = open(name, 'rb')
	res = file.read().decode('utf8')
	file.close()
	if res[-1] == '\n':
		res = res[:-1]
		print('ok')
	return res

def readFile(name):
	file = open(name, 'r')
	res = file.read()
	file.close()
	if res[-1] == '\n':
		res = res[:-1]
		print('ok')
	return res

TOKEN = readFile('token.txt')
print(TOKEN)
bot = telebot.TeleBot(TOKEN, parse_mode=None)
funcIsNotWorking = 'Сейчас эта функция недоступна'

@bot.message_handler(commands=["start"])
def start (msg):
	bot.send_message(msg.chat.id, readFileUtf8('texts/start.txt'))

@bot.message_handler(commands=["help"])
def help (msg):
	bot.send_message(msg.chat.id, readFileUtf8('texts/help.txt'))

@bot.message_handler(commands=["random"])
def randomAnime (msg):
	bot.send_message(msg.chat.id, funcIsNotWorking)

@bot.message_handler(commands=["top_alltime", "top_month", "top_week"])
def getTopForAll (msg):
	timeGot = msg.text
	bot.send_message(msg.chat.id, f'Данная функция сейчас недоступна, вы выбрали {timeGot}')

@bot.message_handler(commands=["personal"])
def getPersonalAnime (msg):
	bot.send_message(msg.chat.id, funcIsNotWorking)

@bot.message_handler(commands=["add_friend"])
def addFriend (msg):
	bot.send_message(msg.chat.id, funcIsNotWorking)

@bot.message_handler(commands=["top_friend"])
def removeFriend (msg):
	bot.send_message(msg.chat.id, funcIsNotWorking)

@bot.message_handler(commands=["watched"])
def watchedAnime (msg):
	bot.send_message(msg.chat.id, funcIsNotWorking)

if __name__ == "__main__":
	bot.infinity_polling()