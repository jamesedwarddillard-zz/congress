import csv

def candidate_csv(csv_name):
	with open(csv_name) as file:
		filereader = csv.reader(file)
		data = [row for row in filereader]
		return data

# need to pop header off and then start a process to organize the data
# you'll then call for the cid and then merge it with the existing data

print candidate_csv('test_candidates.csv')