#!/usr/bin/python3


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

ok_if_leap_year = (days([31, 29] + L)) % 7 == 0

feb29 = today_d == 29 and today_m == 1
if not feb29:
    ok_if_not_leap_year = (days([31, 28] + L)) % 7 == 0

if ok_if_leap_year and (feb29 or ok_if_not_leap_year):
    print ("TGIF")
elif ok_if_leap_year or (not feb29 and ok_if_not_leap_year):
    print ("not sure")
else:
    print (":(")



