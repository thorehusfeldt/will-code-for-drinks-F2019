#!/usr/bin/python3
from sys import stdout
from math import ceil
W, H, L, N = map(int, input().split())
text = ' '.join([input().strip() for _ in range(N)])
words = text.split()
i = 0
typesettext = list()
line = ""
while i < len(words):
    next_word = words[i]
    if len(line) == 0 and len(next_word) > W:
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

print ('+' + '-' * W + '+-+')
for i in range(L , L + H):
    stdout.write('|')
    stdout.write (typesettext[i])
    stdout.write(' ' * (W - len(typesettext[i])) + '|')
    if i == L: 
        stdout.write('^')
    elif i == L + H - 1:
        stdout.write('v')
    elif i - L - 1 == L // ceil(len(typesettext)/(H-2)):
        stdout.write('X')
    else:
        stdout.write(' ')
    stdout.write('|\n')

print ('+' + '-' * W + '+-+')




