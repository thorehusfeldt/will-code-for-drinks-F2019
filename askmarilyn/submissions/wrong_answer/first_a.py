#!/usr/bin/env python3
import random

for _ in range(1000):
    print("A")
    door, what = input().split()
    if what == "1":
        print(door)
    else:
        door = random.choice(list(set("ABC") - set(door)))
        print(door)
    input()
