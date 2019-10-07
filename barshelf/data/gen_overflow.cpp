#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main(int argc, char *argv[]) {
	if (argc != 3) {
       		cerr << "Wrong number of arguments to gen_overflow" << endl;
		return 1;
	}
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int N = atoi(argv[1]);
	vi nums = {1};
	for (;;) {
		ll x = nums.back();
		x = x * 2 + 1;
		if (x <= 1'000'000'000) {
			nums.push_back((int)x);
		}
		else break;
	}
	cout << N << endl;
	rep(i,0,N) {
		if (i) cout << ' ';
		cout << nums[(N-1 - i) * sz(nums) / N];
	}
	cout << endl;
}
