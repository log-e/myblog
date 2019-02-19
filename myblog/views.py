from myblog import app
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Article


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if not current_user.is_authenticated:
            return redirect(url_for('index'))
        title = request.form
    return render_template('index.html')


@app.route('/article/view/<int:article_id>')
def view_article(article):
    pass


@app.route('/article/edit/<int:article_id>')
@login_required
def edit_article(article):
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if not username or not password:
            flash('Invalid input')
            return redirect(url_for('login'))
        
        user = User.query.first()

        if username == user.username and user.check_password(password):
            login_user(user)
            flash('Login Success')
            return redirect(url_for('index'))
        
        flash('Invalid username or password.')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('GoodBye.')
    return redirect(url_for('index'))