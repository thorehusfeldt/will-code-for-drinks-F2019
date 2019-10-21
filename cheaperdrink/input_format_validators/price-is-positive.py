#!/usr/bin/python3
import sys
assert(input())
assert sum(int(line) for line in sys.stdin) > 0, 'total price must be positive.'
# Nothing to report
sys.exit(42)
