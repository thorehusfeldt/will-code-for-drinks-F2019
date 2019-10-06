#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

struct FW {
	vi ar;
	FW(int n) : ar(n+1) {}
	void add(int ind, int x) {
		while (ind + 1 < sz(ar)) {
			ar[ind + 1] += x;
			ind |= ind + 1;
		}
	}
	int sum(int lim) {
		int res = 0;
		while (lim) {
			res += ar[lim];
			lim &= lim - 1;
		}
		return res;
	}
};

int main() {
	cin.sync_with_stdio(false);
	int N;
	cin >> N;
	vi ar(N);
	rep(i,0,N) cin >> ar[i];
	map<int, int> ren;
	rep(i,0,N) ren[ar[i]];
	int ind = 0;
	trav(pa, ren) pa.second = ind++;
	ren[INT_MAX] = ind;
	FW fw(ind);
	unsigned int res = 0;
	for (int i = N; i--;) {
		res += fw.sum(ren.lower_bound((ar[i] + 1) / 2)->second);
		fw.add(ren[ar[i]], 1);
	}
	cout << res << endl;
}
