# problem link: https://www.hackerrank.com/contests/supercoder-or-pseudocoder/challenges/q-2

#Solution

import sys
n = int(raw_input())
range_list = []
num_prime = []

for i in range(n):
    range_list.append(raw_input().split())

for i in range(n):
    prime_counter = 0
    low = int(range_list[i][0])
    high = int(range_list[i][1])
    for k in range(low+1,high):
        prime_flag = 1
        for x in range(2,k/2+1):
            if k % x == 0:
                prime_flag = 0
        if prime_flag == 1:
            prime_counter += 1
    num_prime.append(prime_counter)     
for j in range(n):
    sys.stdout.write(str(num_prime[j])+'\n')
     
