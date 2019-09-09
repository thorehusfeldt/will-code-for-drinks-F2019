#include <stdio.h>
#include <vector>
#include <tuple>
#include <algorithm>
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
  vector<tuple<int,int,int> > v;
  rep(i,0,n) {
    int s, f, w;
    readn(s);
    readn(f);
    readn(w);
    v.push_back(make_tuple(f, s, w));
  }
  v.push_back(make_tuple(-1,-1,0));
  ++n;
  sort(v.begin(), v.end());
  vi best(n);
  rep(i,1,n) {
    int s = get<1>(v[i]);
    int lo = 0;
    int hi = i;
    while (hi - lo > 1) {
      int mi = (hi + lo) >> 1;
      if (get<0>(v[mi]) <= s) {
        lo = mi;
      } else {
        hi = mi;
      }
    }
    best[i] = max(best[i-1], best[lo] + get<2>(v[i]));
  }
  printf("%d\n", best[n-1]);
}
