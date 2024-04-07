from flask import render_template, request
from models import Student

def register_routes(app, db):

    @app.route('/', methods=['GET','POST'])
    def index():
        if request.method == 'GET':
            user = Student.query.all()
            return render_template('index.html', users=user)
        elif request.method == 'POST':
            # id = request.form.get('id')
            studentID = request.form.get('name')
            fName = request.form.get('firstName')
            lName = request.form.get('lastName')
            age = request.form.get('age')
            email = request.form.get('email')
            phonenum = request.form.get('phonenum')
            student = Student(firstName=fName,lastName=lName,
                              age=age,email=email,phoneNumber=phonenum)
            db.session.add(student)
            db.session.commit()
            user = Student.query.all()
            return render_template('index.html', users=user)

    
    @app.route('/home_test')
    def home_test():
        return render_template('base.html') #home_test.html
    
    @app.route('/home')
    def home():
        return render_template('home.html')


    @app.route('/test_file')
    def test_file():
        return render_template('test_file.html')