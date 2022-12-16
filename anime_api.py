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