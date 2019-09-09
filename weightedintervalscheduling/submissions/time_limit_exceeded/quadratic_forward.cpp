#include <bits/stdc++.h>
using namespace std;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
typedef long long ll;
typedef unsigned long long ull;
typedef vector<vi> vvi;
typedef vector<vii> vvii;
template <class T> T smod(T a, T b) { return (a % b + b) % b; }

void readn(int &n) {
  int sign = 1;
  char c;
  n = 0;
  while((c = getc_unlocked(stdin)) != '\n') {
    switch(c) {
      case '-': sign = -1; break;
      case ' ': goto hell;
      case '\n': goto hell;
      default: n *= 10; n += c - '0'; break;
    }
  }
hell:
  n *= sign;
}

int main() {
  int n;
  readn(n);
  vector<tuple<int,int,int> > v(n);
  rep(i,0,n) {
    readn(get<1>(v[i]));
    readn(get<0>(v[i]));
    readn(get<2>(v[i]));
  }
  sort(v.begin(), v.end());
  vi best(n);
  int m = 0;
  rep(i,0,n) {
    int s = get<1>(v[i]);
    int b = 0;
    rep(j,0,i) {
      if (get<0>(v[j]) > s) break;
      b = max(b, best[j]);
    }
    best[i] = b + get<2>(v[i]);
    m = max(m, best[i]);
  }
  printf("%d\n", m);
}
