import urllib, urllib2, requests
from secrets import API_KEY

# url = 'http://opensecrets.org/api/?method=candSummary&output=json&apikey=989a4fa91e411e9efe316ef266f3fe18&cycle=2014&cid=N00007360'

def candSummary(apikey,cid, cycle='2018', output ='json'):
	url = 'http://opensecrets.org/api/?method=candSummary&output=%s&apikey=%s&cycle=%s&cid=%s' % \
		(output,apikey,cycle, cid )
	response = requests.get(url)
	return response.json()

def candidate_details(response):
	try:
		response["response"]

