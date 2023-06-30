import os
import logging
from flask import Flask
import psycopg2

app = Flask(__name__)
logger = logging.getLogger(__name__)

def get_db_connection():
    return psycopg2.connect(host=os.environ.get('host', 'database'),
                            database=os.environ.get('database', 'books'),
                            user=os.environ.get('user', 'postgres'),
                            password=os.environ.get('password', 'postgres'),
                           )

@app.route("/")
def index():
    return {"hello": "world"}

@app.route("/books")
def check_db():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute('select * from books')
    books = cur.fetchall()
    cur.close()
    conn.close()
    return {"books": books}

@app.route('/run-db-init-script')
def setup_db():
    from init_db import setup_db
    setup_db()
    return {"done": "done"}

