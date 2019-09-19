#!python3

import random

n = int(input())
rounds = int(input())

for _ in range(rounds):
    doors = set(range(1, n + 1))
    first_choice = random.choice(list(doors))
    doors.remove(first_choice)
    print (first_choice)
    assert input()
    hint = int(input().split()[-2])
    doors.remove(hint) # hint may be not in doors -> RTE
    second_choice = random.choice(list(doors))
    print(second_choice)
    assert input() in ["Here you go!", "Bad luck."]
    assert input()




