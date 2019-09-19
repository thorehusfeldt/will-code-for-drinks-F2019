#!python3
N = int(input())
drink = input()

for i in range(N, 0, -1):
    print ('{} bottles of {} on the wall, {} bottles of {}.'.format(i, drink, i, drink))
    print ('Take one down, pass it around, {} bottles of {} on the wall.'.format(i-1, drink))
    print()
