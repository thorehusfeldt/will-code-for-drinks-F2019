#!python3

import random

n = 3
rounds = 1000

for _ in range(rounds):
    doors = set(range(1, n + 1))
    first_choice = random.choice(list(doors))
    doors.remove(first_choice)
    print (first_choice)
    assert input()
    line = input().split()
    hint = int(line[-2])
    if hint in doors:
        doors.remove(hint)
    second_choice = random.choice(list(doors))
    print(second_choice)
    assert input() 
    assert input()




