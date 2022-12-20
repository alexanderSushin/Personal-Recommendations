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

def distNames(api, name):
	return (1 + levenstein(api['russian'], name, 5, 10, 0)) * (10 - float(api['score']))


def getIdOnName (name):
	best_api, lev = 228, 2020202020
	any_api = False
	all_api = getReq(f'https://shikimori.one/api/animes/search?q={name}&limit=50')
	for i in range(min(len(all_api), 10)):
		cur_lev = distNames(all_api[i], name)
		print(all_api[i]['russian'], cur_lev)
		any_api = True
		if lev > cur_lev or (lev == cur_lev and all_api[i]['score'] > best_api['score']):
			lev = cur_lev
			best_api = all_api[i]
	name_split = name.split()
	for word in name_split:
		all_api = getReq(f'https://shikimori.one/api/animes/search?q={word}')
		for i in range(min(len(all_api), 10)):
			any_api = True
			cur_lev = distNames(all_api[i], name)
			print(all_api[i]['russian'], cur_lev)
			if lev > cur_lev or (lev == cur_lev and all_api[i]['score'] > best_api['score']):
				lev = cur_lev
				best_api = all_api[i]
	if not any_api:
		return None
	print(best_api['russian'])
	return best_api['id']

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

def getSeason(month):
	if month == 1 or month == 2:
		return 'winter'
	elif month >= 3 and month <= 5:
		return 'spring'
	elif month >= 6 and month <= 8:
		return 'summer'
	else:
		return 'fall'

def getSeasonRus(month):
	if month == 1 or month == 2:
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
	month = getMonth()
	res = getReq(f'https://shikimori.one/api/animes?limit={cntInTop}&order=ranked&page=1&season={getSeason(month)}_{getYear()}')
	for i in res:
		ans.append([i["russian"], i["score"]])
	return ans

def getIdOnUserName(username):
    r = getReq(f'https://shikimori.one/{username}')
    soup = BeautifulSoup(r.text, "html.parser")
    lst = soup.findAll('section', class_='l-page')
    if len(lst) == 0:
        return None
    need = (str(lst[0]).split('data-user-id'))[1]
    id = ''
    for i in range(2, len(need)):
        if need[i].isdigit():
            id += need[i]
        else:
            break
    return int(id)


def getAnimeRatesById(user_id):
	res = getReq(f'https://shikimori.one/api/v2/user_rates?user_id={user_id}')
	arr = []
	for item in res:
		arr.append((item["target_id"], item["score"]))
	return arr
