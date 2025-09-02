from flask import Blueprint, request, jsonify, render_template
from app import db
from app.models import User
from app.utils.auth_helpers import hash_password, verify_password
from flask_jwt_extended import create_access_token

bp = Blueprint('auth', __name__, url_prefix='')
@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')  # Show the form

    data = request.form
    user = User(
        name=data['name'],
        email=data['email'],
        password=hash_password(data['password']),
        role=data['role']
    )
    db.session.add(user)
    db.session.commit()
    return jsonify({"msg": "User registered"}), 201
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')  # Show the form

    data = request.form
    user = User.query.filter_by(email=data['email']).first()
    if user and check_password(data['password'], user.password):
        return jsonify({"msg": "Login successful"}), 200
    return jsonify({"msg": "Invalid credentials"}), 401
