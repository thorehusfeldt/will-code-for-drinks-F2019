#!python3

# TLE: forgets to decrease 

N = int(input())
drink = input()

i = N
while i > 0:
    print ('{} bottles of {} on the wall, {} bottles of {}.'.format(i, drink, i, drink))
    print ('Take one down, pass it around, {} bottle{} of {} on the wall.'.format(i-1, '' if i == 2 else 's', drink))
    print()
print ('{} bottle of {} on the wall, {} bottle of {}.'.format(1, drink, 1, drink))
print ('Take it down, pass it around, no more bottles of {}.'.format(drink))
