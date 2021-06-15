import os
from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer

path = "./data/"
file_list = os.listdir(path)
file_list_txt = [file for file in file_list if file.endswith(".txt")]  # 393개 파일
tokenizer = TreebankWordTokenizer()

# 불용어 삭제
def remove_stopwords(list):
    stop_words = stopwords.words("english")
    stop_words.remove("not")
    new_list = [word for word in list if word not in stop_words]

    return new_list


# 2글자 미만 단어 모두 제거
def remove_word_less_than_two(list):
    res = []
    for word in list:
        word = word.replace("'", "")
        if len(word) >= 3:
            res += [word]
    return res


# 행동 대사 삭제
def remove_action_script(script):
    while script.find("[") != -1 and script.find("]") != -1:
        s, e = script.find("["), script.find("]")
        script = script[:s] + script[e + 1 :]

    return script


# 특수문자 제거
def remove_special_character(script):
    for p in punctuation.replace("'", ""):
        script = script.replace(p, "")
    script = script.replace("—", "").replace("…", "").replace("♪", "")
    return script


def remove_number(scripts):
    return list(filter(lambda x: x.isalpha(), scripts))


scripts = []
for filename in file_list_txt:
    with open(path + filename) as f:
        for line in f:
            if ":" in line:
                lines = line.strip().split(":")
                if lines[0] == "Plankton":
                    script = lines[1].strip().lower()
                    script = remove_action_script(script)
                    script = remove_special_character(script)
                    scripts += tokenizer.tokenize(script)
        scripts = remove_stopwords(scripts)
        scripts = remove_word_less_than_two(scripts)
        scripts = remove_number(scripts)
# print(scripts)
with open("Plankton.txt", "w") as f:
    f.write(" ".join(scripts))
