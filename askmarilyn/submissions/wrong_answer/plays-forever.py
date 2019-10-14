#!/usr/bin/python3

import random
from sys import stderr

rounds = 1000
n = 3

while (True):
    doors = set('ABC')
    first_choice = random.choice('ABC')
    doors.remove(first_choice)
    print (first_choice)
    stderr.write(str(first_choice) + '\n')
    hint, bottle = input().split()
    if bottle == '0':
        if hint in doors:
            doors.remove(hint)
        second_choice = doors.pop()
    else:
        second_choice = hint
    print(second_choice)
    line = input().split()
    assert int(line[0]) == int(second_choice == line[1])




