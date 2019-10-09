#!/usr/bin/python
from sys import stdin
import sys
import re

integer = "(0|[1-9][0-9]*)"

line = stdin.readline()
assert re.match(integer + ' ' + integer + ' '  + integer + ' ' + integer +'\n', line), 'first line: expected four integers'
W, H, F, N = map(int, line.split())
assert 3 <= W <= 200
assert 3 <= H <= 200
assert 1 <= N <= 30000

textlines = []
for i in range(N):
    line = stdin.readline()
    assert re.match('[a-zA-Z].*[a-zA-Z]\n', line) or re.match('[a-zA-Z]\n',line), i
    assert len(line) <= 81
    textlines.append(line.strip())
text = ' '.join(textlines)
words = text.split()

i = 0
typesettext = list()
line = ""
while i < len(words):
    next_word = words[i]
    if len(line) == 0 and len(next_word) >= W:
        line += next_word[:W]
        i += 1
        continue
    if len(line) + len(next_word) + 1 <= W:
        line += (" " if len(line) > 0 else "") + next_word 
        i += 1
        continue
    else:
        typesettext.append(line)
        line = ""
if (line):
        typesettext.append(line)

assert 0 <= F <= len(typesettext) - H
assert H < len(typesettext)

assert not stdin.readline()
# Nothing to report
sys.exit(42)
