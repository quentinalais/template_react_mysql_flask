import flask 
from flask import request, jsonify 
import mysql.connector

app=flask.Flask(__name__)

app.config["DEBUG"]=True


config = {
        'user': 'admin',
        'password': 'admin',
        'host': 'db',
        'port': '3306'
    }
#connection = mysql.connector.connect(**config)

@app.route('/',methods=["GET"])
def home():
    return "<h1> Welcome to your Flask Backend. </h1>"

app.run(host="backend", debug=True)