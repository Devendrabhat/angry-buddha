from flask import Flask, render_template, request, flash, session, g, redirect, url_for
import requests
from flask_wtf.csrf import CSRFProtect
import random
import csv
import os

import sqlite3

app = Flask(__name__)
csrf = CSRFProtect(app)
csrf.init_app(app)
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY


@app.route('/', methods=['GET', 'POST'])
@csrf.exempt
def home_page():
    if request.method =='POST':
        return 'Success'
    elif request.method =='GET':
        return render_template('home_volunteer_page.html')

@app.route('/sapling_for_water', methods=['GET', 'POST'])
@csrf.exempt
def sapling_for_water():
    if request.method =='POST':
        return render_template('saplings_for_water.html')
    elif request.method =='GET':
        return render_template('saplings_for_water.html')

@app.route('/new_sapling_here', methods=['GET', 'POST'])
@csrf.exempt
def new_sapling_here():
    if request.method =='POST':
        lat = request.form['lat']
        lng = request.form['lng']
        sap_id = request.form['sap_id']
        print(request.form)
        return 'Success'
    elif request.method =='GET':
        data = request.args['sap_id']
        return render_template('new_sapling_here.html', data=data)

@app.route('/plant', methods=['GET', 'POST'])
@csrf.exempt
def home_page1():
    if request.method == 'POST':
        print(request.form)
        lat = request.form['lat']
        lng = request.form['lng']
        print(f'latitude: {lat}\nlongitude: {lng}\n')
        return 'Sucess'
    else:
        return render_template('home.html')


@app.route('/sapling_page', methods=['GET', 'POST'])
@csrf.exempt
def sapling_page():
    if request.method == 'POST':
        print(request.form)
        return 'Success'
    elif request.method == 'GET':
        data = request.args['sap_id']
        return render_template('sapling_page.html', data=data)


if __name__ == '__main__':
    app.run('localhost', 8080, debug=True)
