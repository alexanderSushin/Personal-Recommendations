import telebot
import numpy
from anime_api import getInfoById, root_url, getAnimeList, getTopAllTime
import urllib
import os

cur_cnt = 0

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

def delRectBrackets (s):
	bal = 0
	res = ''
	for i in s:
		if i == '[' or i == '(' or i == '{':
			bal += 1
		elif i == ']' or i == ')' or i == '}':
			bal -= 1
		elif bal == 0:
			res += i
	return res.strip()

def getAnimeInfoText(aid):
	pass

def sendAnimeInfo(msg, aid):
	global cur_cnt
	anime = getInfoById(aid)
	url = root_url[:-5] + anime["image"]["original"]
	print(url)
	uid = cur_cnt
	cur_cnt = (cur_cnt + 1) % 10
	path = f'images/{uid}.jpg'
	f = open(path, 'wb')
	f.write(urllib.request.urlopen(url).read())
	f.close()
	img = open(path, 'rb')
	bot.send_chat_action(msg.chat.id, 'upload_photo')
	genres = anime["genres"]
	while len(genres) > 5:
		genres = genres[:-1]
	genres_s = ''
	for genre in genres:
		genres_s += genre["russian"] + ', '
	desc = delRectBrackets(anime["description"].split("\n")[0])
	caption = f'{anime["russian"]}\n<b>Рейтинг</b>: {anime["score"]}/10\n<b>Cерий</b>: {anime["episodes"]}\n\n<b>Жанры</b>: {genres_s[:-2]}\n\n<b>Описание</b>: {desc}'
	bot.send_photo(msg.chat.id, img, caption=caption, parse_mode="html")

def wrand (a, b, c):
	d = numpy.random.randint(a, b)
	for i in range(c - 1):
		d = min(d, numpy.random.randint(a, b))
	return d

def getRandomAnime ():
	uid = wrand(1, MAX_PLACE, 3)
	anime = getAnimeList(1, uid, "popularity")
	if not anime:
		return None
	return anime[0]["id"]

MAX_PLACE = 300
animecsv = open('jsons/anime.csv', 'rb').read().decode('ascii',errors='ignore').split('\n')
print(len(animecsv))
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
	aid = getRandomAnime()
	sendAnimeInfo(msg, aid)

@bot.message_handler(commands=["top_alltime", "top_month", "top_week"])
def getTopForAll (msg):
	timeGot = msg.text
	if timeGot == "/top_alltime":
		anime = getTopForAll(10)
		res = ''
		for uid in anime:
			res += getAnimeInfoText(uid)
		bot.send_message(msg.char.id, res, parse_mode="html")
	else:
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