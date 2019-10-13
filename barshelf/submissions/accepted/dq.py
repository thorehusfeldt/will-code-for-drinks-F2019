from __future__ import print_function
from bisect import bisect_left, bisect_right, insort
from sys import stdin

''' Divide and conquer, following the merge-sort recurrence.
    Split in the middle, find left and right messy pairs.
    In the conquer step, assemble contribution from trios across the middle
    from the indexed count of messy *pairs* in the opposite part;
    use the same trick as for text-book "counting inversions" divide-and-conquer
    exercise, so the sorted sublists are passed up. Bit tricker here because
    it requires binary search to find the number of elements in the other part
    that contribute to a count.

    Only wart: to merge two sorted sublists in python, the fastest thing
    is to just sort them, spening linearithmic time in highly optimized C is better than
    spending linear time in Python.

    Running time is O(n log^2 n)
    '''

def slow_count(L):
    smaller = [0] * len(L)
    larger  = [0] * len(L)
    left, right = [], []

    for i in range(len(L)):
        larger[i] = len(left) - bisect_left(left, L[i] * 2)
        insort(left, L[i])

    for i in reversed(range(len(L))):
        smaller[i] = bisect_right(right, L[i] / 2)
        insort(right, L[i])

    return sum([larger[i] * smaller[i] for i in range(len(L))])

def count(lo, hi):
    ''' concerned with H[lo],...,H[hi], i.e., H[lo:hi+1] of length hi - lo + 1
        returns ct
        - ct, the number of antigeometric triples in H
        - as a side effect, ensured aux[lo:hi+1] = sorted(H[lo:hi+1])
        - L[i]: # indices j with j<i and H[j] >= 2*H[i] (Large guys to the Left) 
        - R[i]: # indices j with j>i and H[i] >= 2*H[j] (small guys to the Right)
    '''
    global H, L, R
    assert 0<= lo <= hi < len(H)
    if hi == lo:
        ct = 0
        aux[lo] = H[lo]
        L[lo] = R[lo] = 0
    elif hi == lo + 1:
        ct = 0
        L[lo] = R[hi] = 0
        L[hi] = int(H[lo] >= 2*H[hi])
        R[lo] = int(H[lo] >= 2*H[hi])
        aux[lo] = min(H[lo], H[hi])
        aux[hi] = max(H[lo], H[hi])
    else:
        mid = lo + (hi - lo)//2
        assert lo <= mid< mid+1 <= hi < len(H)
        a = count(lo, mid)
        b = count(mid+1, hi)
        c = conquer(lo, mid, hi)
        ct = a + b + c

    #assert ct == slow_count(H[lo:hi+1]), "ct = {} ({}), lo = {}, hi = {} ".format(ct, slow_count(H), lo, hi)
    return ct

def conquer(lo, mid, hi):
    '''
    return the crossing triples between index ranges lo..mid and mid+1..hi
    as a side effect, sort H from lo to hi (inclusive)
    and update the L and R dictionaries
    '''
    global H, L, R
    #assert okL(L, lo, mid) 
    #assert okR(R, mid+1, hi) 
    #assert is_sorted(aux, lo, mid)
    #assert is_sorted(aux, mid + 1, hi)

    ct = 0
    for i in range(lo, mid + 1):
        ct += L[i] * (bisect_right(aux, H[i] / 2, lo = mid + 1, hi = hi + 1) - mid - 1)
    for i in range(mid + 1, hi + 1):
        ct += R[i] * (mid + 1 - bisect_left(aux, 2*H[i], lo = lo, hi = mid + 1))

    #assert ct == slow_count(H[lo:hi+1])


    for i in range(lo, mid + 1):
        R[i] += bisect_right(aux, H[i] / 2, lo = mid + 1, hi = hi + 1) - mid - 1
    for i in range(mid + 1, hi + 1):
        L[i] += mid + 1 - bisect_left(aux, 2 * H[i], lo = lo, hi = mid + 1)

    #assert okL(L, lo, hi) 
    #assert okR(R, lo, hi) 

    tmp = sorted(H[lo: hi+1]) # not linear, but just faster than actually merging. Sue me.
    for i in range(hi - lo +1):
        aux[i + lo] = tmp[i]
    #assert is_sorted(aux, lo, hi)

    return ct

def is_sorted(_H, lo, hi): # inclusive
    for i in range(lo, hi):
        assert _H[i] <= _H[i+1]
    return True

def okL(_L, lo, hi):
    global H
    for i in range(lo, hi + 1):
        assert _L[i] == sum(1 for j in range(lo, i) if H[j] >= 2*H[i] )
    return True

def okR(_R, lo, hi):
    global H
    for i in range(lo, hi + 1):
        assert _R[i] == sum(1 for j in range(i+1, hi+1) if H[i] >= 2*H[j])
    return True

n = int(stdin.readline())
H = list(map(int, stdin.readline().split()))

L = [None]*n
R = [None]*n
aux = [None] * n

#print("Testing assertions")
#assert okL([0,0,2,3,0], 0, 4)
#ssert okR([2,2,1,0,0], 0, 4)

print (count(0, n-1))
