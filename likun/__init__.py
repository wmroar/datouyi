from .bootstrap import bootstrap
from factory import create_app
from flask import redirect,url_for



app = create_app(__name__,'config.py')
bootstrap(app)

@app.route('/')
def index():
    return  redirect(url_for('common',filename='/',_external=True))