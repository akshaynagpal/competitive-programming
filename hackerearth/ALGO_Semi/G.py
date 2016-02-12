num_test = int(raw_input())
for i in range(num_test):
    n, show_string = raw_input().split()
    num_teams = int(n)
    team_strings = []

    for i in range(num_teams):
        team_strings.append(raw_input())

    scores = [0 for i in range(num_teams)]
    for i in range(num_teams):
        for letter in team_strings[i]:
            scores[i] += show_string.count(letter)
    max_score = max(scores)
    max_score_freq = scores.count(max_score)
    if max_score_freq == 1:
        print scores.index(max_score)+1
    else:
        winning_team_sizes=[]
        winning_team_indexes = []
        for i in range(len(scores)):
            if scores[i] == max_score:
                winning_team_sizes.append(len(team_strings[i]))
                winning_team_indexes.append(i)
        min_size = min(winning_team_sizes)
        print winning_team_indexes[winning_team_sizes.index(min_size)] + 1