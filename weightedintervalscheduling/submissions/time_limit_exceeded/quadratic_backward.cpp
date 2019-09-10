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
  vector<tuple<int,int,int> > v(n);
  for (int i = 0 ; i < n ; ++i) {
    readn(get<1>(v[i]));
    readn(get<0>(v[i]));
    readn(get<2>(v[i]));
  }
  sort(v.begin(), v.end());
  vector<int> best(n);
  best[0] = get<2>(v[0]);
  for (int i = 1 ; i < n ; ++i) {
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
