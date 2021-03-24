from flask import Flask, request, jsonify, Response
import json
import mysql.connector

server = Flask(__name__)

@server.route("/")
def hello():
    return "Discount Service\n!!"

def get_mysql_connection():
    return mysql.connector.connect(user='discount_service', host='db', port='3306', password='123', database='discounts')

@server.route('/api/campaign', methods=['GET'])
def get_campaign():
    db = get_mysql_connection()
    print(db)
    try:
        sqlstr = "select * from campaigns;"
        print(sqlstr)
        cur = db.cursor()
        cur.execute(sqlstr)
        output_json = cur.fetchall()
    except Exception as e:
        print("Error in SQL:\n", e)
    finally:
        db.close()
    return jsonify(results=output_json)


if __name__ == "__main__":
   server.run(host='0.0.0.0')




