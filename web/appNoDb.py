from flask import Flask
from flask import render_template
from flask import request
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World - Rado !'

@app.route('/project')
def projects():
    return 'The project page'

@app.route('/about')
def about():
    return 'The about page'

@app.route('/poetry', methods=['POST', 'GET'])
def poetry(name=None):
    error = None
    if request.method == 'POST':
        return 'It works !'
    else:
        error = 'Error!'
    #
    return render_template('index.html', name=name)


if __name__ == '__main__':
    app.run(debug=True)
