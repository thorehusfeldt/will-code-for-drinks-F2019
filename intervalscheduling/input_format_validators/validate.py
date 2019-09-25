#!/usr/bin/python
from sys import stdin
import sys
import re

integer = "(0|-?[1-9]\d*)"

line = stdin.readline()
assert re.match(integer + "\n", line), "First line must be integer" % line
n = int(line)
assert 1<= n <= 10**5, 'n out of range'
for i in range(int(line)):
    line = stdin.readline()
    assert re.match(integer + " " + integer + "\n", line), "Syntax error" % line
    s, f = map(int, line.split())
    assert 0<= s <= 10**9, 's out of range'
    assert 0<= f <= 10**9, 'f out of range'
    assert s < f, 'intervals must be nonempty'

assert not stdin.readline()
# Nothing to report
sys.exit(42)
