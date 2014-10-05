"""
Author: Remy D <remyd@civx.us>
        Ralph Bean <rbean@redhat.com>
        Mike Nolan <me@michael-nolan.com>
License: AGPLv3+
"""

import ConfigParser
import feedparser
import json
import urllib2
from flask import Flask
from flask.ext.mako import MakoTemplates, render_template
from flask import redirect, url_for, request

from evernote.api.client import EvernoteClient
from evernote.edam.notestore.ttypes import NoteFilter, NotesMetadataResultSpec
from evernote.edam.type.ttypes import NoteSortOrder

app = Flask(__name__)
app.template_folder = "templates"
mako = MakoTemplates(app)

config = ConfigParser.ConfigParser()
config.read('config.ini')

consumer_key = config.get('evernote', 'consumer_key', 0)
consumer_secret = config.get('evernote', 'consumer_secret', 0)
dev_token = config.get('evernote', 'dev_token', 0).strip("'")


@app.route('/')
def index():
    client = EvernoteClient(token=dev_token)
    userStore = client.get_user_store()
    user = userStore.getUser()
    username = user.username
    return render_template('index.mak', name='mako', username=username)


@app.route('/getbooks')
def getbooks():
    client = EvernoteClient(token=dev_token)
    noteStore = client.get_note_store()
    notebooks = noteStore.listNotebooks(dev_token)
    for n in notebooks:
        print n.name
    return "cool"


@app.route('/getevernote')
def getevernote():
    client = EvernoteClient(token=dev_token)
    updated_filter = NoteFilter(order=NoteSortOrder.UPDATED)
    offset = 0
    max_notes = 10
    result_spec = NotesMetadataResultSpec(includeTitle=True)
    note_store = client.get_note_store()
    result_list = note_store.findNotesMetadata(
        dev_token,
        updated_filter,
        offset,
        max_notes,
        result_spec)

    notes = {"timeline": {
        "headline": "Sh*t People Say",
        "type": "default",
        "text": "People say stuff",
        "startDate": "2014,8,26",
        "date": [],
        "era": [
            {
                "startDate": "2014,06,10",
                "endDate": "2014,08,11",
                "headline": "Headline Goes Here",
                "text": "<p>Body text goes here, some HTML is OK</p>",
                "tag": "This is Optional"
            }
        ]
    }}

    for note in result_list.notes:
        content = note_store.getNoteContent(dev_token, note.guid)
        content_list = content.split(',', 3)
        media = False
        if (content.contains(":wikipedia:") or content.contains(":twitter:") or
                content.contains(":youtube:")):
            media = True

        note_json = {
            "startDate": content_list[1].replace('-', ','),
            "endDate": content_list[2].replace('-', ','),
            "headline": note.title,
            "text": content_list[3]
        }
        notes['timeline']['date'].append(note_json)

    return json.dumps(notes)


