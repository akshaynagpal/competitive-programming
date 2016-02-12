master_list = []
num_test = int(raw_input())

def print_list(list_to_print):
    global master_list
    master_list.append(list_to_print)
    return 0


def path_find(vertex):
    current_path.append(vertex)
    for i in range(int(v)):
        if adj_list[vertex][i] == 1:
            if i == dest:
                path_list.append(current_path)
                print_list(path_list[0])
            elif i not in current_path:
                path_find(i)
    del current_path[-1]
    return 0


for i in range(num_test):
    n, m = raw_input().split()
    v = int(n)
    e = int(m)
    adj_list = [[0 for x in range(v)] for x in range(v)]
    for k in range(e):
        u, v, w = raw_input().split()
        adj_list[int(u) - 1][int(v) - 1] = int(w)
        adj_list[int(v) - 1][int(u) - 1] = int(w)

    num_req_nodes = int(raw_input())
    req_nodes = [(int(i) - 1) for i in raw_input().split()]
    source = req_nodes[0]
    dest = req_nodes[-1]
    current_path = []
    path_list = []

    path_find(source)

    print master_list
