import re
import nltk
from string import punctuation
from nltk.corpus import stopwords

# nltk.download("stopwords")


def find_start(line):
    for word in line:
        if word.startswith("("):
            start = line.index(word)
            break
    
    return start


def find_end(line, start):
    for word in line:
        if ")" in word:
            end = start + line.index(word)
            break
    
    return end


def get_sliced_line(line):
    start = find_start(line)
    
    if ")" in line[start]:
        line = line[:start] + line[start+1:]
    else:
        end = find_end(line[start:], start)
        line = line[:start] + line[end+1:]
    
    return line


# 행동 지문 삭제하기 
def remove_parenthese(line):
    line = line.split()
    parentheses = [word for word in line if "(" in word]

    for paren in range(len(parentheses)):
        line = get_sliced_line(line)

    return line


# 파일 가져오기
def get_files():
    file_list = {}
    file_names = ["Hans", "Fletcher", "Plankton", "Snowball", "HarleyQuinn", "Jigsaw", "Joker"]

    for fn in file_names:
        with open(f'data-analytics/preprocessing/data/{fn}.txt') as lines:
            lines = list(lines)[0]
            lines = remove_parenthese(lines)
            file_list[fn] = lines

    return file_list


# 소문자로 만들기
def lower_words(list):
    new_words = []

    for word in list:
        if len(word) > 2:
            new_words.append(word.lower())

    return new_words


# 불용어 삭제
def remove_stopwords(list):
    stop_words = stopwords.words("english")
    stop_words.remove('not')
    new_list = [word for word in list if word not in stop_words]
    return new_list


# 태그 비롯해서 행동 지문 삭제
def remove_tags(list):
    pattern = "<.*>"
    new_list = []

    for word in list:
        new_word = re.sub(pattern, "", word)
        new_list.append(new_word)

    return new_list


def remove_punc(word):
    for p in punctuation:
        word = word.replace(p,"")
    return word


# 특수문자 및 구두점 삭제 
def remove_extra(list):
    new_list = []

    for word in list:
        new_word = remove_punc(word)
        new_list.append(new_word)
    
    return new_list


# 축약어의 앞부분(명사)만 가져오기
def split_aux(list):
    new_list = []

    for word in list:
        if "'" in word:
            set = word.split("'")
            if len(set[0]) > 2:
                new_list.append(set[0])
        elif "’" in word:
            set = word.split("’")
            if len(set[0]) > 2:
                new_list.append(set[0])
        else:
            new_list.append(word)

    return new_list


# file로 export하기
def exporter():
    file_list = get_files()

    for name, words in file_list.items():
        filename = name
        words_wo_aux_verbs = split_aux(words)
        extra_removed_list = remove_extra(words_wo_aux_verbs)
        lowered_words = lower_words(extra_removed_list)
        words_wo_stopwords = remove_stopwords(lowered_words)
        
        output = open(f'{filename}.py', 'a')
        data = str(words_wo_stopwords)
        output.write(f'words = {data}')
        output.close()


# exporter()
