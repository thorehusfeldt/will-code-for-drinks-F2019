#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

string upsidedown(string s) {
	reverse(all(s));
	trav(x, s) {
		if (x == '8' || x == '0' || x == '1') continue;
		if (x == '9') x = '6';
		else if (x == '6') x = '9';
		else return "";
	}
	return s;
}

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int N;
	cin >> N;
	vector<string> strs;
	rep(i,0,N) {
		string s;
		cin >> s;
		string s2 = upsidedown(s);
		if (!s2.empty() && s2 < s) s = s2;
		strs.push_back(s);
	}
	sort(all(strs), [&](const string& a, const string& b) {
		return a + b < b + a;
	});
	string res;
	trav(x, strs) res += x;
	cout << res << endl;
}
