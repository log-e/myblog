from myblog import app
from flask import render_template

@app.errorhandler(404)
def handle_404(e):
    return render_template('errors/404.html'), 404
