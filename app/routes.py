from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.models import db, User

main_bp = Blueprint('main_bp', __name__)

@main_bp.route('/')
def index():
    return render_template('index.html')

@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.password == password:
            flash('Login successful!', 'success')
            return redirect(url_for('main_bp.index'))
        else:
            flash('Invalid credentials', 'danger')
    return render_template('login.html')
