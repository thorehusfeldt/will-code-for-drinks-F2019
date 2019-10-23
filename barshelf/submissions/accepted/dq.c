#include <stdio.h>
#include <stdlib.h>

long *H, *tmp, *aux, *L, *R;

/*  Divide and conquer, following the merge-sort recurrence.
    Split in the middle, find left and right messy pairs.
    In the conquer step, assemble contribution from trios across the middle
    from the indexed count of messy *pairs* in the opposite part;
    use the same trick as for text-book "counting inversions" divide-and-conquer
    exercise, so the sorted sublists are passed up. Bit tricker here because
    it requires binary search to find the number of elements in the other part
    that contribute to a count.

    Running time is O(n log^2 n)
    */

int bisect_left(long* arr, int item, int lo, int hi) {
	while (lo < hi) {
		int mid = (lo + hi) / 2;
		if (arr[mid] < item) lo = mid + 1;
		else                 hi = mid;
	}
	return lo;
}

int bisect_right(long* arr, int item, int lo, int hi) {
	while (lo < hi) {
		int mid = (lo + hi) / 2;
		if (item < arr[mid]) hi = mid;
		else                 lo = mid + 1;
	}
	return lo;
}

long conquer(int lo, int mid, int hi) {
	/*
	   return the crossing triples between index ranges lo..mid and mid+1..hi
	   as a side effect, sort H from lo to hi (inclusive)
	   and update the L and R dictionaries
	   */

	long ct = 0;
	for (int i  = lo; i < mid + 1; ++i) 
		ct += L[i] * (bisect_right(aux, H[i] / 2, mid + 1, hi + 1) - mid - 1);
	for (int i = mid + 1; i < hi + 1; ++i) 
		ct += R[i] * (mid + 1 - bisect_left(aux, 2*H[i], lo, mid + 1));

	for (int i = lo; i < mid + 1; ++i) 
		R[i] += bisect_right(aux, H[i] / 2, mid + 1, hi + 1) - mid - 1;
	for (int i = mid + 1; i <  hi + 1; ++i) 
		L[i] += mid + 1 - bisect_left(aux, 2 * H[i], lo, mid + 1);
		
	//mergesort aux[lo]..aux[hi], using tmp as temporary storage:
        for (int k = lo; k <= hi; k++)
	       tmp[k] = aux[k];
        int i = lo;
        int j = mid+1;
        for (int k = lo; k <= hi; k++) {
            if      (i > mid)         aux[k] = tmp[j++]; 
            else if (j > hi)          aux[k] = tmp[i++];
            else if (tmp[j] < tmp[i]) aux[k] = tmp[j++];
            else                      aux[k] = tmp[i++];
        }	

	return ct;
}

long count(int lo, int hi) {
	/* concerned with H[lo],...,H[hi], i.e., H[lo:hi+1] of length hi - lo + 1
	   returns ct
	   - ct, the number of antigeometric triples in H
	   - as a side effect, ensured aux[lo:hi+1] = sorted(H[lo:hi+1])
	   - L[i]: # indices j with j<i and H[j] >= 2*H[i] (Large guys to the Left) 
	   - R[i]: # indices j with j>i and H[i] >= 2*H[j] (small guys to the Right)
	   */
	long ct;

	if (hi == lo) {
		ct = 0;
		aux[lo] = H[lo];
		L[lo] =  0;
		R[lo] = 0;
	}
	else if  (hi == lo + 1) {
		ct = 0;
		L[lo] = R[hi] = 0;
		L[hi] = (H[lo] >= 2*H[hi]);
		R[lo] = (H[lo] >= 2*H[hi]);
		aux[lo] = (H[lo] <  H[hi]) ? H[lo] : H[hi];
		aux[hi] = (H[lo] >  H[hi]) ? H[lo] : H[hi];
	}
	else { 
		int mid = lo + (hi - lo)/2;
		ct = count(lo, mid) + count(mid+1, hi) + conquer(lo, mid, hi);
	}
	return ct;
}


int main(int argv, char** args)
{
	int n;
	scanf("%d", &n);
	H = (long*) malloc(n * sizeof(long));
	aux = (long*) malloc(n * sizeof(long));
	tmp = (long*) malloc(n * sizeof(long)); // prolly either tmp or aux can be avoided...
	L = (long*) malloc(n * sizeof(long));
	R = (long*) malloc(n * sizeof(long));
	for (int i = 0; i < n; ++i) {
		scanf("%ld", &H[i]);
		aux[i] = H[i];
	}

	printf("%ld\n", count(0, n-1));

	return 0;
}
