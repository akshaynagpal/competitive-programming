from operator import xor
import sys

num_test = int(raw_input())
for i in range(num_test):
    n,m,p,x = raw_input().split()
    n = int(n)
    m = int(m)
    p = int(p)
    x = int(x)

    given_row = list(raw_input())
    current_row = [int(i) for i in given_row]

    for i in range(1,n):
        next_row=[0 for i in range(m)]
        for j in range(0,m):
            next_row[(j+p) % m] = xor(xor(current_row[j], x), current_row[(j+p) % m])
        current_row = next_row
    print(''.join(str(x) for x in current_row))


