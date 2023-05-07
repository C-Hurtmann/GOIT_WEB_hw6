from pathlib import Path
from sqlite3 import connect
from pprint import pprint

def execute(path_to_sql):
    with open(path_to_sql) as f:
        sql = f.read()
    with connect('main.db') as con:
        cur = con.cursor()
        cur.execute(sql)
        return cur.fetchall()


if __name__ == '__main__':
    query_1 = execute(Path('queries/query_1.sql'))
    query_2 = execute(Path('queries/query_2.sql'))
    query_3 = execute(Path('queries/query_3.sql'))
    query_4 = execute(Path('queries/query_4.sql'))
    query_5 = execute(Path('queries/query_5.sql'))
    query_6 = execute(Path('queries/query_6.sql'))
    query_7 = execute(Path('queries/query_7.sql'))
    query_8 = execute(Path('queries/query_8.sql'))
    query_9 = execute(Path('queries/query_9.sql'))
    query_10 = execute(Path('queries/query_10.sql'))
    query_11 = execute(Path('queries/query_11.sql'))
    query_12 = execute(Path('queries/query_12.sql')) 
    pprint(query_12)