@app.route('/postevernote')
def postevernote():
    '''
    An example script using the EvernoteClient to post new notes.
    Source:
    https://github.com/evernote/evernote-sdk-python/tree/master/sample/client
    '''
    #
    # A simple Evernote API demo script that lists all notebooks in the user's
    # account and creates a simple test note in the default notebook.
    #
    # Before running this sample, you must fill in your Evernote developer
    # token.
    #
    # To run (Unix):
    #   export PYTHONPATH=../../lib; python EDAMTest.py
    #

    import hashlib
    import binascii
    import evernote.edam.userstore.constants as UserStoreConstants
    import evernote.edam.type.ttypes as Types

    from evernote.api.client import EvernoteClient

    # Real applications authenticate with Evernote using OAuth, but for the
    # purpose of exploring the API, you can get a developer token that allows
    # you to access your own Evernote account. To get a developer token, visit
    # https://sandbox.evernote.com/api/DeveloperToken.action
    auth_token = dev_token

    if auth_token == "your developer token":
        print "Please fill in your developer token"
        print "To get a developer token, visit " \
            "https://sandbox.evernote.com/api/DeveloperToken.action"
        exit(1)

    # Initial development is performed on our sandbox server. To use the
    # production service, change sandbox=False and replace your
    # developer token above with a token from
    # https://www.evernote.com/api/DeveloperToken.action
    client = EvernoteClient(token=auth_token, sandbox=True)

    user_store = client.get_user_store()

    version_ok = user_store.checkVersion(
        "Evernote EDAMTest (Python)",
        UserStoreConstants.EDAM_VERSION_MAJOR,
        UserStoreConstants.EDAM_VERSION_MINOR
    )
    print "Is my Evernote API version up to date? ", str(version_ok)
    print ""
    if not version_ok:
        exit(1)

    note_store = client.get_note_store()

    # List all of the notebooks in the user's account
    notebooks = note_store.listNotebooks()
    print "Found ", len(notebooks), " notebooks:"
    for notebook in notebooks:
        print "  * ", notebook.name

    print
    print "Creating a new note in the default notebook"
    print

    # To create a new note, simply create a new Note object and fill in
    # attributes such as the note's title.
    note = Types.Note()
    note.title = "Test note from EDAMTest.py"

    # To include an attachment such as an image in a note, first create a
    # Resource for the attachment. At a minimum, the Resource contains the
    # binary attachment data, an MD5 hash of the binary data, and the
    # attachment MIME type.  It can also include attributes such as filename
    # and location.
    image = open('static/img/enlogo.png', 'rb').read()
    md5 = hashlib.md5()
    md5.update(image)
    hash = md5.digest()

    data = Types.Data()
    data.size = len(image)
    data.bodyHash = hash
    data.body = image

    resource = Types.Resource()
    resource.mime = 'image/png'
    resource.data = data

    # Now, add the new Resource to the note's list of resources
    note.resources = [resource]

    # To display the Resource as part of the note's content, include an
    # <en-media> tag in the note's ENML content. The en-media tag identifies
    # the corresponding Resource using the MD5 hash.
    hash_hex = binascii.hexlify(hash)

    # The content of an Evernote note is represented using Evernote Markup
    # Language (ENML). The full ENML specification can be found in the Evernote
    # API Overview at
    # http://dev.evernote.com/documentation/cloud/chapters/ENML.php
    note.content = '<?xml version="1.0" encoding="UTF-8"?>'
    note.content += '<!DOCTYPE en-note SYSTEM ' \
        '"http://xml.evernote.com/pub/enml2.dtd">'
    note.content += '<en-note>Here is the Evernote logo:<br/>'
    note.content += '<en-media type="image/png" hash="' + hash_hex + '"/>'
    note.content += '</en-note>'

    # Finally, send the new note to Evernote using the createNote method
    # The new Note object that is returned will contain server-generated
    # attributes such as the new note's unique GUID.
    created_note = note_store.createNote(note)

    status = "Successfully created a new note with GUID: " + created_note.guid
    print status
    return status


@app.route('/about')
def about():
    return render_template('about.mak', name='mako')


@app.route('/feed')
def feed():
    query = request.args.get('q').lower()
    request_type = request.args.get('type').lower()
    if request_type == 'news':
        google_news_rss_url = "https://news.google.com/news/feeds?q=" + "{0}".format(query) + "&output=rss"
        feed = feedparser.parse(google_news_rss_url).entries
        return render_template('feed.mak', request_type=request_type,
                               name='mako', feed=feed)
    elif request_type == 'bills':
        bills_response = urllib2.urlopen(
            "http://congress.api.sunlightfoundation.com/bills/search?query="
            + "{0}".format(query) + "&apikey=9b21768d77c648a39ba9b9e77cda089c")
        feed = json.loads(bills_response.read().decode(
            bills_response.info().getparam('charset') or 'utf-8'))['results']
        return render_template('feed.mak', request_type=request_type,
                               name='mako', feed=feed)


@app.route('/timeline')
def timeline():
    return render_template('timeline.mak', name='mako')


@app.route('/story')
def story():
    return render_template('story.mak', name='mako')
    # return redirect(url_for('static', filename='img/preso.svg'))


@app.route('/slides')
def slides():
    return redirect(url_for('static', filename='img/preso.svg'))
