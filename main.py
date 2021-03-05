from flask import Flask, request, render_template, jsonify, redirect
from flask_cors import CORS
from bdd import *
from data_video import *
import requests
from setup_logger import logger
import json

app = Flask(__name__)
CORS(app)

message = ''


@app.route('/create_table')
def create_table():
    global message
    db_learn = BDD()
    try:
        db_learn.execute_query(db_learn.create_table)
        message = 'SUCCESS'
    except:
        message = 'impossible to create table'
        app.logger.error('impossible to create table')
    db_learn.__disconnect__()
    return redirect('/admin')


@app.route('/insert_data')
def insert_data():
    global message
    db_learn = BDD()
    try:
        db_learn.insert_data(DataVideo().data)
        message = 'SUCCESS'
    except:
        print('impossible to insert data')
        message = 'ERROR'
    db_learn.__disconnect__()
    return redirect('/admin')


@app.route('/api/query_data')
def get_elearn_list():
    global message
    try:
        db_learn = BDD()
        data_learn = db_learn.select_from_db()
        db_learn.__disconnect__()
        return jsonify(data_learn)
    except:
        return redirect('/admin')


@app.route('/')
def page_data():
    return render_template('index.html')


@app.route('/admin')
def page_admin():
    global message
    return render_template('admin.html', message=message)
