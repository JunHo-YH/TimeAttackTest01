from flask import Flask, render_template, jsonify, request
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client.dbStock


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post', methods=['POST'])
def save_post():

    idx = request.form['idx']
    title = request.form['title']
    content = request.form['content']
    reg_date = request.form['reg_date']
    doc = {
        "idx" : idx,
        "title" : title,
        "content" : content,
        "reg_date" : reg_date

    }
    db.list.insert_one(doc)
    return {"result": "success"}


@app.route('/post', methods=['GET'])
def get_post():
    result = list(db.list.find({}, {'_id':False}))
    return jsonify({'result':result})


@app.route('/post', methods=['DELETE'])
def delete_post():
    idx = request.form['idx']
    db.list.delete_one({'idx': idx})
    return {"result": "success"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)