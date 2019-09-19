#!/usr/bin/python
from sys import stdin
import sys
import re

posinteger = "([1-9]\d*)"
nonnegintegerwithleadingzeros = "(\d*)"

line = stdin.readline()
assert re.match(posinteger + "\n", line), "'%s' is not an integer" % line
n = int(line)
assert 100000 >= n > 0, 'n out of range'
for i in range(n):
    line = stdin.readline()
    assert re.match(nonnegintegerwithleadingzeros + "\n", line), "'%s' is not an integer" % line
    p = int(line)
    assert p > 0, 'price must be nonzero in line %d' % i
    assert len(line.strip()) <= 10, 'price out of range in line %d' % i

assert not stdin.readline(), 'extra input'
# Nothing to report
sys.exit(42)
