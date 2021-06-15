from operator import itemgetter
from collections import Counter
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


def count_words(files):
    counts_dict = {}

    for name, words in files.items():
        counter = Counter(words)
        sorted_counter = sorted(counter.items(), key=itemgetter(1), reverse=True)
        counts_dict[name] = sorted_counter

    return counts_dict


def exporter():
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
    counts_dict = count_words(FILES)

    output = open('wordCounts.txt', 'a')
    output.write(str(counts_dict))
    output.close()

exporter()
