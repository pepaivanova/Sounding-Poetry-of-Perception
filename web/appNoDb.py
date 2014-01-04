from flask import Flask
from flask import render_template
from flask import request
from send2Pd import send2Pd 
from send2Pd import audioOn
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    if request.method == 'POST':
	# get text from the form 
        text=request.form['poetry']
        # turn on audio
        audioOn()
        # send text to pure data
        send2Pd(text)
        # show text on the bottom of page
        return render_template('index.html', result=text)
    else:
        error = 'Error !'
    #
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    # open About page, where should be described the project
    return render_template('about.html')


if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')
