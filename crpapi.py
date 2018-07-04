import urllib, urllib2, requests, csv
from secrets import API_KEY

# These functions work with the Center for Responsible Politics API to isolate data on a per candidate basis

def candidate_summary(apikey,cid, cycle='2018', output ='json'):
	# calls the CRP API for a specific method
	url = 'http://opensecrets.org/api/?method=candSummary&output=%s&apikey=%s&cycle=%s&cid=%s' % \
		(output,apikey,cycle, cid )
	response = requests.get(url)
	return response.json()

def candidate_details(response):
	# parses the response for the candidate summary method
	details =response['response']['summary']['@attributes']
	return details