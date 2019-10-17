from exchange_rates_api import get_pairs_rates
from database_table_class import Database_Table
import tkinter as tk
import datetime

pairs = ['EURUSD', 'USDEUR', 'USDJPY', 'USDGBP', 'USDCHF', 'USDAUD', 'USDCAD']
rates = {}
now = ''

def get_new_data():
	""" Make API call for all currencies pairs, store data in database, 
	get the latest data from databse and show it in tkinter. """
	global pairs
	global rates
	global now

	# Make API calls and get currencies rates data.
	pairs_rates = get_pairs_rates()

	# Loop each currency pair and add data to database
	for pair_name in pairs_rates:

		table_name = pair_name
		rate = pairs_rates[pair_name]['rate']
		updated = pairs_rates[pair_name]['updated']

		table = Database_Table(table_name)
		table.check_if_table_is_created()
		table.update_table(pair_name, rate, updated)

	# Get the latest data from database table for each currencies pair.
	for pair in pairs:
		table = Database_Table(pair)
		data = table.get_latest_data()
		rates[pair] = {
		    			'rate' : data[2],
		    			'updated' : data[3]
		    			}

	# Get date and time when data was extracted from database.
	now = str(datetime.datetime.now().strftime('%Y-%m-%d %H:%M'))

def combine_text():
	""" Combine text which will be shown in tkinter. """

	text_to_show = ('EUR/USD' + '     ' +  str(rates['EURUSD']['rate']) + '\n\n' +
		'USD/EUR' + '     ' +  str(rates['USDEUR']['rate']) + '\n\n' +
		'USD/JPY' + '     ' +  str(rates['USDJPY']['rate']) + '\n\n' +
		'USD/GBP' + '     ' +  str(rates['USDGBP']['rate']) + '\n\n' +
		'USD/CHF' + '     ' +  str(rates['USDCHF']['rate']) + '\n\n' +
		'USD/AUD' + '     ' +  str(rates['USDAUD']['rate']) + '\n\n' +
		'USD/CAD' + '     ' +  str(rates['USDCAD']['rate']) + '\n\n\n' +
		'Data Updated   ' + now + '\n')

	return text_to_show

get_new_data()

text_to_show = combine_text()

# Create tkinter 
root = tk.Tk()

def update_rates():
	"""Update data in tkinter"""
	get_new_data()
	text_to_show = combine_text()
	w1.config(text=text_to_show)

# Title of tkinter.
root.title('Rates of Currencies')
# Size of tkinter window.
root.geometry("300x300")
frame = tk.Frame(root)
frame.pack()

# Show combine text in tkinter.
w1 = tk.Label(root, text=text_to_show, fg='black')
w1.pack(fill=tk.X)

# Button that pressed updates data shown in tkinter window.
data_update = tk.Button(root, text='Update Data', command=update_rates).pack()
w1.pack()

tk.mainloop()
