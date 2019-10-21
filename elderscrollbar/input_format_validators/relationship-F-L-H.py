#!/usr/bin/python3
'''
Checks that F <= L - H and  H < L, where F and H are given in the input
and L is the length of the (aligned) text.
'''
from sys import stdin
import sys
import re

W, H, F, N = map(int, input().split()) 

textlines = []
for i in range(N):
    line = stdin.readline()
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
sys.exit(42)
