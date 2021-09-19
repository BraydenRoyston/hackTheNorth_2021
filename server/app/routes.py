
from flask.helpers import url_for
from flask import Flask, request, jsonify
from werkzeug.urls import url_parse
from datetime import datetime
from flask import jsonify
from . import app
from os.path import abspath
from .add_features import get_added_features
from joblib import dump, load
import os
from flask_cors import CORS, cross_origin
dirname = os.path.dirname(__file__)

clf = load(os.path.join(dirname, './model.joblib')) 



@cross_origin()
@app.route("/", methods=['POST'])
def index():
    lyrics = request.json['lyrics']

    parameters_dict:dict = get_added_features(lyrics)

    result = clf.predict_proba([list(parameters_dict.values())])[0][1]

    return jsonify({"result": result})
