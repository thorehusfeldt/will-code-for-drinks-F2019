from random import choice, shuffle
I = []
I.append(( 10**6 - 1,  10**6 + 1, choice([1,2])))
for i in range(1, 10**5 // 2 - 1):
    I.append(( 10**6 - i - 1,  10**6 - i + 1, choice([1,2])))
    I.append(( 10**6 + i - 1,  10**6 + i + 1, choice([1,2])))
shuffle(I)
print (len(I))
for s, f, w in I:
    print (s,f,w)
