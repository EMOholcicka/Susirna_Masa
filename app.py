from flask import Flask, render_template
import sqlite3

app = Flask(__name__)


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


def database_query(sql):
    """
    :param sql: unicode
    :return: sqlite3.Row
    """
    conn = sqlite3.connect('database.db')
    conn.row_factory = dict_factory
    cur = conn.cursor()
    cur.execute(sql)
    rows = cur.fetchall()
    print(rows)

@app.route("/")
def index():
    database_query("select * from thresholds")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)