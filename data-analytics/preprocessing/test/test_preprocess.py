from string import punctuation
from ..extractor import preprocessor


def test_remove_punctuation():
    list = ['hi"', ':', ',ss', 'dkso']
    pre_list = preprocessor.remove_extra(list)

    assert pre_list == ['hi', '', 'ss', 'dkso']


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


def test_remove_action():
    line = "(Shot the Tapp) Listen carefully, (ifyou) will There are rules (Lawrence on rules)"
    line = line.split()
    parentheses = [word for word in line if "(" in word]

    for paren in range(len(parentheses)):
        line = get_sliced_line(line)

    assert line == "Listen carefully, will There are rules".split()
