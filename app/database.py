import psycopg2
from psycopg2.extras import RealDictCursor
import time


while True:
    try:
        conn = psycopg2.connect(host="localhost", database="fastapi", user="postgres", password="postgres",cursor_factory=RealDictCursor)
        cursor = conn.cursor()
        print("database connection successfull")
        break
    except Exception as err:
        print(f"database connection failed {err}") 
        time.sleep(3) 