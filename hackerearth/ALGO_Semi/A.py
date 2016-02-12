import itertools
import sys

num_tests = int(raw_input())

for i in range(num_tests):
    x, y, z = raw_input().split()
    a = int(x)
    b = int(y)
    q = int(z)

    q_list = [int(i) for i in raw_input().split()]

    add = a + b
    sub = max(a,b) - min(a,b)
    adder_list = [a,b,add,sub]

    for query in q_list:
        if query < min(a,b):
            sys.stdout.write('0')
        elif query in adder_list:
            sys.stdout.write('1')
        else:
            two_list = list(itertools.combinations_with_replacement(adder_list,2))
            sum_two_list = []
            for i in range(len(two_list)):
                sum_two_list.append(sum(two_list[i]))
            if query in sum_two_list:
                sys.stdout.write('1')
            else:
                three_list = list(itertools.combinations_with_replacement(adder_list,3))
                sum_three_list = []
                for i in range(len(three_list)):
                    sum_three_list.append(sum(three_list[i]))
                if query in sum_three_list:
                    sys.stdout.write('1')
                else:
                    four_list = list(itertools.combinations_with_replacement(adder_list,4))
                    sum_four_list = []
                    for i in range(len(four_list)):
                        sum_four_list.append(sum(four_list[i]))
                    if query in sum_four_list:
                        sys.stdout.write('1')
                    else:
                        five_list = list(itertools.combinations_with_replacement(adder_list,5))
                        sum_five_list = []
                        for i in range(len(five_list)):
                            sum_five_list.append(sum(five_list[i]))
                        if query in sum_five_list:
                            sys.stdout.write('1')
                        else:
                            six_list = list(itertools.combinations_with_replacement(adder_list,6))
                            sum_six_list = []
                            for i in range(len(six_list)):
                                sum_six_list.append(sum(six_list[i]))
                            if query in sum_six_list:
                                sys.stdout.write('1')
                            else:
                                sys.stdout.write('0')
    print ""