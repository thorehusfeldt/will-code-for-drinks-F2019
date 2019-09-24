from random import randrange, seed
import sys

seed(int(sys.argv[1]))
MAX = 10**5

W = randrange(3,201)
N = MAX

def adjust(words, width):
    i = 0
    typesettext = list()
    line = ""
    while i < len(words):
        next_word = words[i]
        if len(line) == 0 and len(next_word) >= width:
            line += next_word[:W]
            i += 1
            continue
        if len(line) + len(next_word) + 1 <= width:
            line += (" " if len(line) > 0 else "") + next_word 
            i += 1
            continue
        else:
            typesettext.append(line)
            line = ""

    if (line):
            typesettext.append(line)
    return typesettext

raw_text = []
for _ in range (100 * N):
    raw_text.append('x' * randrange(1,81))

adjusted_80_text = adjust(raw_text, 80)[:MAX]

T = len(adjust(' '.join(adjusted_80_text).split(), W))
assert (T>5)
H = randrange(3,min(201, T))
print (W, H, randrange(T-H), N)
print ('\n'.join(adjusted_80_text))
