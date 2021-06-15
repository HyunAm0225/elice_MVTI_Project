import nltk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from collections import Counter
from wordcloud import WordCloud
from nltk.sentiment.vader import SentimentIntensityAnalyzer 
from nrclex import NRCLex
from sklearn.preprocessing import MinMaxScaler
from preprocessing.data import (
    Hans,
    HarleyQuinn,
    Jigsaw,
    Joker,
    Fletcher,
    Snowball,
    Plankton,
    Vader,
    Thanos,
    HannibalLecter,
    JimMoriarty,
    Scar
)

# nltk.download('vader_lexicon')
# nltk.download('punkt')
sid = SentimentIntensityAnalyzer()


# vader score를 구해서 단어 별 점수를 딕셔너리 형식으로 저장 
def get_vader_score(words):
    word_dict = {}

    for word in words:
        ss = sid.polarity_scores(word)
        # for k in ss:
        #     print('{0}: {1}, '.format(k, ss[k]), end='')
        word_dict[word] = ss['compound']

    return word_dict


# 중립 단어를 제외하고 긍/부정적인 단어만 추출
def get_polar(data):
    polar_list = []

    for word, score in data.items():
        if score != 0:
            polar_list.append(word)

    return polar_list


# 단어의 구체적(라벨링된) 감정을 추출해서 리스트에 저장 
def classify_emotion(data):
    emotion_list = []

    for word in data:
        emotion = NRCLex(word)
        top_emo = emotion.top_emotions
        if top_emo[0][1] != 0.0:
            emotion_list.append(top_emo)

    return emotion_list


# 감정 별 수치를 모두 합산 
def sum_emotion(data):
    emotion_dict = {}

    for top_emo in data:
        for emo in top_emo:
            emotion = emotion_dict.get(emo[0])
            if not emotion:
                emotion_dict[emo[0]] = emo[1]
            else:
                emotion_dict[emo[0]] += emo[1]

    return emotion_dict


# 키워드 별 감정 사전을 반환 
def get_emotion_dict():
    FILES = {
        "Hans": Hans.words,
        "Fletcher": Fletcher.words,
        "Plankton": Plankton.words,
        "Snowball": Snowball.words,
        "HarleyQuinn": HarleyQuinn.words,
        "Jigsaw": Jigsaw.words,
        "Joker": Joker.words,
        "Vader": Vader.words,
        "Thanos": Thanos.words,
        "HannibalLecter": HannibalLecter.words,
        "JimMoriarty": JimMoriarty.words,
        "Scar": Scar.words
    }
    emotion_dict = {}

    for fn, words in FILES.items():
        word_dict = get_vader_score(words)
        polar_list = get_polar(word_dict)
        emotion_list = []

        for word in polar_list:
            emotion = NRCLex(word)
            emo = emotion.affect_dict
            if emo:
                emotion_list.append(emo)
        
        emotion_dict[fn] = emotion_list

    return emotion_dict


# 감정 별 키워드 수를 세기 위한 키워드 리스트를 만듦 
def creat_emotion_dict_for_counter(data):
    emotion_dict = {}

    for _, words in data.items():
        for emo_dict in words:
            for kw, emotions in emo_dict.items():
                for emotion in emotions:
                    temp = emotion_dict.get(emotion)
                    if temp:
                        emotion_dict[emotion].append(kw)
                    else:
                        emotion_dict[emotion] = []
                        emotion_dict[emotion].append(kw)

    return emotion_dict


# 감정 별 키워드 사전을 워드클라우드 이미지로 내보내기 
def create_word_cloud(data):
    for emotion, kws in data.items():
        counter = Counter(kws)
        cloud = WordCloud(background_color="white")
        cloud.fit_words(counter)
        cloud.to_file('{}.png'.format(emotion))


# emotion_dictionary = get_emotion_dict()
# create_word_cloud(creat_emotion_dict_for_counter(emotion_dictionary))

# 키워드 별 감정 사전을 파일로 내보내기 
def export_emotion_dict(data):
    output = open('characterEmotions.txt', 'a')
    output.write(str(data))
    output.close()
        

# export_emotion_dict(get_emotion_dict())

# 캐릭터별 감정 수치 그래프 그리기
def draw_graph(data, name):
    emotions = pd.DataFrame({
        'emotions': data
    })
    emo_values = emotions.to_numpy()
    # 0~1 사이의 값으로 정규화 
    # 방법 1. fit(data) -> transform(data)
    # 방법 2. fit_transform(data)
    scaler = MinMaxScaler().fit(emo_values)
    _data = scaler.transform(emo_values)
    emotions['emotions'] = _data

    fig, ax = plt.subplots(figsize=(8, 6))
    ax.bar(emotions.index, emotions['emotions'])
    plt.tight_layout()
    plt.title(name)
    fig.savefig(f'{name}_emotion_std.png',bbox_inches='tight')
    

def main():
    FILES = {
        "Hans": Hans.words,
        "Fletcher": Fletcher.words,
        "Plankton": Plankton.words,
        "Snowball": Snowball.words,
        "HarleyQuinn": HarleyQuinn.words,
        "Jigsaw": Jigsaw.words,
        "Joker": Joker.words,
        "Vader": Vader.words,
        "Thanos": Thanos.words,
        "HannibalLecter": HannibalLecter.words,
        "JimMoriarty": JimMoriarty.words
    }

    for fn, words in FILES.items():
        word_dict = get_vader_score(words)
        polar_list = get_polar(word_dict)
        emotion_list = classify_emotion(polar_list)
        emotion_dict = sum_emotion(emotion_list)
        draw_graph(emotion_dict, fn)


# main()
