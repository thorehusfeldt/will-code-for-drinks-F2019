#include <iostream>
#include <stdio.h>
#include <vector>
#include <tuple>
using namespace std;

int main() {
  int n;
  cin >> n;
  vector<pair<int,int> > v;
  for (int i = 0 ; i < n ; ++i) {
    int s, f;
    cin >> s >> f;
    v.push_back(make_pair(f, s));
  }
  sort(v.begin(), v.end());
  int next_idle = 0;
  int res = 0;
  for (int i = 0; i < n; ++i) {
	  if (v[i].second >= next_idle) {
		  ++res;
		  next_idle = v[i].first;
	  }
  }
  cout << res << endl;
}
