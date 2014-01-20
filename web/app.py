import os
import os.path as p
from time import time, sleep
from os import path, getcwd

from flask import Flask
from flask import render_template
from flask import request
import database
from Pd import Pd
from time import gmtime, localtime, strftime
from send2Pd import checkPdStarted
from send2Pd import startStopPd
# from send2Pd import send2Pd
from send2Pd import processText
from send2Pd import dspOn
from send2Pd import dspOff
app = Flask(__name__)

db_file = p.abspath(p.join(os.getcwd(), 'sounds.db'))
database.connect_db(db_file)

#start Pure Data
def startPd():
    # Here should be placed the generation of the commands to PD
    '''
    pd = Pd(nogui=False)
    print("PD started")
    pd.Send(["Hello", "World"])
    '''
    print("Starting PD")
    start = time()
    # launching pd
    pd = Pd(nogui=False)
    pd.Send(["test message", 1, 2, 3])

    def Pd_hello(self, message):
        print "Pd called Pd_hello(%s)" % message

    pd.Pd_hello = Pd_hello

    sentexit = False
    # running a bunch of stuff for up to 20 seconds
    while time() - start < 60 and pd.Alive():
        if time() - start > 20 and not sentexit:
            pd.Send(["exit"])
            sentexit = True
        pd.Update()

    if pd.Alive():
        pd.Exit()


def getCurrentDateTime():
    # return date and time string
    dateAndTime = strftime("%Y-%m-%d %H:%M:%S", localtime())
    return dateAndTime


@app.route('/', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    if request.method == 'POST':
    # get text from the form
        text = request.form['poetry']
        if text != "enter your poem here ...":
            database.store_poetry(text)
            # turn on audio
            dspOn()
            # send text to pure data
            startPd()
            processText(text)
            # get current date and time
            dt = getCurrentDateTime()
            place = "Bulgaria, Sofia"
            txt = text
            text = dt + " | " + place + " | " + txt
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
