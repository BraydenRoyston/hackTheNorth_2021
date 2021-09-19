
from flask import Flask
from config import Config
import os

import time


app = Flask(__name__)
app.config.from_object(Config)

from . import routes
