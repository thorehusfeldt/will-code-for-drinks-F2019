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
  vector<tuple<int,int,int> > v(n);
  rep(i,0,n) {
    readn(get<1>(v[i]));
    readn(get<0>(v[i]));
    readn(get<2>(v[i]));
  }
  sort(v.begin(), v.end());
  vi best(n);
  best[0] = get<2>(v[0]);
  rep(i,1,n) {
    int s = get<1>(v[i]);
    int j = i - 1;
    while (j >= 0) {
      if (get<0>(v[j]) <= s) break;
      --j;
    }
    if (j >= 0) {
      best[i] = max(best[i-1], best[j] + get<2>(v[i]));
    } else {
      best[i] = max(best[i-1], get<2>(v[i]));
    }
  }
  printf("%d\n", best[n-1]);
}
