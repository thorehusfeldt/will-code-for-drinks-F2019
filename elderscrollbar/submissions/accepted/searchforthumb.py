from sys import stdin, stdout
from fractions import Fraction

# searches linearly for thumb position in 0..H-2 that satisfies constraint

W, H, L, N = map(int, stdin.readline().split())
text = ' '.join([stdin.readline().strip() for _ in range(N)])
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
        
for widgetpos in range(H-2):
    if abs( Fraction(widgetpos, H - 2) - Fraction(L, len(typesettext) - H )) <= Fraction(1, H-2):
        break
else:
    assert False

print ('+' + '-' * W + '+-+')
for i in range(L , L + H):
    stdout.write('|')
    stdout.write (typesettext[i])
    stdout.write(' ' * (W - len(typesettext[i])) + '|')
    if i == L: 
        stdout.write('^')
    elif i == L + H - 1:
        stdout.write('v')
    elif i == L + widgetpos + 1:
        stdout.write('X')
    else:
        stdout.write(' ')
    stdout.write('|\n')

print ('+' + '-' * W + '+-+')


