from flask import Flask, render_template
from flask import g
from sense_emu import SenseHat
import time
import sqlite3
import pygal

app = Flask(__name__)
DATABASE = "/home/pi/Documents/Poseidon/Poseidon.db"


def connect_db():
    connection = sqlite3.connect(DATABASE)
    return connection


@app.before_request
def before_request():
    g.db = connect_db()


def query_db(query, args=(), one=False):
    cur = g.db.execute(query, args)
    rv = [dict((cur.description[idx][0], value)
               for idx, value in enumerate(row)) for row in cur.fetchall()]
    return (rv[0] if rv else None) if one else rv


def get_datas_by_name(name):
    connection = connect_db()
    c = connection.cursor()
    datas = query_db("select " + str(name) + " from data_poseidon ORDER BY ID DESC LIMIT 0, 20")
    tab = []
    i = 0
    for row in datas:
        tab.append(row[str(name)])

    return tab


def get_data_full():
    connection = connect_db()
    c = connection.cursor()
    datas = query_db("select * from data_poseidon ORDER BY id DESC")
    str(datas)
    return datas


@app.route('/pygalexample/')
def pygalexample():
    temp = pygal.Line()
    temp.title = 'Temperatures of the Server Room'
    temp.x_labels = get_datas_by_name('Timestamp')
    temp.add('Temperature', get_datas_by_name('Temperature'))
    temp_data = temp.render_data_uri()

    pressure = pygal.StackedLine(fill=True)
    pressure.title = 'Pressure of the Server Room'
    pressure.x_labels = get_datas_by_name('Timestamp')
    pressure.add('Air Pressure', get_datas_by_name('Pression'))
    pressure_data = pressure.render_data_uri()

    humidity = pygal.Line()
    humidity.title = 'Humidity of the Server Room'
    humidity.x_labels = get_datas_by_name('Timestamp')
    humidity.add('Humidity', get_datas_by_name('Humidity'))
    humidity_data = humidity.render_data_uri()

    return render_template("graphing.html", temp=temp_data, pressure=pressure_data, humidity=humidity_data)


@app.route('/')
def index():
    datas = get_data_full()
    return render_template("index.html", datas=datas)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
