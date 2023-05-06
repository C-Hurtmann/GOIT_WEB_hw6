import sqlite3

def create_databases():
    with open('create_sql', 'r') as f:
        sql = f.read()

    with sqlite3.connect('db.sqlite') as con:
        cur = con.cursor()
        cur.executescript(sql)

if __name__ =='__main__':
    create_databases()