from flask import Blueprint, jsonify
from app.models import User, Achievement
from app.utils.pdf_generator import generate_portfolio

bp = Blueprint('portfolio', __name__, url_prefix='/portfolio')

@bp.route('/<int:student_id>', methods=['GET'])
def generate(student_id):
    student = User.query.get(student_id)
    achievements = Achievement.query.filter_by(student_id=student_id).all()
    filename = generate_portfolio(student, achievements)
    return jsonify({"msg": "Portfolio generated", "file": filename})
