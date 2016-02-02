import csv
count = 0
with open('submissions.csv', 'rb') as count_file:
    csv_reader = csv.reader(count_file)
    for row in csv_reader:
        count += 1

print count