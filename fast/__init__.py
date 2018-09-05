from flask import Flask

app = Flask(__name__) 
app.config['SECRET_KEY'] = 'fff'
app.config['SESSION_TYPE'] = 'filesystem'

from fast import api
from fast import models