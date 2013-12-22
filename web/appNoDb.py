from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)


@app.route('/', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    if request.method == 'POST':
	# return entered text in to the form to the page
        return render_template('index.html', result=request.form['poetry'])
    else:
        error = 'Error !'
    #
    return render_template('index.html', name=name)

@app.route('/about')
def about():
    # open About page, where should be described the project
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)
