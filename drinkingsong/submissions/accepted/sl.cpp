#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string bev;
string bot(int n) {
	if (n == 1) return "1 bottle of " + bev;
	else return to_string(n) + " bottles of " + bev;
}

int main() {
	int N;
	cin >> N >> bev;
	for (; N > 0; N--) {
		cout << bot(N) << " on the wall, " << bot(N) << "." << endl;
		if (N == 1)
			cout << "Take it down, pass it around, no more bottles of " << bev << "." << endl;
		else
			cout << "Take one down, pass it around, " << bot(N-1) << " on the wall." << endl << endl;
	}
}
