import pymysql
from flask import Flask, render_template
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Thilak@2003',
    database='courses'
)

app = Flask(__name__)
app.static_folder = 'static'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text, nullable=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/courses', methods=['GET'])
def get_courses():
    courses = Course.query.all()
    course_list = [{'id': course.id, 'title': course.title, 'description': course.description} for course in courses]
    return jsonify(course_list)

@app.route('/course/<int:course_id>', methods=['GET'])
def get_course(course_id):
    course = Course.query.get(course_id)
    if course:
        return jsonify({'id': course.id, 'title': course.title, 'description': course.description})
    else:
        return jsonify({'error': 'Course not found'}), 404

@app.route('/course', methods=['POST'])
def create_course():
    data = request.get_json()
    if 'title' in data:
        course = Course(title=data['title'], description=data.get('description'))
        db.session.add(course)
        db.session.commit()
        return jsonify({'message': 'Course created successfully'}), 201
    else:
        return jsonify({'error': 'Invalid input'}), 400

@app.route('/course/<int:course_id>', methods=['PUT'])
def update_course(course_id):
    course = Course.query.get(course_id)
    if course:
        data = request.get_json()
        if 'title' in data:
            course.title = data['title']
        if 'description' in data:
            course.description = data['description']
        db.session.commit()
        return jsonify({'message': 'Course updated successfully'})
    else:
        return jsonify({'error': 'Course not found'}), 404

@app.route('/course/<int:course_id>', methods=['DELETE'])
def delete_course(course_id):
    course = Course.query.get(course_id)
    if course:
        db.session.delete(course)
        db.session.commit()
        return jsonify({'message': 'Course deleted successfully'})
    else:
        return jsonify({'error': 'Course not found'}), 404

if __name__ == '__main__':
    with app.app_context():
        app.run(debug=True)