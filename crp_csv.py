import csv
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
	candidate_data['spent'] = crp_online_data['spent'] # data pulled from the api
	candidate_data['total'] = crp_online_data['total']
	candidate_data['cash on hand'] = crp_online_data['cash_on_hand']
	candidate_data['debt'] = crp_online_data['debt']
	candidate_data['updated date'] = crp_online_data['last_updated']
	return candidate_data

def new_csv(old_csv):
	data = candidate_csv(old_csv)
	# have to have a way to skip the blanks here
	for row in

print enriched_data(candidate_csv('test_candidates.csv')[0]).keys()