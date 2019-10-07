#!/usr/bin/python
from sys import stdin
import sys
import re

integer = "([1-9][0-9]*)"

MAX = 10**9

line = stdin.readline()
assert re.match(integer + "\n", line), "First line must be single int" % line
n = int(line)
assert 1 <= n <= 10**6, "n out of range" 

line = stdin.readline().split()
assert len(line) == n, "2nd line must contain n values"
for val in line:
    assert re.match(integer, val), "'%s' is not an int" % val
    assert int(val), "int expected"

assert not stdin.readline()
# Nothing to report
sys.exit(42)
