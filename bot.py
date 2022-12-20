import telebot
import numpy
from anime_api import getIdOnUserName, getInfoById, root_url, getAnimeList, getTopAllTime, getTopThisMonth, getTopThisYear, getAllAnons, getSeasonRus, getIdOnName
import urllib
from utils import reduceText
import os
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from dotenv import load_dotenv


dotenv_path = os.path.join(os.path.dirname(__file__), '.env.local')
if os.path.exists(dotenv_path):
	print('loaded')
	load_dotenv(dotenv_path)
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

def getAnimeInfoText(russian, score):
	return f'<b>{russian}</b> - Рейтинг {score}/10'

def getAnimeInfoText2(russian, score):
	return f'<b>{russian}</b>\nРейтинг: {score}/10'

def getAnimeInfoTextById(uid):
	anime = getInfoById(uid)
	return f"{anime['russian']} - Рейтинг {anime['score']}/10"

def downloadAnimePhoto (link):
	global cur_cnt
	url = root_url[:-5] + link
	uid = cur_cnt
	cur_cnt = (cur_cnt + 1) % 10
	path = f'images/{uid}.jpg'
	f = open(path, 'wb')
	f.write(urllib.request.urlopen(url).read())
	f.close()
	return path

def parseAnimeGenres (genres):
	while len(genres) > 5:
		genres = genres[:-1]
	genres_s = ''
	for genre in genres:
		genres_s += genre["russian"] + ', '
	return genres_s[:-2]

def sendAnimeInfo(msg, aid):
	anime = getInfoById(aid)
	path = downloadAnimePhoto(anime["image"]["original"])
	img = open(path, 'rb')
	bot.send_chat_action(msg.chat.id, 'upload_photo')
	genres = parseAnimeGenres(anime["genres"])
	desc = ''
	if anime['description']:
		desc = reduceText(delRectBrackets(anime["description"].split("\n")[0]))
	caption = f'{anime["russian"]}\n<b>Рейтинг</b>: {anime["score"]}/10\n<b>Cерий</b>: {anime["episodes"]}\n\n<b>Жанры</b>: {genres}\n\n<b>Описание</b>: {desc}'
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

def genMarkup (aid):
	markup = InlineKeyboardMarkup()
	markup.row_width = 3
	for x in range(3):
		markup.add(InlineKeyboardButton(str(x * 3 + 1), callback_data=f"rate_{aid}_{x * 3 + 1}"), 
		InlineKeyboardButton(str(x * 3 + 2), callback_data=f"rate_{aid}_{x * 3 + 2}"), 
		InlineKeyboardButton(str(x * 3 + 3), callback_data=f"rate_{aid}_{x * 3 + 3}"))
	markup.add(InlineKeyboardButton('Не помню', callback_data=f"rate_{aid}_not"), 
		InlineKeyboardButton('10', callback_data=f"rate_{aid}_10"), 
		InlineKeyboardButton('Не смотрел', callback_data=f"rate_{aid}_not"))
	return markup

def rateAnime (msg, aid):
	anime = getInfoById(aid)
	path = downloadAnimePhoto(anime["image"]["original"])
	img = open(path, 'rb')
	bot.send_chat_action(msg.chat.id, "upload_photo")
	caption = f'<b>{anime["russian"]}</b>\n\n Как бы вы оценили данное аниме?'
	bot.send_photo(msg.chat.id, img, caption=caption, parse_mode="html", reply_markup=genMarkup(aid))

MAX_PLACE = 300
animecsv = open('jsons/anime.csv', 'rb').read().decode('ascii',errors='ignore').split('\n')
print(len(animecsv))
TOKEN = os.environ.get("TELEGRAM_TOKEN")
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

@bot.message_handler(commands=["top_alltime"])
def getTopForAll (msg):
	anime = getTopAllTime(10)
	res = 'Топ аниме по популярности:\n'
	for russian, score in anime:
		res += getAnimeInfoText2(russian, score) + '\n' * 2
	bot.send_message(msg.chat.id, res, parse_mode="html")

@bot.message_handler(commands=["top_month"])
def getTopForMonth (msg):
	anime = getTopThisMonth(10)
	print(anime)
	res = 'Топ аниме по популярности за месяц:\n'
	for russian, score in anime:
		res += getAnimeInfoText2(russian, score) + '\n' * 2
	bot.send_message(msg.chat.id, res, parse_mode="html")

@bot.message_handler(commands=["top_year"])
def getTopForYear (msg):
	anime = getTopThisYear(10)
	res = 'Топ аниме по популярности за год:\n'
	for russian, score in anime:
		res += getAnimeInfoText2(russian, score) + '\n' * 2
	bot.send_message(msg.chat.id, res, parse_mode="html")

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
	bot.send_message(msg.chat.id, 'Введите название аниме, которе посмотрели:')
	bot.register_next_step_handler(msg, process_watched_name)

def process_watched_name (msg):
	try:
		name = msg.text
		print(msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, name)	
		aid = getIdOnName(name)
		if not aid:
			print(1 / 0)
		rateAnime(msg, aid)
	except Exception as e:
		bot.reply_to(msg, 'Ни одного аниме с похожим названием не найдено.')
		print(e)
		
@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
	text = call.data
	if text[:4] == "rate":
		last = text.split('_')[-1]
		if last == 'not':
			bot.answer_callback_query(call.id, 'Вы не смотрели это')
		else:
			bot.answer_callback_query(call.id, f'Вы оценили это на {last}/10')



@bot.message_handler(commands=["get_all_anons"])
def anonsAnime (msg):
	anons = getAllAnons()
	cnt = 0
	res = 'Свежие анонсы аниме:\n'
	for elem in anons:
		if float(elem[4]) < 8:
			continue
		dat = elem[1].split('T')[0]
		month = dat.split('-')[1]
		year = dat.split('-')[0]
		cnt += 1
		res += getAnimeInfoText2(elem[3], elem[4])
		res += f"\nДата выхода: {'.'.join(dat.split('-')[::-1])}\n\n"
		if cnt >= 10:
			break
	print(res)
	bot.send_message(msg.chat.id, res, parse_mode="html")

def process_describe_name (msg):
	try:
		name = msg.text
		print(msg.from_user.username, msg.from_user.first_name, msg.from_user.last_name, name)	
		aid = getIdOnName(name)
		if not aid:
			print(1 / 0)
		sendAnimeInfo(msg, aid)
	except Exception as e:
		bot.reply_to(msg, 'Ни одного аниме с похожим названием не найдено.')
		print(e)

@bot.message_handler(commands=["describe"])
def describe(msg):
	bot.send_message(msg.chat.id, f'Введите название аниме, которое хотите узнать:')
	bot.register_next_step_handler(msg, process_describe_name)


def process_link_shikimori (msg):
	try:
		name = msg.text
		aid = getIdOnUserName(name)
		if not aid:
			print(1 / 0)
		# DO SOMETHING PLEASE
		# DO SOMETHING PLEASE
		# DO SOMETHING PLEASE
		# DO SOMETHING PLEASE
		# DO SOMETHING PLEASE
		# DO SOMETHING PLEASE
	except Exception as e:
		bot.reply_to(msg, 'Пользователя с таким никнеймом нет.')

@bot.message_handler(commands=["link_shikimori"])
def link_shikimori (msg):
	bot.send_message(msg.chat.id, "Введите ваш никнейм на <a href='https://shikimori.one'>shikimori</a>", parse_mode='html')
	bot.register_next_step_handler(msg, process_link_shikimori)

if __name__ == "__main__":
	bot.infinity_polling()