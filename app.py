from flask import Flask, render_template, jsonify, request
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('localhost', 27017)
db = client.dbStock
# dbStock => 대소문자를 구분한다.


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/stock', methods=['GET'])
def show_diary():
    codes = list(db.codes.find({}, {'_id': False}))

    return jsonify({'all_codes': codes})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)


