import requests
import re
import json
import os
from bs4 import BeautifulSoup

pattern = "{.*}|\[.*\]"

# 겨울왕국 - 한스(HANS)
req = requests.get('https://transcripts.fandom.com/wiki/The_Lion_King')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
# script = soup.select_one('.scrtext > pre')
script = soup.select_one('#mw-content-text > div')

# bs4 객체 type casting
script = str(script)
script = re.sub(pattern, "", script)

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
    if l[0].startswith("Scar"):
        line = l[1].split('\r\n\r\n')
        lines.append(line[0].replace("\n","").replace("\r","").replace("?","").replace(".","").strip())

# 개별 단어 추출
remove_blank = []

string = ' '.join(lines)
string = string.split(' ')

for s in string:
    if s != '' and s[0]!="(" and s[-1]!=")":
        remove_blank.append(s)


def exporter(filename):
    output = open(filename, 'w')
    output.write(str(remove_blank))
    output.close()
