import csv
import pandas
from crpapi import candidate_summary, candidate_details
from secrets import API_KEY

def candidate_csv(csv_name): # will only work with the CRP formatted CSV
	with open(csv_name) as file:
		reader = csv.DictReader(file)
		data = [row for row in reader]
		return data

def enriched_data(candidate_data_dict):
	cid = candidate_data_dict['CID']
	crp_online_data = candidate_details(candidate_summary(apikey = API_KEY, cid = cid))
	candidate_data= {}
	candidate_data['cid'] = cid # data from the original csv
	candidate_data['name'] = candidate_data_dict['CRPName']
	candidate_data['district'] = candidate_data_dict['DistIDRunFor']
	candidate_data['party'] = candidate_data_dict['Party']
	candidate_data['status code'] = crp_online_data['status_code']
	if crp_online_data['status_code'] == 200:
		crp_online_data = crp_online_data['details']
		candidate_data['spent'] = float(crp_online_data['spent']) # data pulled from the api
		candidate_data['total'] = float(crp_online_data['total'])
		candidate_data['cash on hand'] = float(crp_online_data['cash_on_hand'])
		candidate_data['debt'] = float(crp_online_data['debt'])
		candidate_data['updated date'] = crp_online_data['last_updated']
	else:
		candidate_data['spent'] = 'not found'
		candidate_data['total'] = 'not found'
		candidate_data['cash on hand'] = 'not found'
		candidate_data['debt'] = 'not found'
		candidate_data['updated date'] = 'not found'
	return candidate_data

headers = ['cid', 'name', 'district', 'party', 'spent', 'total', 'cash on hand', 'debt', 'updated date', 'status code']

def new_csv(old_csv):
	data = candidate_csv(old_csv)
	with open('candidate_data.csv', 'w') as csv_file:
		filewriter = filewriter = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
		filewriter.writerow(headers)
		for row in data:
			if row['CID'] != '':
				candidate_row = enriched_data(row)
				ordered_row = []
				for item in headers:
					ordered_row.append(candidate_row[item])
				filewriter.writerow(ordered_row) 
	print 'All done.'

new_csv('candidates.csv')