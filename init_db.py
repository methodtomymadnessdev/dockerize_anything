import os
import psycopg2
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT # <-- ADD THIS LINE



# Open a cursor to perform database operations
def setup_db():
    con = psycopg2.connect(dbname='postgres',
        user=os.environ.get('user','postgres'), host=os.environ.get('host', 'database'),
        password=os.environ.get('password', 'postgres'))

    con.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT) # <-- ADD THIS LINE

    cur = con.cursor()

    # Use the psycopg2.sql module instead of string concatenation 
    # in order to avoid sql injection attacks.
    cur.execute(sql.SQL("CREATE DATABASE books"))
    conn = psycopg2.connect(host=os.environ.get('host', 'database'),
                                database=os.environ.get('database', 'books'),
                                user=os.environ.get('user', 'postgres'),
                                password=os.environ.get('password', 'postgres'),
                               )

    cur = conn.cursor()

    # Execute a command: this creates a new table
    cur.execute('DROP TABLE IF EXISTS books;')
    cur.execute('CREATE TABLE books (id serial PRIMARY KEY,'
                                     'title varchar (150) NOT NULL,'
                                     'author varchar (50) NOT NULL,'
                                     'pages_num integer NOT NULL,'
                                     'review text,'
                                     'date_added date DEFAULT CURRENT_TIMESTAMP);'
                                     )

    # Insert data into the table

    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('A Tale of Two Cities',
                 'Charles Dickens',
                 489,
                 'A great classic!')
                )


    cur.execute('INSERT INTO books (title, author, pages_num, review)'
                'VALUES (%s, %s, %s, %s)',
                ('Anna Karenina',
                 'Leo Tolstoy',
                 864,
                 'Another great classic!')
                )

    conn.commit()

    cur.close()
    conn.close()
