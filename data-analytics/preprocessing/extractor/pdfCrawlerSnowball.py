from string import punctuation
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import TreebankWordTokenizer

tokenizer = TreebankWordTokenizer()

# 불용어 삭제
def remove_stopwords(list):
    stop_words = stopwords.words("english")
    stop_words.remove("not")
    new_list = [word for word in list if word not in stop_words]

    return new_list


# 특수문자 제거
def remove_special_character(script):
    for p in punctuation:
        script = script.replace(p, "")
    script = script.replace("—", "")
    return script


# 어퍼스트로피 단어 삭제
def remove_apostrophe_word(scripts):
    res = []
    for word in scripts:
        if not "’" in word:
            res.append(word)
    return res


with open("the-secret-life-of-pets-2016.txt") as f:
    scripts = []
    script = ""
    ck = False
    for line in f:
        line = line.strip().replace("\n", "")
        if line.isupper() and line.startswith("SNOWBALL"):
            ck = True
            continue
        elif line.isupper() or line == "The Secret Life of Pets" or line.isdigit():
            ck = False
            if len(script) > 0:
                script = script.strip().lower()
                script = remove_special_character(script)
                scripts += tokenizer.tokenize(script)
                script = ""
        if ck:
            script += line + " "
    scripts = remove_stopwords(scripts)
    scripts = remove_apostrophe_word(scripts)
    print(scripts)

with open("Snowball.txt", "w") as f:
    f.write(" ".join(scripts))
