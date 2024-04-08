from app import db 
# from sqlalchemy import UniqueConstraint
from datetime import date
    
class Student(db.Model):
    __tablename__ = 'students'
    # id = db.Column(db.Integer, primary_key=True)
    StudentID = db.Column(db.Integer, primary_key=True, nullable=False, unique=True)
    firstName = db.Column(db.Text, nullable=False)
    lastName = db.Column(db.Text, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    email = db.Column(db.Text, nullable=False, unique=True)
    phoneNumber = db.Column(db.Text)
    # __table_args__ = (db.UniqueConstraint('StudentID','email'))

    def __repr__(self):
        return f"Student full name is {self.firstName} {self.lastName} and their email is {self.email}, their age is {self.age}"


class Event(db.Model):
    __tablename__ = 'events'
    id = db.Column(db.Integer, primary_key=True)
    eventID = db.Column(db.Integer, nullable=False)
    Name = db.Column(db.Text, nullable=False)
    # Date = db.Column(db.Datetime, nullable=False)
    Location = db.Column(db.Text,nullable=False)
    Description = db.Column(db.Text)
    #from datetime import Date
    def __repr__(self):
        return f"Event{self.eventID}: {self.Name} and the location {self.Location} with a Description: {self.Description}."


class RSVP(db.Model):
    __tablename__ = 'rsvp'
    id = db.Column(db.Integer, primary_key=True)
    studentID = db.Column(db.Integer, nullable=False)
    eventID = db.Column(db.Integer, nullable=False)
    rsvpStatus = db.Column(db.Text, nullable=False)
    # rsvpDate = db.Column(db.Datetime, nullable=False)

    def __repr__(self):
        return f"{self.studentID} send a status {self.rsvpStatus} for {self.eventID}."


class Attendance(db.Model):
    __tablename__ = 'attendance'
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    studentID=db.Column(db.Integer, nullable=False)
    eventID=db.Column(db.Integer, nullable=False)
    status=db.Column(db.Boolean)
    # date=db.Column(db.Datetime,nullable=False)
    def __repr__(self):
        return f"{self.studentID} is in {self.status} for {self.eventID}"

class Advisor(db.Model):
    __tablename__='advisors'
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    firstName = db.Column(db.Text, nullable=False)
    lastName = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    phoneNumber = db.Column(db.Text)
    department = db.Column(db.Text)
    def __repr__(self):
        return f"Advisor {self.id}: Full name: {self.firstName} {self.lastName}, Email: {self.email}, Department: {self.department}, PhoneNum: {self.phoneNumber}"


class AppointmentID(db.Model):
    __tablename__='appointments'
    id=db.Column(db.Integer, primary_key=True, nullable=False)
    studentID=db.Column(db.Integer, nullable=False)
    AdvisorID=db.Column(db.Integer, nullable=False)
    # date=db.Column(db.Datetime, nullable=False)
    status=db.Column(db.Text, nullable=False)
    def __repr__(self):
        return f"AppointmentID:{self.id} for StudentID:{self.studentID} and Advisor:{self.AdvisorID} with status:{self.status}"
