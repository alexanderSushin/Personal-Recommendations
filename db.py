from psycopg2 import connect, sql
from dotenv import load_dotenv
import os
from user import User
from anime import Anime
from genre import Genre

main_file = (__name__ == "__main__")
dotenv_path = os.path.join(os.path.dirname(__file__), '.env.local')
if os.path.exists(dotenv_path):
	if main_file:
		print('loaded')
	load_dotenv(dotenv_path)

conn = connect(dbname=os.environ.get("POSTGRES_DB"), user=os.environ.get("POSTGRES_USER"), 
	password=os.environ.get("POSTGRES_PASSWORD"), host="localhost")
cur = conn.cursor()

if main_file:
	print('connection successfull')

def insertUser (user: User):
	try:
		cur.execute("INSERT INTO users (telegram_id, telegram_chat_id, is_deleted, shikimori) VALUES (%s, %s, %s, %s)", user.exportInsert())
		conn.commit()
		return True
	except Exception as e:
		print(e)
		return False

def getUserById (user_id: int) -> User:
	cur.execute('SELECT * FROM users WHERE id=%s;', [user_id])
	res = cur.fetchone()
	return User(res)

def getUserByTid (telegram_id: int) -> User:
	cur.execute('SELECT * FROM users WHERE tid=%s;', [telegram_id])
	res = cur.fetchone()
	return User(res)

def updateLogin (user: User):
	cur.execute('UPDATE users SET shikimori=%s WHERE id=%s', [user.login, user.id])
	conn.commit()

def getAnimeById (anime_id: int) -> Anime:
	cur.execute('SELECT * FROM anime_list WHERE id=%s;', [anime_id])
	res = cur.fetchone()
	return Anime(res)

def getAnimeBySid (anime_id: int) -> Anime:
	cur.execute('SELECT * FROM anime_list WHERE shikimory_id=%s;', [anime_id])
	res = cur.fetchone()
	return Anime(res)

def getGenreByName (name: str) -> Genre:
	cur.execute('SELECT * FROM genres WHERE name=%s;', [name])
	res = cur.fetchone()
	return Genre(res)

def getGenreByRussian (name: str) -> Genre:
	cur.execute('SELECT * FROM genres WHERE russian=%s;', [name])
	res = cur.fetchone()
	return Genre(res)

def getGenreById (id: int) -> Genre:
	cur.execute('SELECT * FROM genres WHERE id=%s;', [id])
	res = cur.fetchone()
	return Genre(res)

def insertAnime (anime: Anime):
	cur.execute('INSERT INTO anime_list (shikimory_id, name, russian, url, status, score, episodes, year, rating, description, image_url, genres) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)', anime.exportInsert())
	conn.commit()

if main_file:
	conn.close()