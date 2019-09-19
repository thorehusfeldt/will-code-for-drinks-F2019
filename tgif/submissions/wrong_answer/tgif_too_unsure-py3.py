#!/usr/bin/python3

# Incorrectly thinks we have *no* idea which day it is in MAR till DEC    

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
feb29 = (days == 59 and month == 'FEB')

# shift by weekday on 1 JAN, where 0 = FRI:
days += [ 'FRI' , 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU' ].index(input().strip())
if days % 7 == 0 and (before or feb29):
    print ("TGIF")
else: 
    print ("not sure")


