import csv
total = 1198132
counter = 0
with open('finalSS.csv', 'wb') as final_file:
    final_writer = csv.writer(final_file)
    with open('submissions.csv', 'rb') as sub_file:
        sub_reader = csv.reader(sub_file)
        for row in sub_reader:
            # print row[1]
            record_to_add = []
            record_to_add.extend([row[2], row[3]])

            with open('problems.csv', 'rb') as prob_file:
                prob_reader = csv.reader(prob_file)
                for prob_row in prob_reader:
                    # print prob_row[0], row[1]
                    if prob_row[0].strip() == row[1].strip():
                        record_to_add.extend(prob_row)

            with open('users.csv', 'rb') as user_file:
                user_reader = csv.reader(user_file)
                for user_row in user_reader:
                    # print user_row[0], row[0]
                    if (user_row[0].strip()) == (row[0].strip()):
                        record_to_add.extend(user_row)
            # print record_to_add
            final_writer.writerow(record_to_add)
            counter += 1
            print "progress = ", str(counter), " / ", str(total)
