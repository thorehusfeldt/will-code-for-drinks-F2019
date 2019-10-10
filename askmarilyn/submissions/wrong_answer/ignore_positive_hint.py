#!python3

# This is the rote "you must always take the remaining door" strategy that you may
# remember from having read about MH problen, ignoring
# that in this exercise, Marilyn actually may be helpful

import random

n = 3
rounds = 1000

for _ in range(rounds):
    doors = set('ABC')
    first_choice = random.choice('ABC')
    doors.remove(first_choice)
    print (first_choice)
    hint, bottle = input().split()
    if hint in doors:
        doors.remove(hint)
    second_choice = doors.pop()
    print(second_choice)
    line = input().split()
    assert int(line[0]) == int(second_choice == line[1])




