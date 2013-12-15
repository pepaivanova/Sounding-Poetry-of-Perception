from flask import Flask
from database import db_session

app = Flask(__name__)

@app.teardown_appcontext
def shutdown_session(exception=None):
    db_session.close()
    db_session.remove()

@app.route('/')
def home():
    return "Hello World!"


if __name__ == '__main__':
    app.run()