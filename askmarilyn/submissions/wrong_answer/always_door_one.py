#!python3

import random

n = 3
rounds = 1000

for _ in range(rounds):
    doors = set(range(1, n + 1))
    first_choice = 1 
    doors.remove(first_choice)
    print (first_choice)
    assert input()
    second_choice = 1 
    print(second_choice)
    assert input()
    assert input()





