import re
import tensorflow as tf
import functools
import nltk
from typing import List, Set, Dict, Tuple, Optional
from functools import reduce
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
from statistics import mean
import os
import numpy as np


def split_into_lines(lyrics: str) -> List[str]:
    lines: List[str] = lyrics.splitlines()

    result: List[str] = []

    for line in lines:
        if line != "":
            result.append(line)

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

    lyrics =  filter_out_non_important(lyrics)
    lines = split_into_lines(str(lyrics))

    if len(lines) == 0:
        return None

    tokenizer = tf.keras.preprocessing.text.Tokenizer(
        num_words=None,
    )

    tokenizer.fit_on_texts(lines)

    tfidf_matrix = tokenizer.texts_to_matrix(lines, mode='tfidf')

    return np.average(tfidf_matrix)

def get_added_features(raw_data) -> dict:
    repetition_score = get_repetition_score(str(raw_data))
    if repetition_score == None:
        return None

    return {
        "repetitionScore": repetition_score
    }


