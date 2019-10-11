#include<bits/stdc++.h> 
using namespace std; 
  
// Returns count of inversions of size 3 
int invcount(vector<int> arr, int n) 
{ 
    int invcount = 0;  // Initialize result 
  
    for (int j=1; j<n-1; j++) 
    { 
        // Count all smaller elements on right of arr[j] 
        int small = 0; 
        for (int k=j+1; k<n; k++) 
            if (arr[j] >= 2 * arr[k]) 
                small++; 
  
        // Count all greater elements on left of arr[i] 
        int great = 0; 
        for (int i = 0 ; i < j; ++i) 
            if (arr[i] >= 2 * arr[j]) 
                great++; 
  
        // Update inversion count by adding all inversions 
        // that have arr[i] as middle of three elements 
        invcount += great*small; 
    } 
  
    return invcount; 
} 

int main() {
	int N;
	cin >> N;
	vector<int> ar(N);
	for (int i = 0; i < N; ++i) cin >> ar[i];
	int res = invcount(ar, N);
	cout << res << endl;
}
