from app import db

class Person(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.Text, nullable=False)
    lastName = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    role = db.Column(db.Text)

    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"