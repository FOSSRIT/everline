"""
Author: Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
        Mike Nolan <me@michael-nolan.com>
License: AGPLv3+
"""
import os

import ConfigParser
from flask import Flask
from flask.ext.mako import MakoTemplates, render_template
from flask import redirect, url_for

app = Flask(__name__)
app.template_folder = "templates"
mako = MakoTemplates(app)

config = ConfigParser.ConfigParser()
config.read('config.ini')

consumer_key = config.get('evernote', 'consumer_key', 0)
consumer_secret = config.get('evernote', 'consumer_secret', 0)


@app.route('/')
def index():
    return render_template('index.mak', name='mako', consumer_key=consumer_key,
                           consumer_secret=consumer_secret)


@app.route('/about')
def about():
    return render_template('about.mak', name='mako')


@app.route('/story')
def story():
    return render_template('story.mak', name='mako')
    # return redirect(url_for('static', filename='img/preso.svg'))


@app.route('/slides')
def slides():
    return redirect(url_for('static', filename='img/preso.svg'))
