from flask import render_template, redirect, url_for, request

from app import app, db, freezer
from models import *

# Site Path
app.config['SITE_PATH'] = "2016/airbnb"

# Project Title
app.config['PROJ_TITLE'] = "Airbnb 2016"

# Project Hashtag
app.config['HASHTAG'] = 'Airbnb2016'

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
    	title="Airbnb, rivals flourish in SF amid regulatory crackdown",
    	description="Special report: Data on Airbnb shows that visitors continue to flock to the rentals - often in defiance of city requirements to register these impromptu inns.",
    	twitter_text="Airbnb, rivals flourish in SF amid regulatory crackdown.")

@app.route('/laws/')
def scofflaws():
    return render_template('scofflaws.html',
        slug='laws',
        title='Most Airbnb hosts ignore SF vacation-rental laws',
        description="Special report Turning houses into fulltime hotels is a huge violation. But there are other problems - and new changes coming to how existing rules are enforced.",
        twitter_text="Most Airbnb hosts ignore SF vacation-rental laws.")

@app.route('/hostels/')
def multiple():
    return render_template('multiple.html',
        slug='hostels',
        title="Home-based hostels spring up on Airbnb",
        description="Special report: Home-based hostels appear to be on the rise in San Francisco and some of the informal hostels seem to be big business.",
        twitter_text="Home-based hostels spring up on Airbnb.")

@app.route('/economics/')
def economics():
    return render_template('economics.html',
        slug='economics',
        title="Is Airbnb to blame for high housing prices in SF?",
        description="Special report: Some say companies like Airbnb drive up rent, but the impact is strongest at the micro level - in popular areas where rentals are most concentrated.",
        twitter_text="Is Airbnb to blame for high housing prices in SF?")

@app.route('/methodology/')
def methodology():
    return render_template('methodology.html',
        slug='',
        title='Methodology',
        description="How The Chronicle crunched the Airbnb data",
        twitter_text='Airbnb, rivals flourish in SF amid regulatory crackdown.')