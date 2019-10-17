#!/usr/bin/python3
from sys import stdin
import sys
import re

integer = "(0|-?[1-9][0-9]*)"
monthname = "(JAN|FEB|MAR|APR|MAY|JUN|JUL|AUG|SEP|OCT|NOV|DEC)"
dayname = "(MON|TUE|WED|THU|FRI|SAT|SUN)"

MAX = 31

line = stdin.readline()
assert re.fullmatch(integer + " " + monthname + "\n", line), "'%s' is not a date" % line
d = int(line.split()[0])
assert 1 <= d <= MAX, "%s  not in [1, %s]" % (n, MAX)

line = stdin.readline()
assert re.fullmatch(dayname + "\n", line), "'%s' is not a weekday" % line

assert not stdin.readline()
# Nothing to report
sys.exit(42)
