from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient 

from flask_pymongo import pymongo
from wtforms.validators import InputRequired 
app = Flask(__name__)

#route to index/home page
@app.route('/')
def index_page(name=None):
    return render_template('index.html', name=name)

#route to feedback page
@app.route('/feedback', methods=['POST','GET']) 
def feedback_page():   
        if request.method == "POST": 
             user_name = request.form.get('user_name') 
             user_email = request.form.get('user_email') 
             user_comment = request.form.get('user_comment') 
             db.feedback.insert_one({"name": user_name,
                                     "email": user_email,
                                     "comment": user_comment}) 
        return render_template('feedback.html')   

#mongodb config 
app.config['SECRET_KEY'] = '1b7a998cfaa5610d75e2b5ac16afd49b45bcf314' 
CONNECTION_STRING = 'mongodb+srv://lombardodierch:mytestdb@cluster0.ngmmokf.mongodb.net/?retryWrites=true&w=majority'

#mongodb setup/connecting to database
client = pymongo.MongoClient(CONNECTION_STRING)
db = client.get_database('donate_testdb')
user_collection = pymongo.collection.Collection(db, 'feedback')


if __name__ == '__main__':
    app.run(debug=True, port=5001)