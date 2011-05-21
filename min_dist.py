import json
from urllib.parse import urlencode
from urllib.request import urlopen

api = "http://maps.googleapis.com/maps/api/distancematrix/json?"

def min_dist(addrs):
	'Given a list of places, finds the location closest to the others.'
	matrix = get_matrix(addrs)
	return addrs[min(range(len(addrs)), key=lambda k: sum([
		get_dist(matrix, j, k) for j in range(len(addrs)) if j != k
	]))]

def get_matrix(addrs):
	'Assembles a distance matrix using Google Maps.'
	places = '|'.join(addrs)
	query = api + urlencode({
		'origins': places,
		'destinations': places,
		'sensor': 'false',
	})
	resp = urlopen(query).read()
	return json.loads(str(resp, 'utf-8'))

def get_dist(mat, j, k, metric="distance"):
	'Finds the distance from place-j to place-k.'
	# metric = 'distance' | 'duration'
	return mat['rows'][j]['elements'][k][metric]['value']
