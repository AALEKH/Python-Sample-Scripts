##Script to fetch a movie from IMDB
import urllib2
import json

## Need to add try catch block too

a = 'http://www.omdbapi.com/?t=Penguins+of+Madagascar+&y=2014&plot=short&r=json'
request = urllib2.Request(a)
response = urllib2.urlopen(request)
data = response.read()
decoded = json.loads(data)
print decoded['Title']
