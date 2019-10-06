#!/usr/bin/python
from sys import stdin
import sys
import re

integer = "([1-9][0-9]*)"

MAX = 99

line = stdin.readline()
assert re.match(integer, line), "'%s' is not an integer" % line
d = int(line.split()[0])
assert 1 <= d <= MAX, "%s  not in [1, %s]" % (n, MAX)

line = stdin.readline()
assert re.match("[a-zA-Z]{1,20}" + "\n", line), "'%s' is not a valid beverage" % line

assert not stdin.readline()
# Nothing to report
sys.exit(42)
