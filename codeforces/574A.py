n = int(raw_input())
vote_list = [int(i) for i in raw_input().strip().split()]

count = 0

def checkmax(vote_list):
    for i in range(1,n):
        if vote_list[i] >= vote_list[0]:
            return False
    return True

while(checkmax(vote_list) == False and count < vote_list[0]):
    for i in range(1,n):
        if vote_list[i] >= vote_list[0]:
            vote_list[i] -= 1
            vote_list[0] += 1
            count += 1

print count

        
