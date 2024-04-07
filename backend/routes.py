from flask import render_template, request
from models import Student

def register_routes(app, db):

    @app.route('/')
    def index():
        user = Student.query.all()
        return str(user)
    
    @app.route('/home_test')
    def home_test():
        return render_template('base.html') #home_test.html
    
    @app.route('/home')
    def home():
        return render_template('home.html')


    @app.route('/test_file')
    def test_file():
        return render_template('test_file.html')