from flask import Flask, render_template
from flask_pymongo import PyMongo  
app = Flask(__name__)

#route to index/home page
@app.route('/')
def index_page(name=None):
    return render_template('index.html', name=name)
#route to feedback page
@app.route('/feedback')
def feedback_page():
    return render_template('feedback.html')  


if __name__ == '__main__':
    app.run(debug=True)