from flask import Flask, render_template, request, jsonify

from pymongo import MongoClient

client = MongoClient('mongodb+srv://admin:01234@sparta.sjbnpdb.mongodb.net/?retryWrites=true&w=majority')
db = client.dbsparta

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')


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

@app.route('/fanpage', methods=["GET"])
def fanpage_go():
    #jk fanpage go func
    tmp = request.args.get('id')
    return render_template('test.html', id = tmp)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)