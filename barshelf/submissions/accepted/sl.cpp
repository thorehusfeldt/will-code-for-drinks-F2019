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
	vector<ll> ar;
	FW(int n) : ar(n+1) {}
	void add(int ind, ll x) {
		while (ind + 1 < sz(ar)) {
			ar[ind + 1] += x;
			ind |= ind + 1;
		}
	}
	ll sum(int lim) {
		ll res = 0;
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
	FW fw1(ind);
	FW fw2(ind);
	ll res = 0;
	for (int i = N; i--;) {
		int mine = ren[ar[i]];
		int lim = ren.upper_bound(ar[i] / 2)->second;
		ll res1 = fw1.sum(lim);
		ll res2 = fw2.sum(lim);
		res += res2;
		fw1.add(mine, 1);
		fw2.add(mine, res1);
	}
	cout << res << endl;
}
