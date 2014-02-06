import os
import os.path as p
from time import time, sleep
from os import path, getcwd

from flask import Flask
from flask import render_template
from flask import request, redirect, url_for
from werkzeug import secure_filename

import database
from time import gmtime, localtime, strftime
from sounding import processPoetry

app = Flask(__name__)

db_file = p.abspath(p.join(os.getcwd(), 'sounds.db'))
database.connect_db(db_file)

# flask-uploads extension
UPLOAD_FOLDER = 'patches/sounds'
ALLOWED_EXTENSIONS = set(['wav', 'mp3'])
global SET_LOCATION
SET_LOCATION = ''

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS

#start Pure Data
# Here should be implemented the communication between PD and Python

def getCurrentDateTime():
    # return date and time string
    dateAndTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    return dateAndTime


@app.route('/', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    try:
        prn = Printer()
        prn.connect()
    except:
        prn = None
        print('Printer not found.')
    if request.method == 'POST':
    # get text from the form
        text = request.form['poetry']
        if text != "enter your poem here ...":
            database.store_poetry(text)
            processPoetry(text)
            # get current date and time
            dt = getCurrentDateTime()
            place = SET_LOCATION
            txt = text
            text = dt + " | " + place + " | " + txt
            # print text message on thermal printer
            if prn is not None:
                prn.printText(text)
                # disconnect printer
                prn.disconnect()
        return render_template('index.html', result=text)
        #
    else:
        error = 'Error !'
    #
    return render_template('index.html', name=name)


@app.route('/upload', methods=['POST', 'GET'])
def upload_file():
    if request.method == 'POST':
        file = request.files['file']
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            #return redirect(url_for('uploaded_file',
            #                        filename=filename))
            #return render_template('config.html', result=filename)
            return '''
            <!doctype html>
            <title>Upload new File</title>
            <h1>Upload new File</h1>
            <form action="" method=post enctype=multipart/form-data>
            <p><input type=file name=file>
                <input type=submit value=Upload>
            </form>
            <p>File uploaded</p>
            '''

    return '''
    <!doctype html>
    <title>Upload new File</title>
    <h1>Upload new File</h1>
    <form action="" method=post enctype=multipart/form-data>
      <p><input type=file name=file>
         <input type=submit value=Upload>
    </form>
    '''

@app.route('/config', methods=['POST', 'GET'])
def config(name='Example: Sofia, Bulgaria'):
    # configuration of the settings
    error = None
    if request.method == 'POST':
    # get text from the form
        location = request.form['location']
        if location != "Set location here.":
            SET_LOCATION = location
            #print(SET_LOCATION)
            new_location = "Location set to: " + location
        return render_template('config.html', result=new_location)
        #
    else:
        error = 'Error !'
    #
    return render_template('config.html', result=name)


@app.route('/about')
def about():
    # open About page, where should be described the project
    return render_template('about.html')


@app.route('/history')
def history():
    all_ = database.db_session.query(database.Poetry).all()
    return '<br>'.join(p.poetry for p in all_)


@app.teardown_appcontext
def shutdown_session(exception=None):
    database.db_session.remove()

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
