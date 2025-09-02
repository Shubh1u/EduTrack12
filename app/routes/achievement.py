from flask import Blueprint, request, jsonify
from app import db
from app.models import Achievement

bp = Blueprint('achievement', __name__, url_prefix='/achievement')

@bp.route('/add', methods=['POST'])
def add_achievement():
    data = request.json
    ach = Achievement(student_id=data['student_id'],
                      title=data['title'],
                      category=data['category'],
                      description=data['description'],
                      status='pending')
    db.session.add(ach)
    db.session.commit()
    return jsonify({"msg": "Achievement added"}), 201

@bp.route('/list/<int:student_id>', methods=['GET'])
def list_achievements(student_id):
    achievements = Achievement.query.filter_by(student_id=student_id).all()
    return jsonify([{
        "title": a.title,
        "category": a.category,
        "description": a.description,
        "status": a.status
    } for a in achievements])
