from flask import Flask, jsonify, request
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teachers.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class Teacher(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(30))
    age = db.Column(db.Integer)
    salary = db.Column(db.Float)
    gender = db.Column(db.String(10))
    subject = db.Column(db.String(50))

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'age': self.age,
            'salary': self.salary,
            'gender': self.gender,
            'subject': self.subject
        }

with app.app_context():
    db.create_all()

@app.route('/api/teachers', methods=['GET'])
def get_all():
    teachers = Teacher.query.all()
    return jsonify([t.to_dict() for t in teachers])

@app.route('/api/teachers/<int:id>', methods=['GET'])
def get_by_id(id):
    teacher = Teacher.query.get_or_404(id)
    return jsonify(teacher.to_dict())

@app.route('/api/teachers', methods=['POST'])
def create():
    data = request.json
    teacher = Teacher(
        name=data['name'],
        title=data.get('title'),
        age=data.get('age'),
        salary=data.get('salary'),
        gender=data.get('gender'),
        subject=data.get('subject')
    )
    db.session.add(teacher)
    db.session.commit()
    return jsonify(teacher.to_dict()), 201

@app.route('/api/teachers/<int:id>', methods=['PUT'])
def update(id):
    teacher = Teacher.query.get_or_404(id)
    data = request.json
    teacher.name = data['name']
    teacher.title = data.get('title')
    teacher.age = data.get('age')
    teacher.salary = data.get('salary')
    teacher.gender = data.get('gender')
    teacher.subject = data.get('subject')
    db.session.commit()
    return jsonify(teacher.to_dict())

@app.route('/api/teachers/<int:id>', methods=['DELETE'])
def delete(id):
    teacher = Teacher.query.get_or_404(id)
    db.session.delete(teacher)
    db.session.commit()
    return '', 204

if __name__ == '__main__':
    app.run(port=8080, debug=True)
