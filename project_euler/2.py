i=1
j=2
sum=2
next_term = i+j
while(next_term<=4000000):
	if(next_term%2==0):
		sum += next_term
	i = j
	j = next_term
	next_term = i + j

print sum
