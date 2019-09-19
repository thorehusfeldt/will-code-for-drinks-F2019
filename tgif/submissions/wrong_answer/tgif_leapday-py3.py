#!/usr/bin/python3

# Misses that on 29 FEB we're sure which day it is

line = input().split()

month = line[1]

M = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]
L = [    31,    28,    31,    30,    31,    30,    31,    31,    30,    31,    30,    31 ]

assert month in M

days = -1 # days since 1 JAN

# add days in previous months:
for i in range(M.index(month)):
    days += L[i]

# add days in this month:
days += int(line[0])
before = days < 31 + 28

# shift by weekday on 1 JAN, where 0 = FRI:
days += [ 'FRI' , 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU' ].index(input().strip())
if days % 7 == 0 and before:
    print ("TGIF")
elif days % 7 in [0,6] and not before:
    print ("not sure")
else:
    print (":(")


