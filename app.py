# Words Counter and Paragraphs Counter hi

# Words Counter and Paragraphs Counter 

from flask import Flask, request, render_template
from datetime import datetime
from pymongo import MongoClient
import os
import sys

app = Flask(__name__)
#client = MongoClient("mongodb://mongodb:27017/")  # Use the correct connection string format

db_url = os.environ.get("DB_URL")
user_name = os.environ.get("USER_NAME")
password = os.environ.get("USER_PWD")
if db_url is None or user_name is None or password is None:
    print("ERROR: DB_URL, USER_NAME, and USER_PWD environment variables are not set.")
    sys.exit(1)

client = MongoClient(db_url, username=user_name, password=password)
db = client["Python-app"]
collection = db["Word-count"]

def replace_multiple_newlines(text):
    lines = text.split('\n')
    lines = [line for line in lines if line.strip()]
    return len(lines)

@app.route('/')
def home():
    return render_template('home.html', datetoday2=datetime.now().strftime("%d-%B-%Y"))

@app.route('/count', methods=['POST'])
def count():
    text = request.form['text']

    words = len(text.split())
    paras = replace_multiple_newlines(text)
    text = text.replace('\r', '')
    text = text.replace('\n', '')
    chars = len(text)

    result = {
        "words": words,
        "paragraphs": paras,
        "characters": chars,
        "date": datetime.now().strftime("%d-%B-%Y")
    }
    collection.insert_one(result)

    return render_template('home.html', words=words, paras=paras, chars=chars, datetoday2=datetime.now().strftime("%d-%B-%Y"))

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)

    