# link: https://www.hackerearth.com/algorithms-qualifiers-round-1/algorithm/hungry-lemurs/

num_bananas,num_lemurs = raw_input().split()

bananas = int(num_bananas)
lemurs = int(num_lemurs)
total_time = 0

def combinations(b,l):
    pair_list = []
    pair_list.extend((((b+1),(l+1)),((b-1),(l-1)),((b+1),(l-1)),((b-1),(l+1)),((b+1),l),((b-1),l),(b,(l+1)),(b,(l-1))))
    comp_list = []
    for i in range(8):
        ans = 0
        t1 = pair_list[i][0]
        t2 = pair_list[i][1]
        ans = t1%t2
        if(ans>=0):
            comp_list.append(t1%t2)
        else:
            comp_list.append(1000000)
    minimum_element = min(comp_list)
    index_of_min = comp_list.index(minimum_element)
    if index_of_min<4:
            return index_of_min,2
    else:
            return index_of_min,1
		

while (bananas%lemurs != 0):
    index_min,increment = combinations(bananas,lemurs)
    total_time += increment
    if index_min <4:
            if index_min == 0:
                    bananas += 1
                    lemurs +=1
            elif index_min ==1:
                    bananas -=1
                    lemurs -= 1
            elif index_min ==2:
                    bananas +=1
                    lemurs -= 1
            else:
                    bananas -=1
                    lemurs += 1
    else:
            if index_min == 4:
                    bananas += 1
            elif index_min ==5:
                    bananas -=1
            elif index_min ==6:
                    lemurs += 1
            else:
                    lemurs -= 1
    
print total_time
