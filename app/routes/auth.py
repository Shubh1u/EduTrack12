from flask import Blueprint, render_template, request, redirect, url_for, flash
from app import db
from app.models import User
from app.utils.auth_helpers import hash_password, verify_password

bp = Blueprint('auth', __name__, url_prefix='')

@bp.route('/')
def index():
    return render_template('index.html')

@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        role = request.form.get('role', 'student')

        if not name or not email or not password:
            flash("All fields except role are required!", "error")
            return redirect(url_for('auth.register'))

        user = User(name=name, email=email, password=hash_password(password), role=role)
        db.session.add(user)
        db.session.commit()
        flash("Registration successful! Please log in.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')

@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')

        user = User.query.filter_by(email=email).first()
        if user and verify_password(password, user.password):
            flash(f"Welcome back, {user.name}!", "success")
            return redirect(url_for('auth.index'))
        else:
            flash("Invalid credentials", "error")
            return redirect(url_for('auth.login'))

    return render_template('login.html')
