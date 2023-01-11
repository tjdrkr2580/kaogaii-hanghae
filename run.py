from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:01234@sparta.sjbnpdb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fanpage')
def fanpage():
    return render_template('fanpage.html')

@app.route("/idol", methods=["POST"])
def idol_post():
    # db.idol.insert_one(doc)
    
    count = len(list(db.idol.find({}))) + 1
    idol_name = request.form['idol_name']
    idol_link = request.form['idol_link']

    doc = {
        'idol_num' : count,
        'idol_name' : idol_name,
        'idol_link' : idol_link
    }

    db.idol.insert_one(doc)
    return jsonify({'msg': '응원 완료!'})


@app.route("/idol", methods=["GET"])
def idol_get():
    idol_list = list(db.idol.find({},{'_id':False}))
    return jsonify({'idol':idol_list})

@app.route("/comment", methods=["POST"])
def comment_post():

    name_receive = request.form["name_give"]
    comment_receive = request.form["comment_give"]
    num_receive = request.form['num_give']

    doc = {
        'idol_num' : num_receive,
        'name': name_receive,
        'comment': comment_receive
    }

    db.comments.insert_one(doc)
    return jsonify({'msg': '남기기 완료!'})

@app.route("/comment", methods=["GET"])
def comments_get():
    comments_list = list(db.comments.find({},{'_id':False}))
    return jsonify({'comments':comments_list})

if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)