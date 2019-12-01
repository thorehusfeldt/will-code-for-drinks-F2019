#!/usr/bin/env python3

FLIP = {'1': '1', '0': '0', '8':'8', '6':'9', '9':'6'}

class magnet(str):
    def __new__(cls, text):
        if all(c in FLIP for c in text):
            text = min(text, ''.join(FLIP[c] for c in text[::-1]))
        return super().__new__(cls, text)

    def __lt__(self, other):
        return str(self) + str(other) < str(other) + str(self)

A = [magnet(input()) for _ in range(int(input()))]
print(''.join(text for text in sorted(A)))
