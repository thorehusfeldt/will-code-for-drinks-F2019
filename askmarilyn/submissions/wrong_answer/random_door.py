#!python3

import random

n = 3
rounds = 1000

for _ in range(rounds):
    doors = set(range(1, n + 1))
    first_choice = 1 + random.randrange(3)
    print (first_choice)
    assert input()
    hint = int(input().split()[-2])
    second_choice = 1 + random.randrange(3)
    print(second_choice)
    assert input() 
    assert input()





