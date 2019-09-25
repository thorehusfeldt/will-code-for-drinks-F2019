#include <stdio.h>
#include <stdlib.h>

typedef struct 
{
	int s, f;
} interval;

int cmp(const void *a, const void *b) {
	return (*((interval **) a))->f - (*((interval **) b))->f;
}

int main(void)
{
	int n, s, f;
	scanf("%d", &n);
	interval* intervals = malloc(n * sizeof(interval)); // probably even faster if array of pointers, not structs. Sue me.
	interval** pointers = malloc(n * sizeof(interval*));
	for (int i = 0; i < n; ++i) {
		scanf("%d %d", &s, &f);
		intervals[i] = (interval) {s, f};
		pointers[i] = &intervals[i]; 
	}

	qsort(pointers, n, sizeof (interval*), cmp);

	int next_idle = 0;
	int res = 0;
	for (int i = 0; i < n; ++i) {
		if (pointers[i]->s >= next_idle) {
			++res;
			next_idle = pointers[i]->f;
		}
	}
	printf("%d\n", res);
}
