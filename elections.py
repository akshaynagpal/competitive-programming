#http://codeforces.com/problemset/problem/570/A

dimensions = [int(i) for i in raw_input().strip().split()]
n = dimensions[0]
m = dimensions[1]

arr = [[0 for x in range(n)] for x in range(m)]

for i in range(m):
    arr[i]=[int(j) for j in raw_input().strip().split()]

#print arr
    
winners=[]
#level 1 winners
for i in range(m):
    largest = arr[i][0]
    for j in range(1,n):
        if arr[i][j]>largest:
            largest = arr[i][j]
    winners.append(arr[i].index(largest))

#print winners

#lvl 2 winners

counts = []
for i in range(m):
    counts.append(winners.count(winners[i]))

#print counts

maximum_count = counts[0]
winning_index = 0

for i in range(1,m):
    if counts[i]>maximum_count:
        maximum_count = counts[i]
        winning_index = i
    elif (counts[i] == maximum_count and winners[i]<winners[winning_index]):
        winning_index = i

print winners[winning_index]+1 
