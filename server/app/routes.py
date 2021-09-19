
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
dirname = os.path.dirname(__file__)

clf = load(os.path.join(dirname, './model.joblib')) 




@app.route("/", methods=['POST'])
def index():
    lyrics = request.json


    parameters_dict:dict = get_added_features(lyrics)

    print(parameters_dict.values())

    print(clf.predict_proba(list(parameters_dict.values())))

    return jsonify({"result": clf.predict_proba(clf.predict_proba(list(parameters_dict.values())))[0][1]})
