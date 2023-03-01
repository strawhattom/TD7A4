import os
from flask import Flask, url_for
from pymongo import MongoClient

app = Flask(__name__)
mongo_uri = os.environ.get("MONGO_URI")
client = MongoClient(mongo_uri)
db = client["testdb"]
collection = db["testcollection"]

# Adding data to the specific collection
# documents = [{"name": "Jane Doe", "age": 25},
#             {"name": "Jim Smith", "age": 35}]

# collection.insert_many(documents)

content = ''


@app.route("/")
def index():
    data = list(collection.find({}))
    return str(data)


@app.route("/text")
def text():
    file_path = open('.' + url_for('static', filename='content.txt'), 'r')
    content = file_path.readline()
    return str(content)


if __name__ == "__main__":
    app.run()
