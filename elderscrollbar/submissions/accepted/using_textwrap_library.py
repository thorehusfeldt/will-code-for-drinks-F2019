from sys import stdin, stdout
from textwrap import wrap

W, H, L, N = map(int, stdin.readline().split())
text = ' '.join([stdin.readline().strip() for _ in range(N)])

typesettext = [ line[:W] for line in wrap(text, W, break_long_words = False) ]

thumbpos = int(L * (H-2) / (len(typesettext) - H + 1)) + 1
scrollbar = ['^'] + [' '] * (H - 2) + ['v']
scrollbar[thumbpos] = 'X'

print ('+' + '-' * W + '+-+')
for i in range(L , L + H):
    print('|{:<{width}}|{}|'.format(typesettext[i], scrollbar[i - L],  width = W))
print ('+' + '-' * W + '+-+')
