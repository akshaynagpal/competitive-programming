import csv

with open('123.csv','wb') as openfile:
	openwriter = csv.writer(openfile)
	openwriter.writerow(["hello","hello","hello","hello","hello"])
