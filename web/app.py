import os
import os.path as p

from flask import Flask
from flask import render_template
from flask import request
import database
from send2Pd import checkPdStarted
from send2Pd import startStopPd
from send2Pd import send2Pd
from send2Pd import dspOn
from send2Pd import dspOff
app = Flask(__name__)

db_file = p.abspath(p.join(os.getcwd(), 'sounds.db'))
database.connect_db(db_file)

# check if pure data is running and if not start it
if checkPdStarted('pdextended'):
    print("Pure Data is running")
else:
    startStopPd('pdextended -nogui -noadc -open ../pd/startSoundFromPython.pd &')
    print("Pure Data started")


@app.route('/', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    if request.method == 'POST':
    # get text from the form
        text = request.form['poetry']
        if text != "Please enter text.":
            database.store_poetry(text)
        # turn on audio
        dspOn()
        # send text to pure data
        send2Pd(text)
        return render_template('index.html', result=text)
        #
    else:
        error = 'Error !'
    #
    return render_template('index.html', name=name)


@app.route('/config', methods=['POST', 'GET'])
def config():
    if request.method == 'POST':
        if request.form['sound_off'] == "Sound OFF":
            dspOff()
            print("Sound OFF")
    # config page, where sounds could be started and stoped
    return render_template('config.html')


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
