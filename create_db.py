from sqlite3 import connect
from pathlib import Path


def create_databases():
    path = Path('create_dbs.sql')
    with open(path, 'r') as f:
        sql = f.read()

    with connect('test.db') as con:
        cur = con.cursor()
        cur.executescript(sql)
    
    con.close()


if __name__ =='__main__':
    create_databases()