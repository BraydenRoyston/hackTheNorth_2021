
from flask import Flask
from config import Config
import os

import time
from flask_cors import CORS, cross_origin

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'



app.config.from_object(Config)

from . import routes
