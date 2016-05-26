# Alternative: Sieve of Erastothenes

def check_prime(x):
	maxp = int(pow(x,0.5))
	for i in range(2,maxp+1):
		if x%i == 0:
			return False
	return True

num = 600851475143
temp = int(num/2)
max_div_prime = 2
for i in range(3,temp,2):
	if check_prime(i) and num%i==0:
		max_div_prime = i

print(max_div_prime)
