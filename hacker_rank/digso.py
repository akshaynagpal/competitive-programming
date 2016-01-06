# problem link : https://www.hackerrank.com/contests/projecteuler/challenges/euler063
#python 3 used
#solution below




n = int(input("Enter n"))
def is_perfect( value, exponent ):
    root = value ** ( 1.0 / exponent )
    root = int( round( root ) )
    return root ** exponent == value


low = 10**(n-1)
high = 10**n

for i in range(low,high):
        if(is_perfect(i,n)== True):
            print (i)