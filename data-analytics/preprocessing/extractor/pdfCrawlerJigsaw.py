import itertools
import re

text = []
character = []
with open('saw.txt') as f:
    for line in f:
        text.append(line.replace('\n', '').replace('.', '').strip())
# print(text)
talk = []
character = []
for i in text:
    if i.isupper():
        name = i
        if len(talk) > 1:
            new_list = [name, talk]
            character.append(new_list)
            talk = []
    elif i == '' or (i.isupper() and i != name):
        new_list = [name, talk]
        character.append(new_list)
        talk = []
    else:
        talk.append(i)

jigsaw_text = [i[1] for i in character if i[0] == "JIGSAW"]

jigsaw_string = ' '.join(list(itertools.chain(*jigsaw_text))).replace('\t', '').replace('\n', '').replace('�', "'").replace('?', "").replace('!', '').strip()

p = re.compile("[^0-9]")
jigsaw_string = ''.join(p.findall(jigsaw_string))

with open("../data/jigsaw.txt", "w") as f:
    for i in jigsaw_string:
        i.replace('\t', '').replace('\n', '').replace('?', '').strip()
        f.write(i)
