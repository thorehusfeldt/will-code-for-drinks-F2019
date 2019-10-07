#!/usr/bin/python
from sys import stdin
import sys
import re

posinteger = "([1-9][0-9]*)"
nonnegintegerwithleadingzeros = "([0-9]*)"

line = stdin.readline()
assert re.match(posinteger + "\n", line), "'%s' is not an integer" % line
n = int(line)
assert 1000 >= n > 0, 'n out of range'
price = []
for i in range(n):
    line = stdin.readline()
    assert re.match(nonnegintegerwithleadingzeros + "\n", line), "'%s' is not an integer" % line
    p = int(line)
    assert len(line.strip()) <= 10, 'magnet too long in line %d' % i
    price.append(line.strip())

assert (int(''.join(price)) > 0)

assert not stdin.readline(), 'extra input'
# Nothing to report
sys.exit(42)
