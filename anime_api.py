# uses shikimory.one
import requests
import json

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
	calendar = getReq(f'https://shikimori.one/api/calendar')
	return calendar

def getAllAnons():
	calendar = getCalendar()
	ans = []
	for elem in calendar:
		ans.append([elem["anime"]["id"], elem["next_episode_at"], elem["next_episode"]])
	for i in ans:
		print(i)

def getTopAllTime(cntInTop = 10):
    if cntInTop > 50:
        return []
    ans = []
    res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1')
    for i in res:
        ans.append(i["id"])
    return ans
