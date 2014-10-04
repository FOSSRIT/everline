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

CLIENT_ID = config.get('general', 'CLIENT_ID', 0)
CLIENT_SECRET = config.get('general', 'CLIENT_SECRET', 0)


@app.route('/')
def index():
    return render_template('index.mak', name='mako', CLIENT_ID=CLIENT_ID)


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
