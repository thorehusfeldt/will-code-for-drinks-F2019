#!/usr/bin/python3

import random

rounds = 1000
n = 3

for _ in range(rounds):
    doors = set('ABC')
    first_choice = random.choice('ABC')
    doors.remove(first_choice)
    print (first_choice)
    line = input().split()
    hint, bottle = line
    if bottle == '0':
        if hint in doors:
            doors.remove(hint)
        second_choice = doors.pop()
    else:
        second_choice = hint
    print(second_choice)
    assert input() 




