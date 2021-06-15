from collections import Counter
from wordcloud import WordCloud
from preprocessing.data import (
    Hans,
    HarleyQuinn,
    Jigsaw,
    Joker,
    Fletcher,
    Snowball,
    Plankton
) 


def create_word_cloud(words, name):
    counter = Counter(words)
    cloud = WordCloud(background_color="white")
    cloud.fit_words(counter)
    cloud.to_file('{}.png'.format(name))


def exporter():
    files = {
        "Hans": Hans.words,
        "Fletcher": Fletcher.words,
        "Plankton": Plankton.words,
        "Snowball": Snowball.words,
        "HarleyQuinn": HarleyQuinn.words,
        "Jigsaw": Jigsaw.words,
        "Joker": Joker.words
    }
    
    for name, words in files.items():
        create_word_cloud(words, name )

exporter()
