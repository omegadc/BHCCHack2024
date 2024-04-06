from app import db
    
class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, nullable=False)
    firstName = db.Column(db.Text, nullable=False)
    lastName = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phoneNumber = db.Column(db.Text)
    def __repr__(self):
        return f"Student full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class Event(db.Model):
    __tablename__ = 'event'
    id = db.Column(db.Integer, primary_key=True)
    eventID = db.Column(db.Integer, primary_key=True, nullable=False)
    Name = db.Column(db.Text, nullable=False)
    # Date = db.Column(db.Datetime, nullable=False)
    Location = db.Column(db.Text,nullable=False)
    Description = db.Column(db.Text)

    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class RSVP(db.Model):
    __tablename__ = 'rsvp'
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    eventID = db.Column(db.Integer, primary_key=True, nullable=False)
    rsvpStatus = db.Column(db.Text, nullable=False)
    # rsvpDate = db.Column(db.Datetime, nullable=False)

    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class Attendance(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    studentID=db.Column(db.Integer, foreign_key=True, nullable=False)
    eventID=db.Column(db.Integer, foreign_key=True, nullable=False)
    status=db.Column(db.Boolean)
    # date=db.Column(db.Datetime,nullable=False)
    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class Advisor(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    firstName = db.Column(db.Text, nullable=False)
    lastName = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phoneNumber = db.Column(db.Text)
    department = db.Column(db.Text)
    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class AppointmentID(db.Model):
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    studentID=db.Column(db.Integer, foreign_key=True, nullable=False)
    AdvisorID=db.Column(db.Integer, foreign_key=True, nullable=False)
    # date=db.Column(db.Datetime, nullable=False)
    status=db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"User full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"
