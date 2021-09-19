
from flask.helpers import url_for
from flask import Flask, request, jsonify
from werkzeug.urls import url_parse
from datetime import datetime
from flask import jsonify
from . import app
from os.path import abspath

from joblib import dump, load
import os
dirname = os.path.dirname(__file__)

clf = load(os.path.join(dirname, './model.joblib')) 



import re
import functools
import tensorflow as tf
import nltk
from typing import List, Set, Dict, Tuple, Optional
from functools import reduce
from collections import Counter
from statistics import mean
import os
import numpy as np


def split_into_lines(lyrics: str) -> List[str]:
    lines: List[str] = lyrics.splitlines()

    result: List[str] = []

    for line in lines:
        if line != "":
            result.append(str(line))

    return result


def filter_out_non_important(lyrics: str):

    tokens = nltk.word_tokenize(lyrics)

    filtered_tokens = []

    for token in nltk.pos_tag(tokens):

        if(re.match("[a-z|A-Z|0-9]*'", token[0])):
            continue

        if(re.match("[a-z|A-Z|0-9]*[eE]mbed", token[0])):
            continue

        if(token[0] == "[" or token[0] == "]"):
            continue

        if (token[1] == "NN" or
            token[1] == "RB" or
            token[1] == "VB"
            ):
            filtered_tokens.append(token[0])

    return " ".join(str(x) for x in filtered_tokens)


# excludes non {noun, verb, adjective}
def get_repetition_score(lyrics: str):
    
    lines = split_into_lines(str(lyrics))

    for index,line in enumerate(lines):
        lines[index] =  filter_out_non_important(line)
    

    if len(lines) == 0:
        return None

    tokenizer = tf.keras.preprocessing.text.Tokenizer(
        num_words=None,
    )

    tokenizer.fit_on_texts(lines)

    tfidf_matrix = tokenizer.texts_to_matrix(lines, mode='tfidf')

    return np.average(tfidf_matrix)


def get_features(lyrics):
    repetition_score = get_repetition_score(lyrics)

    if repetition_score == None:
        return None

    
    return np.array([[repetition_score]])


@app.route("/", methods=['POST'])
def index():
    lyrics = request.json


    parameter = get_features(lyrics)

    print(clf.predict_proba(parameter))

    return jsonify({"result": clf.predict_proba(parameter)[0][1]})
