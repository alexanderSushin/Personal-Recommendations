from psycopg2 import connect, sql
from dotenv import load_dotenv
import os
from user import User

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

if main_file:
	conn.close()