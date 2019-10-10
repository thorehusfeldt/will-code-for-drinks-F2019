#!/usr/bin/python
from sys import stdin
import sys
import re

pat = "(0|1|2) (0|1|2|3|4)"

line = stdin.readline()
assert re.match(pat, line)

line = stdin.readline()
assert len(line) == 0

# Nothing to report
sys.exit(42)
