#This is where the Flask app, pages, and feezer instances live.  

from flask import Flask 
from flask_flatpages import FlatPages
from flask_frozen import Freezer 

app = Flask(__name__) 
app.config.from_pyfile('settings.py')
pages = FlatPages(app)
feezer = Freezer(app)  