from psycopg2 import connect, sql
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env.local')
if os.path.exists(dotenv_path):
	if __name__ == "__main__":
		print('loaded')
	load_dotenv(dotenv_path)

conn = connect(dbname=os.environ.get("POSTGRES_DB"), user=os.environ.get("POSTGRES_USER"), 
	password=os.environ.get("POSTGRES_PASSWORD"), host="localhost")

