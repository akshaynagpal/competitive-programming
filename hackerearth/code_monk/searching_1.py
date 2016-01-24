size, queries = raw_input().split()
size = int(size)
queries=int(queries)

arr = []
query_arr = []

arr = raw_input().split()

for j in range(queries):
    query_arr.append(raw_input())

for value in query_arr:
    if value in arr:
        print "YES"
    else:
        print "NO"
