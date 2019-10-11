#include <stdio.h>
#include <stdlib.h>


int main(int argv, char** args) 
{ 
	int n;
	scanf("%d", &n);
	int* arr = (int*) malloc(n * sizeof(int));
	for (int i = 0; i < n; ++i)
		scanf("%d", &arr[i]);
	long long res = 0;
	for (int i = 0; i < n - 2; ++i)
		for (int j = i + 1; j < n - 1; ++j)
			for (int k = j + 1; k < n; ++k) 
				res += (arr[i] >= 2*arr[j] && arr[j] >= 2*arr[k]);

	printf("%lld", res);
	return 0; 
} 

