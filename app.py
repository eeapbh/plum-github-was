from flask import Flask, request, jsonify, session
import pymysql
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
@app.route('/home')
def home():
    return'flask'

@app.route('/api/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        args = request.args
        data = args.to_dict()
        user_id = data['user_id']
        user_pw = data['user_pw']
        print(user_id)
        print(user_pw)

        try:
            db = pymysql.connect(host='127.0.0.1', user='root', password='bong0000', db='userdb', charset='utf8')
            cursor = db.cursor(pymysql.cursors.DictCursor)
            sql = "SELECT * FROM user_table where user_id = %s AND user_pw = %s"
            cursor.execute(sql, (user_id, user_pw))
            confirm = cursor.fetchall()
            print(confirm)
            if confirm:
                # session['login'] = True
                response = {
                    'success': True,
                    'data': confirm
                }
                return jsonify(response)
            else:
                return 'login fail'
        except Exception as e:           
            print("error", e)
            return 'error'

        finally:
            if db:
                cursor.close()
                db.close()
            

if __name__ == '__main__':
    app.run(debug=True)