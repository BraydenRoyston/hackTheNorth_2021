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

# from sklearn.metrics.pairwise import cosine_similarity
# import gensim  
# word2vec_model = gensim.models.Doc2Vec.load('saved_word2vec_model')  

# def avg_sentence_vector(words, model, num_features, index2word_set):
#     #function to average all words vectors in a given paragraph
#     featureVec = np.zeros((num_features,), dtype="float32")
#     nwords = 0

#     for word in words:
#         if word in index2word_set:
#             nwords = nwords+1
#             featureVec = np.add(featureVec, model[word])

#     if nwords>0:
#         featureVec = np.divide(featureVec, nwords)
#     return featureVec

# def get_semantic_similarity(sentence_1,sentence_2):
#     #get average vector for sentence 1
#     sentence_1 = "this is sentence number one"
#     sentence_1_avg_vector = avg_sentence_vector(sentence_1.split(), model=word2vec_model, num_features=100)

#     #get average vector for sentence 2
#     sentence_2 = "this is sentence number two"
#     sentence_2_avg_vector = avg_sentence_vector(sentence_2.split(), model=word2vec_model, num_features=100)

#     sen1_sen2_similarity =  cosine_similarity(sentence_1_avg_vector,sentence_2_avg_vector)


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

def get_added_features(raw_data):
    repetition_score = get_repetition_score(raw_data['lyrics'])
    if repetition_score == None:
        return None

    return_value:dict = {
        "repetitionScore": repetition_score
    }

    return return_value



def fill_preprocessed(client):
    db = client['htn']
    raw_datas_collection = db['rawDatas']

    processed_data_collection = db['processedData']

    processed_data_collection.delete_many({})

    raw_datas = raw_datas_collection.find({})

    for raw_data in raw_datas:
        added_features = get_added_features(raw_data)

        if added_features == None:
            continue

        processed_data_collection.insert_one({
            **added_features,
            "isGoodSong": raw_data['isGoodSong'],
            "lyrics": raw_data['lyrics'],
            "artist": raw_data['artist'],
            "song": raw_data['song']
        })
