from myblog import app



@app.route('/', methods=['GET', 'POST'])
def index():
    pass


@app.route('/login', methods=['GET', 'POST'])
def login():
    pass