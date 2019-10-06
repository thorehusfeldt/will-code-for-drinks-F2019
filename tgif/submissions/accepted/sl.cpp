#include <bits/stdc++.h>
using namespace std;

#define rep(i, from, to) for (int i = from; i < (to); ++i)
#define trav(a, x) for (auto& a : x)
#define all(x) begin(x), end(x)
#define sz(x) (int)(x).size()
typedef long long ll;
typedef pair<int, int> pii;
typedef vector<int> vi;

const string monthNames[] = {"JAN", "FEB", "MAR", "APR", "MAY", "JUN", "JUL", "AUG", "SEP", "OCT", "NOV", "DEC"};
const string dayNames[] = {"MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"};
int monthDays[] = {31, 0, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};

int main() {
	cin.sync_with_stdio(false);
	cin.exceptions(cin.failbit);
	int day;
	string str;
	cin >> day >> str;
	int month = (int)(find(all(monthNames), str) - monthNames);
	cin >> str;
	int jan1 = (int)(find(all(dayNames), str) - dayNames);
	auto sol = [&]() {
		int days = jan1;
		rep(m,0,month) days += monthDays[m];
		days += day - 1;
		return days % 7;
	};
	monthDays[1] = 28;
	int day1 = sol();
	monthDays[1] = 29;
	int day2 = sol();
	if (day1 == 4 && day2 == 4) cout << "tgif" << endl;
	else if (day1 == 4 || day2 == 4) cout << "not sure" << endl;
	else cout << ":(" << endl;
}
