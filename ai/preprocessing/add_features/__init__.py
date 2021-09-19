import tensorflow as tf
import functools
import nltk
from typing import List, Set, Dict, Tuple, Optional
from functools import reduce
from collections import Counter
from nltk.sentiment import SentimentIntensityAnalyzer
from statistics import mean
import os


def split_into_lines(lyrics: str) -> List[str]:
    lines: List[str] = lyrics.splitlines()

    result: List[str] = []

    for line in lines:
        if line != "":
            result.append(line)

    return result


def get_avg_repetition_score(lyrics: str):

    lines = split_into_lines(lyrics)

    tokenizer = tf.keras.preprocessing.text.Tokenizer(
        num_words=None,
    )

    tokenizer.fit_on_texts(lines)

    tfidf_vec = tokenizer.texts_to_matrix(lines, mode='tfidf')

    metrics = tf.keras.metrics.CosineSimilarity(axis=-1)

    metrics.reset_states()

    metrics.update_state(*tfidf_vec)

    vector_similarity = metrics.result().numpy()

    print(vector_similarity)

    return vector_similarity


def add_features(client):
    db = client['htn']
    raw_datas_collection = db['rawDatas']

    raw_datas = raw_datas_collection.find({})

    for raw_data in raw_datas:
        repetition_score = get_repetition_score(raw_data['lyrics'])
