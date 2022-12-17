# uses shikimory.one
import requests
import json
from datetime import datetime
from utils import levenstein

root_url = 'http://shikimori.one/api/'

headers =  {'User-Agent': 'PyShiki v1.1.4'}
s = requests.Session()  # Session for http-requests
s.headers.update(headers)

def getReq (url):
	return s.get(url).json()

def translate (name):
	res = getReq(f'https://shikimori.one/api/animes/search?q={name}')
	if len(res) == 0:
		return None
	return res[0]["russian"]

def getAnimeList (limit, page, order):
	res = getReq(f'https://shikimori.one/api/animes?limit={limit}&order={order}&page={page}')
	if len(res) == 0:
		return None
	return res

def getInfo (name):
	res = getReq(f'https://shikimori.one/api/animes/search?q={name}')
	if len(res) == 0:
		return None
	return res[0]

def getIdOnName (name):
	res = getReq(f'https://shikimori.one/api/animes/search?q={name}')
	if len(res) == 0:
		return None
	best = 0
	print(res[1])
	for i in range(0, min(len(res), 6)):
		print(res[i]['russian'], levenstein(res[i]['russian'], name, 1, 10, 0))
		if levenstein(res[best]['russian'], name, 1, 10, 0) > levenstein(res[i]['russian'], name, 1, 10, 0):
			best = i
	print(res[best]['russian'])
	return res[best]['id']

def getInfoById (id):
	return getReq(f'https://shikimori.one/api/animes/{id}')

def getGenres ():
	res = getReq('https://shikimori.one/api/genres')
	if len(res) == 0:
		return None
	return res

def getId (name):
	res = getInfo(name)
	if len(res) == 0:
		return None
	return res["id"]

def getGenre (name):
	for genre in getGenres():
		if genre["name"] == name:
			return genre["russian"]
	return None

def getGenreEng (name):
	for genre in getGenres():
		if genre["russian"] == name:
			return genre["name"]
	return None

def getCalendar():
	calendar = getReq(f'https://shikimori.one/api/calendar?censored=true')
	return calendar

def getAllAnons():
	calendar = getCalendar()
	ans = []
	for elem in calendar:
		ans.append([elem["anime"]["id"], elem["next_episode_at"], elem["next_episode"], elem["anime"]["russian"], elem["anime"]["score"]])
	return ans

def getTopAllTime(cntInTop = 10):
    if cntInTop > 50:
        return []
    ans = []
    res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1')
    for i in res:
        ans.append([i["russian"], i["score"]])
    return ans

def getYear():
	return datetime.now().year

def getMonth():
	return datetime.now().month

def getSeason():
	month = getMonth()
	if month == 12 or month == 1 or month == 2:
		return 'winter'
	elif month >= 3 and month <= 5:
		return 'spring'
	elif month >= 6 and month <= 8:
		return 'summer'
	else:
		return 'autumn'

def getSeasonRus(month):
	if month == 12 or month == 1 or month == 2:
		return 'зима'
	elif month >= 3 and month <= 5:
		return 'весна'
	elif month >= 6 and month <= 8:
		return 'лето'
	else:
		return 'осень'

def getTopThisYear(cntInTop = 10):
    if cntInTop > 50:
        return []
    ans = []
    res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1&season={getYear()}')
    for i in res:
        ans.append([i["russian"], i["score"]])
    return ans


def getTopThisMonth(cntInTop = 10):
	if cntInTop > 50:
		return []
	ans = []
	res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1&season={getSeason()}_{getYear()}')
	for i in res:
		ans.append([i["russian"], i["score"]])
	return ans
