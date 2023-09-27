from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"


db = SQLAlchemy(app)


@app.route('/')
def hello():
    return 'Hello, World!'

# model
class students(db.Model):
    id = db.Column('student_id', db.Integer, primary_key = True)
    name = db.Column(db.String(100))
    city = db.Column(db.String(50))
    addr = db.Column(db.String(200))
    pin = db.Column(db.String(10))


    def __init__(self, name, city, addr,pin):
        self.name = name
        self.city = city
        self.addr = addr
        self.pin = pin


# post - insert
@app.route('/student', methods= ["post"])
def add_student():
    data =request.json
    newStudent = students(data["name"], data["city"], data['address'], data['pin'])
    db.session.add(newStudent)
    db.session.commit()



if __name__ == '__main__':
    app.run(debug=True)
