from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///students.sqlite3'
app.config['SECRET_KEY'] = "random string"

db = SQLAlchemy(app)



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

@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/students', methods = ['POST'])
def add_stud():
    data = request.get_json()
    
 
    newStudent= students(data['name'],data['city'],data['addr'],data['pin'])
    db.session.add (newStudent)
    db.session.commit()
    return jsonify({"message": "new student is created"})


@app.route("/students", methods=["GET"])
def get_students():
    student_list = students.query.all()
    students_data = []
    for student in student_list:
        student_data = {
            'id': student.id,
            'name': student.name,
            'city': student.city,
            'addr': student.addr,
            'pin': student.pin
        }
        students_data.append(student_data)
    
    return jsonify(students_data)



@app.route('/students', methods = ['DELETE'])
def del_stud():
    
    return jsonify({"message": "new student is created"})


if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)

