#include <stdio.h>
#include <vector>
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

struct Interval {
  int s = -1, f = -1, w = 0;
  Interval(int _s, int _f, int _w) : s(_s), f(_f), w(_w) {};
};

bool compareInterval(Interval i1, Interval i2) {
  return (i1.f < i2.f);
}

int main() {
  int n;
  readn(n);
  vector<Interval> v;
  for (int i = 0 ; i < n ; ++i) {
    int s, f, w; 
    readn(s);
    readn(f);
    readn(w);
    v.push_back(Interval(s, f, w));
  }
  v.push_back(Interval(-1, -1, 0));
  ++n;
  sort(v.begin(), v.end(), compareInterval);
  vector<int> best(n);
  for (int i = 0 ; i < n ; ++i) {
    int s = v[i].s;
    int lo = 0;
    int hi = i;
    while (hi - lo > 1) {
      int mi = (hi + lo) >> 1;
      if (v[mi].f <= s) {
        lo = mi;
      } else {
        hi = mi;
      }
    }
    best[i] = max(best[i-1], best[lo] + v[i].w);
  }
  printf("%d\n", best[n-1]);
}
