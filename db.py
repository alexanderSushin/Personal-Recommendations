import psycopg2
from dotenv import load_dotenv
import os

dotenv_path = os.path.join(os.path.dirname(__file__), '.env.local')
if os.path.exists(dotenv_path):
	if __name__ == "__main__":
		print('loaded')
	load_dotenv(dotenv_path)

conn = psycopg2.connect(dbname=os.environ.get("POSTGRES_DB"), user=os.environ.get("POSTGRES_USER"), 
	password=os.environ.get("maindb"), host="localhost")
