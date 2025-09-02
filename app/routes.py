from flask import render_template, request, redirect, url_for, session
from app import app, db
from app.models import User, Student, Attendance, Marks
from flask import Blueprint, render_template

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    return render_template('index.html')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    # Add login logic here
    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    # Add register logic here
    return render_template('register.html')

@app.route('/dashboard')
def dashboard():
    # Add dashboard logic here
    return render_template('dashboard.html')
