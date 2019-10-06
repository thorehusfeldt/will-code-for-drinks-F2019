#!/usr/bin/python3

def countInversions(list):
    if(len(list) <= 1):
        return list, 0
    else:
        mid = int(len(list)/2)
        left, a = countInversions(list[:mid])
        right, b = countInversions(list[mid:])
        result, c = mergeAndCount(left, right)
        return result, (a + b + c)

def mergeAndCount(left, right):
    result = []
    count = 0

    i,j = 0,0                
    while(i < len(left) and j < len(right)):
        if(left[i] < right[j]):
            result.append(left[i])
            i += 1
        else:
            if left[i] > 2 * right[j]:
                count += len(left) - i
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result, count

input()
L = list(map(int, input().split()))
print (countInversions(L)[1])
