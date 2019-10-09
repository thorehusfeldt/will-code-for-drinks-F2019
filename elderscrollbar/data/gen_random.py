from random import randrange, seed
from textwrap import wrap, fill
import sys, getopt

MAXWORDLENGTH = 80
try:
    opts, args = getopt.getopt(sys.argv[1:], "W:H:L:F:S:T:")
except getopt.GetoptError as err:
    print (str(err))
    sys.exit(2)

W = randrange(3,201)
F = L = None
S = 0

for o, a in opts:
    if o == '-W':
        W = int(a)
    if o == '-H':
        H = int(a)
    if o == '-L':
        L = int(a)
    if o == '-F':
        F = int(a)
    if o == '-T':
        T = int(a)
    if o == '-S':
        S = int(a)
seed(S)
assert L is not None
if F is None and T is None:
    F = randrange(L-H)
if F is None and T is not None:
    assert 0 <= T < H - 2
    F = round ((T * (L - H)) / (H - 3))
if H is None:
    H = randrange(3, min(L, 201))
assert 0 <= F <= L - H
assert H < L
assert 3 <= H <= 200
assert 3 <= W <= 200

# generate plenty of random text:
random_words = []
sz = 0
while sz < W * L:
    if randrange(10): # most words are short-ish
        wlen = randrange(9)
    else:
        wlen = randrange(randrange(9, 80)) # some are really long
    word = ''.join([chr(randrange(ord('a'), ord('z') + 1)) for _ in range(wlen)])
    word = chr(randrange(ord('A'), ord('Z') + 1) + (32 if randrange(10) else 0)) + word
    assert 0 < len(word) <= MAXWORDLENGTH
    random_words.append(word)
    sz += min(len(word), W)

text = ' '.join(random_words)
wrappedW =  wrap(text, W, break_long_words = False)  
assert L <= len(wrappedW)
wrappedW = wrappedW[:L]

wrapped80 = wrap( ' '.join(wrappedW), 80)
print (W, H, F, len(wrapped80))
print ('\n'.join(wrapped80))
