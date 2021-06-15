import pdftotext
import itertools
import re

# pdf 파일 경로를 입력합니다..
file = open("./Whiplash.pdf", 'rb')
fileReader = pdftotext.PDF(file)
text = []
# pdf로 읽을 파일을 한줄씩 txt파일에 입력해줍니다.
with open("test.txt", "w") as f:
    for i in fileReader:
        i.replace('\t', '').replace('\n', '').strip()
        f.write(i)
# 캐릭터별 대사 분리
character = []
# 아까 저장한 txt파일 열기
with open('test.txt') as f:
    for line in f:
        if line == '':
            continue
        text.append(line.strip().replace('.', ''))
talk = []
# 첫 대사를 말하는 캐릭터는 직접 지정해줍니다..
text = text[text.index('ANDREW'):]

# 대화 처리
for word in text:
    if word.isupper() and len(talk) < 1:
        #         print(f"{word}일때 word.isupper()실행")
        name = word
        if len(talk) > 1:
            #             print(f"{word}일때 len(talk) > 1:실행")
            new_list = [name, talk]
            character.append(new_list)
            talk = []
    elif word == '' or (word.isupper() and word != name):
        #         print(f"{word}일때 word == '' or (word.isupper() and word != name): 실행")
        new_list = [name, talk]
#         print(f"테스트 {new_list}")
        character.append(new_list)
        if word.isupper():
            name = word
        talk = []
    else:
        #         print(f"{word}일때 else 실행")
        if name == word or name == "(MORE)":
            continue
        talk.append(word)
# 원하는 캐릭터 이름 넣기
fletcher_text = [i[1] for i in character if i[0] in "FLETCHER"]
# print(character)
fletcher_string = ' '.join(list(itertools.chain(*fletcher_text))).replace('\t', '').replace('\n', '').replace('?', '').replace('!', '').strip()
p = re.compile("[^0-9]")
fletcher_string = ''.join(p.findall(fletcher_string))


with open("../data/fletcher.txt", "w") as f:
    for i in fletcher_string:
        i.replace('\t', '').replace('\n', '').replace('?', '').strip()
        f.write(i)
