import pandas as pd
import numpy as np
from numpy import dot
from numpy.linalg import norm
from nrclex import NRCLex
from sklearn.preprocessing import MinMaxScaler


def classify_emotion(data):
    emotion_list = []

    for word in data:
        emotion = NRCLex(word)
        top_emo = emotion.top_emotions
        if top_emo[0][1] != 0.0:
            emotion_list.append(top_emo)

    return emotion_list


def sum_emotion(data):
    emotion_dict = {
        'anger': 0.0,
        'anticipation': 0.0,
        'disgust': 0.0,
        'fear': 0.0,
        'joy': 0.0,
        'negative': 0.0,
        'positive': 0.0,
        'sadness': 0.0,
        'surprise': 0.0,
        'trust': 0.0,
    }

    for top_emo in data:
        for emo in top_emo:
            emotion_dict[emo[0]] += emo[1]

    return emotion_dict


def standardize_data(data):
    emotions = pd.DataFrame({
        'emotions': data
    })
    emo_values = emotions.to_numpy()
    scaler = MinMaxScaler().fit(emo_values)
    _data = scaler.transform(emo_values)
    emotions['emotions'] = _data

    return emotions


def format_data(dataset):
    words = classify_emotion(dataset)
    emotion_sum = sum_emotion(words)
    std_df = standardize_data(emotion_sum)

    return std_df


def calculate_cos_sim(a, b):
    return dot(a, b)/(norm(a)*norm(b))
