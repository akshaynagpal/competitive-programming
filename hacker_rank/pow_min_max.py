# problem -  https://www.hackerrank.com/contests/supercoder-or-pseudocoder/challenges/power-of-minimum-and-maximum

# solution

import sys
n = int(raw_input())
arr = [int(i) for i in raw_input().strip().split()]
num_queries = int(raw_input())
query_list = []
for i in range(num_queries):
    query_list.append(raw_input().split())
for i in range(num_queries):
    prod = 0
    power = 0
    low = int(query_list[i][0]) - 1
    high = int(query_list[i][1]) - 1
    maximum = arr[low]
    minimum = arr[low]
    for i in range(low,high+1):
        if arr[i]>maximum:
            maximum = arr[i]
        if arr[i]<minimum:
            minimum = arr[i]
    prod = (maximum * minimum) % (pow(10,4) + 7)
    power = pow(minimum,maximum) % (pow(10,4) + 7)
    sys.stdout.write(str(prod)+" "+str(power)+"\n")
