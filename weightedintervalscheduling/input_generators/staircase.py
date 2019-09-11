from random import choice, shuffle
I = []
for i in range(10**5):
    I.append((i, i+2, choice([1,2])))
shuffle(I)
print (len(I))
for s, f, w in I:
    print (s,f,w)
