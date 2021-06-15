import requests
from bs4 import BeautifulSoup
import json
import os

# 겨울왕국 - 한스(HANS)
req = requests.get('https://imsdb.com/scripts/Frozen-(Disney).html/')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
script = soup.select_one('.scrtext > pre')

# bs4 객체 type casting
script = str(script)

# 각 대사 별로 자르기 (인물 이름 포함)
raw_lines = script.split("<b>")

# 공백 제거한 대사 리스트
strip_line = []

for rl in raw_lines:
    strip_line.append(rl.strip())

# [[인물, 대사],[인물,대사]...] 형식으로 2차원 배열
role_line_list = []

for sl in strip_line:
    temp = sl.split("</b>")
    role_line_list.append(temp)

# 인물(l[0])이'HANS'인 대사(l[1])를 찾은 다음, 대사에 섞인 나레이션 제거
lines = []

for l in role_line_list:
    if l[0].startswith("HANS"):
        line = l[1].split('\r\n\r\n')
        lines.append(line[0].replace("\n","").replace("\r","").replace(".","").replace(",","").replace("?","").replace("-","").replace("!","").strip().lower())
# print(lines)

# 개별 단어 추출
remove_blank = []

string = ' '.join(lines)
string = string.split(' ')

for s in string:
    if s != '' and s[0]!="(" and s[-1]!=")":
        if "'"in s:
            k = s.split("'")
            remove_blank.append(k[0])
        else:
            remove_blank.append(s)

final = " ".join(remove_blank)
output = open('Hans.txt', 'w', encoding='utf-8')
output.write(final)
output.close()
