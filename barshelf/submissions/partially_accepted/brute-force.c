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
	for (int i = 0; i < n - 1; ++i)
		for (int j = i + 1; j < n; ++j)
			if (arr[i] > 2*arr[j])
				++res;		
	
	printf("%lld", res);
	return 0; 
} 

