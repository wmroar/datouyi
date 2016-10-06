from .bootstrap import bootstrap
from factory import create_app



app = create_app(__name__,'config.py')
bootstrap(app)