from flask import Flask, render_template, jsonify, request
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient
app = Flask(__name__)



client = MongoClient('localhost', 27017)
db = client.dbsparta


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index_week4.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    location_receive = request.form['location_give']
    call_num_receive = request.form['call_num_give']

    order = {'name': name_receive, 'count': count_receive, 'location': location_receive,'call_num': call_num_receive}

# 여길 채워나가세요!
    db.orders.insert_one(order)
    return jsonify({'result': 'success'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    result = list(db.orders.find({}, {'_id': 0}))
# 여길 채워나가세요!
    return jsonify({'result': 'success', 'orders': result})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)