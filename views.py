from flask import render_template, redirect, url_for

from app import app, db, freezer
from models import *

# Site Path
app.config['SITE_PATH'] = "2016/airbnb"

# Project Title
app.config['PROJ_TITLE'] = "Airbnb 2016"

"""
slug completes:
- twitter:url
- og:image/Facebook image preview
- Twitter/Facebook share url
- url for email body

title:
- Page title
- og:title/Facebook headline
- email subject
- twitter:title

description:
- meta description
- og:description/Facebook description

twitter_text:
- text that appears on tweet

"""

@app.route('/')
def index():
    return render_template('index.html',
    	title="",
    	description="",
    	twitter_text="")

@app.route('/scofflaws/')
def insight():
    return render_template('scofflaws.html',
        slug='',
        title='',
        description="",
        twitter_text='')

@app.route('/multiple/')
def photos():
    return render_template('multiple.html',
        slug='',
        title='',
        description="",
        twitter_text='')

@app.route('/economics/')
def data():
    return render_template('economics.html',
        slug='',
        title='',
        description="",
        twitter_text='')

@app.route('/methodology/')
def shelters():
    return render_template('methodology.html',
        slug='',
        title='',
        description="",
        twitter_text='')