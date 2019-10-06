#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) x.begin(), x.end()
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

int main() {
	int W, H, L, N;
	cin >> W >> H >> L >> N;
	string word;
	string line;
	vector<string> lines;
	while (cin >> word) {
		if (sz(line) == 0) {
up:
			line = word;
			if (sz(line) > W) line.resize(W);
		}
		else if (sz(line) + 1 + sz(word) <= W) {
			line += ' ';
			line += word;
		}
		else {
			lines.push_back(line);
			goto up;
		}
	}
	assert(!line.empty());
	lines.push_back(line);

	// 0 <= line <= H - 3
	// L = 0 maps to 0
	// L = sz(lines)-H maps to 1
	// ratio = L / (sz(lines)-H)
	// multiply by H - 3, round down
	int cursorLine = (sz(lines) - H == 0 ? 0 : (int)((ll)(H - 3) * L / (sz(lines) - H)));
	cursorLine += L+1;
	cout << "+" << string(W, '-') << "+-+" << endl;
	rep(i,L,L+H) {
		cout << "|" << setw(W) << setfill(' ') << left << lines[i] << "|";
		if (i == L) cout << "^";
		else if (i == L+H-1) cout << "v";
		else if (i == cursorLine) cout << "X";
		else cout << " ";
		cout << "|" << endl;
	}
	cout << "+" << string(W, '-') << "+-+" << endl;
}
