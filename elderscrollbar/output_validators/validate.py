#!/usr/bin/python3
# usage: validate.py input_file answer_file feedback_dir < contestant_output

from sys import argv, stdin
from math import ceil

with open(argv[1], 'r') as inp:
    _, H, _, _ = map(int, inp.readline().split())

f_ans = open(argv[2], 'r')

LENCIENCY = .2 # accept thumb to be off by 20%, rounded up

ok = True
i = 0
thumbline = None
for line in stdin:
    if '|X|' in line:
        thumbline = i
        line = line.replace('|X|', '| |')
    
    ans_line = f_ans.readline()
    if not ans_line:
        print ('WA: output too long')
        exit(43)
    if '|X|' in ans_line:
        ans_thumbline = i
        ans_line = ans_line.replace('|X|', '| |')

    if line.strip() != ans_line.strip():
        ok = False
    i += 1

ok = ok and not f_ans.readline()
if not ok:
    print ('WA: window wrong')
    exit(43)
if thumbline is None:
    print ('WA: thumb missing')
    exit(43)
if abs(ans_thumbline - thumbline) > ceil( (H-2)*  LENCIENCY):
    print ('WA: thumb too far off')
    exit(43)

exit(42)


