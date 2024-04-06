from flask import render_template, request
from models import Person

def register_routes(app, db):

    @app.route('/')
    def index():
        person = Person.query.all()
        return str(person)