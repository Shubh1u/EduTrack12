from flask import Blueprint, request, jsonify
from app import db
from app.models import User

bp = Blueprint('student', __name__, url_prefix='/student')

@bp.route('/<int:id>', methods=['GET'])
def get_student(id):
    student = User.query.get(id)
    if student:
        return jsonify(name=student.name, email=student.email, role=student.role)
    return jsonify({"msg": "Student not found"}), 404

@bp.route('/update/<int:id>', methods=['PUT'])
def update_student(id):
    data = request.json
    student = User.query.get(id)
    if student:
        student.name = data.get('name', student.name)
        db.session.commit()
        return jsonify({"msg": "Updated"})
    return jsonify({"msg": "Student not found"}), 404
