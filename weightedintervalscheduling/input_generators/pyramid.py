from random import choice, shuffle
I = []
for i in range(10**5):
    I.append(( 10**6 - i - 1,  10**6 + i + 1, choice([1,2])))
shuffle(I)
print (len(I))
for s, f, w in I:
    print (s,f,w)
