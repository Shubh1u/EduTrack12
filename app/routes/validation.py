from flask import Blueprint, request, jsonify
from app import db
from app.models import Achievement

bp = Blueprint('validation', __name__, url_prefix='/validate')

@bp.route('/<int:achievement_id>', methods=['PUT'])
def validate_achievement(achievement_id):
    data = request.json
    ach = Achievement.query.get(achievement_id)
    if ach:
        ach.status = data['status']
        db.session.commit()
        return jsonify({"msg": "Status updated"})
    return jsonify({"msg": "Achievement not found"}), 404
