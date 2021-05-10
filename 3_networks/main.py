import psycopg2
import datetime
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    conn = _get_db_conn()
    cur = conn.cursor()
    current_timestamp = datetime.datetime.now()
    cur.execute(f"INSERT INTO mytable(user_input) VALUES ('{current_timestamp}');")
    conn.commit()
    return 'zaktualizowano bazę'

@app.route('/results')
def results():
    conn = _get_db_conn()
    cur = conn.cursor()
    cur.execute(f"SELECT * FROM mytable;")
    res = cur.fetchall()
    return str(res)


def _init_database():
    conn = _get_db_conn()
    cur = conn.cursor()
    try:
        cur.execute('SELECT 1 FROM mytable;')
        resp = cur.fetchone()
        print('Table found - init not needed')
    except psycopg2.errors.UndefinedTable:
        print("Coudn't find table mytable - creating a new one")
        conn = _get_db_conn()
        cur = conn.cursor()
        create_table_sql = "CREATE TABLE mytable (user_input VARCHAR(255));"
        cur.execute(create_table_sql)
        conn.commit()
        print('Table mytable created')


def _get_db_conn():
    conn = psycopg2.connect(
        host="posgres-srv",
        database="db1",
        user="user",
        password="abc123")
    return conn


if __name__ == '__main__':
    _init_database()
    app.run(host='0.0.0.0', port=5000, debug=True)
