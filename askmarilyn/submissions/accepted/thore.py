#!python3

import random

rounds = 1000
n = 3

for _ in range(rounds):
    doors = set(range(1, n + 1))
    first_choice = random.choice(list(doors))
    doors.remove(first_choice)
    print (first_choice)
    line = input().split()
    hint = int(line[-2])
    if line[2] == 'nothing':
        if hint in doors:
            doors.remove(hint)
        second_choice = random.choice(list(doors))
    else:
        second_choice = hint
    print(second_choice)
    assert input() in ["Enjoy your drink!", "Bad luck."]
    assert input()




