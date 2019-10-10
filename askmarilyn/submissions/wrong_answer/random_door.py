#!python3

import random

n = 3
rounds = 1000

for _ in range(rounds):
    first_choice = chr(ord('A') + random.randrange(3))
    print (first_choice)
    assert (len(input().split()) == 2)
    second_choice = chr(ord('A') + random.randrange(3))
    print(second_choice)
    assert (len(input().split()) == 2)





