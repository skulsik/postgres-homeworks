"""Скрипт для заполнения данными таблиц в БД Postgres."""
import psycopg2

# connect to BD
with psycopg2.connect(host='localhost', database='', user='postgres', password='12345') as conn:
    # greate cursor
    with conn.cursor() as cur:
        # execute query
        cur.execute('INSERT INTO table VALUES (%s, %s)', (3, 'fdgf'))

        cur.execute('SELECT * FROM table')
        # get info
        cur.fetchall()

# close cursor and connect
conn.close()
