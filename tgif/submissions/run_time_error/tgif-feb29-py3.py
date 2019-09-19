#!/usr/bin/python3

# Simulates until it finds given date. But fails to check for FEB 29 in non-leap year
# causing run time error.

M = [ 'JAN', 'FEB', 'MAR', 'APR', 'MAY', 'JUN', 'JUL', 'AUG', 'SEP', 'OCT', 'NOV', 'DEC' ]
L = [                  31, 30, 31, 30, 31, 31, 30, 31, 30, 31 ]
D = [ 'FRI' , 'SAT', 'SUN', 'MON', 'TUE', 'WED', 'THU' ]
line = input().split()
today_d = int(line[0])
today_m = M.index(line[1])

jan1 = D.index(input().strip()) 

def days(lengths):
    d, m = 1, 0

    total = jan1
    while (d, m) != (today_d, today_m):
        d += 1
        total = (total + 1) % 7
        if d > lengths[m]:
            d, m = 1, m + 1
    return total

ok_if_not_leap_year = (days([31, 28] + L)) % 7 == 0
ok_if_leap_year =     (days([31, 29] + L)) % 7 == 0

# print (ok_if_leap_year, ok_if_not_leap_year)
if ok_if_leap_year and ( ok_if_not_leap_year or today_d == 29 and today_m == 1):
    print ("TGIF")
elif ok_if_leap_year or ok_if_not_leap_year:
    print ("not sure")
else:
    print (":(")



