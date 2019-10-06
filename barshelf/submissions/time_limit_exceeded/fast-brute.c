#pragma GCC optimize ("Ofast")
#include "stdio.h"

#define M 100000

int data[M];

void readn(int *n) {
  char c;
  *n = getc_unlocked(stdin) - '0';
  while((c = getc_unlocked(stdin)) != ' ') {
    if (c == '\n') return;
    else {
      *n = 10 * (*n) + c - '0';
    }
  }
}

int main() {
    int n;
    readn(&n);
    int ans = 0;
    for (int i = 0 ; i < n ; ++i) {
        readn(&data[i]);
        int tall = data[i] << 1;
        for (int j = 0 ; j < i ; ++j) {
            ans += (data[j] > tall);
        }
    }
    printf("%d\n", ans);
}
