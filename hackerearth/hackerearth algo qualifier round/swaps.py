#link : https://www.hackerearth.com/algorithms-qualifiers-round-1/algorithm/permutation-swaps/
test_cases = int(raw_input())

for i in range(test_cases):
    flag = 0
    length_of_array,num_good_pairs = raw_input().split()
    array_length = int(length_of_array)
    number_good_pairs = int(num_good_pairs)
    array_p = raw_input().split()
    array_q = raw_input().split()
    good_pair_list = []
    for p in range(number_good_pairs):
        xx,yy = raw_input().split()
        good_pair_list.append((xx,yy))
            
    for pair in good_pair_list:
        t1 = int(pair[0])-1
        t2 = int(pair[1])-1
        temp_array = array_p
        temp_array[t1],temp_array[t2] = temp_array[t2],temp_array[t1]
        if temp_array == array_q:
            flag = 1
    if flag == 1:
        print "YES"
    else:
        print "NO"
