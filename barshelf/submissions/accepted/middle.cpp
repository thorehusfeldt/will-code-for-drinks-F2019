#include<bits/stdc++.h> 
using namespace std; 

// Returns count of inversions of size 3 
unsigned long invcount(vector<unsigned long> arr, unsigned long n) 
{ 
	unsigned long invcount = 0;  // Initialize result 
	long long max = 0;

	for (unsigned long j = 1; j < n - 1; ++j) 
	{ 
		// Count all greater elements on left of arr[i] 
		unsigned long great = 0; 
		for (unsigned long i = 0 ; i < j; ++i) 
			if (arr[i] >= 2 * arr[j]) 
				great++; 

		// Count all smaller elements on right of arr[j] 
		unsigned long small = 0; 
		for (unsigned long k = j + 1; k < n; ++k) 
			if (arr[j] >= 2 * arr[k]) 
				small++; 

		unsigned long res = ( ((long long) great) * ((long long) small));
		if (res >  max){
			//printf("%ld %ld\n", res, invcount);
			max = res;
		}




		// Update inversion count by adding all inversions 
		// that have arr[i] as middle of three elements 
		invcount = (invcount + res) ;
	} 

	return invcount; 
} 

int main() {
	unsigned long N;
	cin >> N;
	vector<unsigned long> ar(N);
	for (unsigned long i = 0; i < N; ++i) cin >> ar[i];
	unsigned long res = invcount(ar, N);
	cout << res << endl;
}
