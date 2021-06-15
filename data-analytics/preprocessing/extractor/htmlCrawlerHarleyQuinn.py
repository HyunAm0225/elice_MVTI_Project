import requests
from bs4 import BeautifulSoup
import json
import os

# 버즈 오브 프레이 - 할리퀸
req = requests.get('https://www.the-editing-room.com/birds-of-prey.html')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
script = soup.select_one('#content > div:nth-child(2)')

# bs4 객체 type casting
script = str(script)

# 각 대사 별로 자르기 (인물 이름 포함, 행동 지문 포함)
raw_lines = script.split('<p class="character">')

target_lines = []

# MARGOT ROBBIE 로 시작하는 대사 필터링
for rl in raw_lines:
    if rl.startswith('MARGOT ROBBIE'):
        target_lines.append(rl)

# 개행에 따라 분리
target_lines_string = " ".join(target_lines)
target_lines = target_lines_string.split('\n')

dialogs = []

# 대사만 분리
for tl in target_lines:
    if tl.startswith('<p class="dialogue">'):
        dialogs.append(tl.replace('<p class="dialogue">',"").replace('</p>',"").replace("!","").replace(".","").replace("?","").replace(",","").replace("-","").lower().strip())

# 대사에서 단어 추출
total_words = []
for d in dialogs:
    temp = d.split(" ")
    total_words += temp

final_words = []
for t in total_words:
    if "'" in t:
        k = t.split("'")
        final_words.append(k[0])
    else:
        final_words.append(t)

final = " ".join(final_words)
output = open('HarleyQuinn.txt', 'w', encoding='utf-8')
output.write(final)
output.close()