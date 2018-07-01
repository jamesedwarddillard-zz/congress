import urllib, urllib2, requests
from secrets import API_KEY

cid ='N00007360'

def candidate_summary(apikey,cid, cycle='2018', output ='json'):
	url = 'http://opensecrets.org/api/?method=candSummary&output=%s&apikey=%s&cycle=%s&cid=%s' % \
		(output,apikey,cycle, cid )
	response = requests.get(url)
	return response.json()

def candidate_details(response):
	details =response['response']['summary']['@attributes']
	return details

print candidate_details(candidate_summary(API_KEY, cid))