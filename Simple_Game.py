inputs = [int(i) for i in raw_input().strip().split()]
n = inputs[0]
m = inputs[1]

prob_dict={};

for a in range(1,n):
	count = 0
	for c in range(1,n):
		if abs(c-a) < abs(c-m):
			count += 1
	prob_dict[a] = count

winning_a = 1
max_prob = prob_dict[winning_a]

for i in range(2,n):
	if prob_dict[i]>prob_dict[winning_a]:
		winning_a = i
		max_prob = prob_dict[winning_a]
print prob_dict
print winning_a




    
    
     
