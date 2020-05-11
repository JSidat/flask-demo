from flask import render_template
from application import app
from application.models import Posts

@app.route('/')
@app.route('/home')
def home():
    postData = Posts.query.first()
    return render_template('home.html', title='Home Page', post=postData)
