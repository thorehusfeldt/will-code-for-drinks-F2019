#!/usr/bin/python
from sys import stdin
import sys
import re

integer = "(0|[1-9]\d*)"

line = stdin.readline()
assert re.match(integer + ' ' + integer + ' '  + integer + ' ' + integer +'\n', line), 'first line: expected four integers'
W, H, L, N = map(int, line.split())
assert 3 <= W <= 200
assert 3 <= H <= 200
assert 1 <= N <= 10**5

textlines = []
for i in range(N):
    line = stdin.readline()
    assert re.match('\w.*\w\n', line) or re.match('\w\n',line), i
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

assert L + H <= len(typesettext)

assert not stdin.readline()
# Nothing to report
sys.exit(42)
