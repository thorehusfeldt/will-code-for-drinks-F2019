#include <stdio.h>
#include <stdlib.h>

long long merge_and_count(int* a, int* tmp, int lo, int mid, int hi){
	// from a[lo]...a[mid] and a[mid + 1],... a[hi]
	long long ct = 0;
	int i = lo;
	int j = mid + 1;

	while (i <= mid && j <= hi)
		if (a[i] > 2 * a[j]) {
			ct += mid  - i + 1;
			++j;
		}
		else ++i;

	i = lo;
	j = mid + 1;                
	for (int k = lo; k <= hi; ++k)
		if      (i > mid)     tmp[k] = a[j++];
		else if (j > hi)      tmp[k] = a[i++];
		else if (a[j] < a[i]) tmp[k] = a[j++];
		else                  tmp[k] = a[i++];

	for (int k = lo; k <= hi; ++k) a[k] = tmp[k];
	return ct;
	}

long long count_inversions(int* a, int* tmp, int lo, int hi) {
	if (hi  <= lo) return 0;
        int mid = lo + (hi - lo) / 2;
        long long ct = count_inversions(a, tmp, lo,    mid);
        ct +=    count_inversions(a, tmp, mid+1, hi );
        ct +=    merge_and_count(a, tmp, lo, mid, hi);
        return ct;
}

int main() {
	int n;
	scanf("%d", &n);
	int* a =   malloc(n * sizeof(int));
	int* tmp = malloc(n * sizeof(int));
	for (int i = 0; i < n; ++i) scanf("%d", &a[i]);
	printf ("%lld\n", count_inversions(a, tmp, 0, n - 1));
}
