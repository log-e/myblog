from myblog import app, db
from flask import render_template, request, url_for, redirect, flash
from flask_login import login_user, login_required, logout_user, current_user
from .models import User, Article


@app.route('/')
def index():
    #todo
    allarticle = Article.query.all()
    return render_template('index.html', allarticle = allarticle)


@app.route('/article/delete/<int:article_id>')
@login_required
def delete_article(article_id):
    article = Article.query.get_or_404(article_id)
    db.session.delete(article)
    db.session.commit()
    flash("delete article success")
    return redirect(url_for("admin"))


@app.route('/article/view/<int:article_id>')
def view_article(article_id):
    article = Article.query.get(article_id)
    return render_template('article.html', article = article)


@app.route('/article/edit/<int:article_id>', methods = ['GET', 'POST'])
@login_required
def edit_article(article_id):
    """ 编辑已有的文章 """
    article = Article.query.get(article_id)
    if request.method == "POST":
        title = request.form['title']
        content = request.form['content']
        article.title = title
        article.content = content
        db.session.commit()
        flash("edit successfully!")
        allarticle = Article.query.all()
        return redirect(url_for("admin"))
    return render_template("edit.html", article = article)


@app.route('/article/post', methods=['GET','POST'])
@login_required
def post_article():
    """ 发布新文章 """
    if request.method == 'POST':
        title = request.form['title']
        content = request.form['content']
        if not title or not content:
            flash('Empty article')
            redirect(url_for('post_article'))
        article = Article(title=title, content = content)
        db.session.add(article)
        db.session.commit()
        flash('Article create successfully!')
        return redirect(url_for('admin'))


@app.route('/admin')
@login_required
def admin():
    """ 管理员页面，可以编辑旧文章，发布新文章，删除旧文章 """
    allarticle = Article.query.all()
    return render_template('admin.html', allarticle = allarticle)


@app.route('/login', methods=['GET', 'POST'])
def login():
    """ 登录 admin 页面 """
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
            return redirect(url_for('admin'))
        
        flash('Invalid username or password.')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    flash('GoodBye.')
    return redirect(url_for('index'))