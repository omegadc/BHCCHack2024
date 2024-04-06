from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/')
    def index():
        person = Person.query.all()
        return str(person)
    
    @app.route('/home_test')
    def home_test():
        return render_template('home_test.html')
    
    @app.route('/home')
    def home():
        return render_template('home.html')


    @app.route('/test_file')
    def test_file():
        return render_template('test_file.html')