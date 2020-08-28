from flask import Flask, render_template
from flask_pymongo import PyMongo
from main import userTest

app = Flask(__name__)

@app.route('/user/<string:name>')
def tryFlask(name = "王一博"):
	stringName = userTest(start_words = name)
	return stringName

if __name__ == '__main__':
    app.run(debug=True)