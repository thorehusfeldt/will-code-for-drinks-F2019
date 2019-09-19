#!/usr/bin/python3

# Falsely assumes all months have 31 days

line = input().split()

month = line[1]

M = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]

assert month in M

days = -1 # days since 1 JAN

# add days in previous months:
days += 31 * M.index(month)

# add days in this month:
days += int(line[0])
before = days < 31 + 28
feb29 = (days == 59 and month == 'FEB')

# shift by weekday on 1 JAN, where 0 = FRI:
days += [ 'FRI' , 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU' ].index(input().strip())
if days % 7 == 0 and (before or feb29):
    print ("TGIF")
elif days % 7 in [0,6] and not before and not feb29:
    print ("not sure")
else:
    print (":(")


