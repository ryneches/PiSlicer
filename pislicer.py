#!/usr/bin/env python

from flask import Flask
from flask import request, session, redirect, url_for
from flask import render_template
from flask import g, flash, send_from_directory
from contextlib import closing
from werkzeug import secure_filename
import json

# Flask configuration
DEBUG = True
TRAP_BAD_REQUEST_KEY_ERRORS = True
TRAP_HTTP_EXCEPTIONS = True
SECRET_KEY = 'OMG so secret'
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = set(['stl'])

app = Flask(__name__)
app.config.from_object(__name__)

@app.route( '/' )
def index() :
    """
    The application root.
    """
    authenticated = False
    user, username = 'test', 'test'
    
    return render_template( 'index.html',
                            user = user,
                            username = username,
                            authenticated = authenticated )

@app.route( '/favicon.ico' )
def favicon() :
    return redirect( url_for( 'static', filename='favicon.ico' ) )

if __name__ == '__main__' :
    app.debug = True
    app.run()
