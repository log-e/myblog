from myblog import app


@app.errorhandler(404)
def handle_404(e):
    pass


@app.errorhandler(503)
def handle_503(e):
    pass