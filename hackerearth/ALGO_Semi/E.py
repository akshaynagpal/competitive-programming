import math
def calc_next(pressed_keys,k,m,n):
        summ = 0
        for i in range(1,n+1):
            summ += math.pow(-1,i+1)*pressed_keys[k-i]
        return summ % m

num_test = int(raw_input())
for j in range(num_test):
    n,m,z = raw_input().split()
    n = int(n)
    m = int(m)
    z = int(z)
    pressed_keys = [int(j) for j in raw_input().split()]
    current_length = len(pressed_keys)
    while(current_length!=z+1):
        pressed_keys.append(calc_next(pressed_keys,current_length,m,n))
        current_length += 1
    print int(pressed_keys[-1])


