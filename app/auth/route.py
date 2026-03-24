from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from functools import wraps

auth_bp = Blueprint('auth', __name__)

FAKE_USER = {
    'username': 'admin',
    'password': 'admin123'
}


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user' not in session:
            flash('Veuillez vous connecter pour accéder à cette page.', 'warning')
            return redirect(url_for('auth.login'))
        return f(*args, **kwargs)
    return decorated_function


@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session:
        return redirect(url_for('dashboard.index'))

    if request.method == 'POST':
        username = request.form.get('username', '').strip()
        password = request.form.get('password', '').strip()

        if username == FAKE_USER['username'] and password == FAKE_USER['password']:
            session['user'] = username
            flash(f'Bienvenue, {username} !', 'success')
            return redirect(url_for('dashboard.index'))
        else:
            flash('Identifiants incorrects.', 'danger')

    return render_template('auth/login.html')


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    flash('Vous avez été déconnecté.', 'info')
    return redirect(url_for('auth.login'))