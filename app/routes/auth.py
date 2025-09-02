from flask import Blueprint, request, jsonify
from app import db
from app.models import User
from app.utils.auth_helpers import hash_password, verify_password
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.json
    user = User(name=data['name'], email=data['email'],
                password=hash_password(data['password']),
                role=data['role'])
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered"}), 201

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(email=data['email']).first()
    if user and verify_password(data['password'], user.password):
        token = create_access_token(identity=user.id)
        return jsonify(access_token=token)
    return jsonify({"msg": "Invalid credentials"}), 401
