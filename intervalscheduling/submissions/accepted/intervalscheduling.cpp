#include <iostream>
#include <vector>
#include <tuple>
#include <algorithm>  
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
	for (auto i: v)
		if (i.second >= next_idle) {
			++res;
			next_idle = i.first;
		}
	cout << res << endl;
}
