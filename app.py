#!/usr/bin/env python
""" Coaching Institute Web Application """

__author__      = "Kaushik Chhappaniya"
__copyright__   = "Copyright 2023, Flask_CRUD"

import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
def db_connect():
    conn = psycopg2.connect(database='flask_db', host='localhost', user='postgres', password='kaushik', port='5432')
    
    return conn

@app.route('/')
def home():
    conn = db_connect()
    curr = conn.cursor()
    curr.execute("SELECT * FROM courses ORDER BY id")
    data = curr.fetchall()
    curr.close()
    conn.close()
    return render_template('home.htm', data=data)

@app.route('/create', methods=['POST'])
def create():
    conn = db_connect()
    curr = conn.cursor()
    name = request.form['name']
    fees = request.form['fees']
    duration = request.form['duration']
    curr.execute('''INSERT INTO courses (name, fess, duration) VALUES (%s, %s, %s)''', (name, fees, duration))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('home'))

@app.route('/update', methods=['POST'])
def update():
    conn = db_connect()
    curr = conn.cursor()
    name = request.form['name']
    fess = request.form['fees']
    duration = request.form['duration']
    id = request.form['id']
    curr.execute('''UPDATE courses SET name=%s, fess=%s, duration=%s WHERE id=%s''', (name, fess, duration, id))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('home'))


@app.route('/delete')
def delete():
    conn = db_connect()
    curr = conn.cursor()
    id = request.form['id']
    curr.execute('''DELETE FROM courses WHERE id=%s''', (id))
    conn.commit()
    curr.close()
    conn.close()
    return redirect(url_for('home'))
    
if __name__ == '__main__':
    app.run(host='localhost', debug=True)
