import requests
from datetime import datetime

def get_pairs_rates():
	"""Get latest data of currency pairs"""

	# List of currencies pairs that data needs to be extracted
	pairs = ['EURUSD', 'USDEUR', 'USDJPY', 'USDGBP', 'USDCHF', 'USDAUD', 'USDCAD']

	# Dictionary that will be populated with latest data of curencies pairs
	pairs_rates = {}

	# Loop list of pairs 
	for pair in pairs:
		# Make an API call to receive JSON data
		url = 'https://www.freeforexapi.com/api/live?pairs=' + pair
		response = requests.get(url)

		# If API call failed populate empty values to dictionary
		if response.status_code != 200:
			pairs_rates[pair] = {
							'rate' : 'NULL',
							'updated' : 'NULL'
							}

		# Manipulate received JSON data and populate values to dictionary
		else:
			pair_info = response.json()
			rate = pair_info['rates'][pair]['rate']
			updated = datetime.fromtimestamp(pair_info['rates'][pair]['timestamp']).strftime('%Y-%m-%d %H:%M:%S')

			pairs_rates[pair] = {
								'rate' : rate,
								'updated' : updated
								}

	return pairs_rates