#include <stdio.h>
#include <vector>
#include <tuple>
#include <algorithm>
using namespace std;

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
  for (int i = 0 ; i < n ; ++i) {
    int s, f, w;
    readn(s);
    readn(f);
    readn(w);
    v.push_back(make_tuple(f, s, w));
  }
  v.push_back(make_tuple(-1,-1,0));
  ++n;
  sort(v.begin(), v.end());
  vector<int> best(n);
  best[0] = 0;
  for (int i = 1 ; i < n ; ++i) {
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
