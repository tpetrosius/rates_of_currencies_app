import sqlite3

class Database_Table():

	filepath = 'C:\\Users\\Vartotojas\\Desktop\\github\\currency_app\\currencies_data.db'

	def __init__(self, table_name):
		"""Initiate database table object"""

		self.table_name = table_name

	def check_if_table_is_created(self):

		# Create SQL queries
		sql_check = "SELECT count(name) FROM sqlite_master WHERE type='table' AND name='"  + self.table_name + "';"
		sql_create_table = 'CREATE TABLE ' + self.table_name + ' (id INTEGER PRIMARY KEY, pair_name text, pair_rate real, update_date text);'

		# Connect to database
		conn = sqlite3.connect(Database_Table.filepath)
		c = conn.cursor()

		# Make SQL query to check if table exists
		c.execute(sql_check)

		# Check if table exists
		if c.fetchone()[0]==1:
			pass

		else:
			c.execute(sql_create_table)

			# Save (commit) the changes and close connection
			conn.commit()
			conn.close()

	def update_table(self, pair, rate, updated):

		# Add input values to list for SQL query
		data = []
		data.append(pair)
		data.append(rate)
		data.append(updated)

		# Create SQL query to insert new values in database table
		sql = 'INSERT INTO ' + self.table_name + ' (pair_name, pair_rate, update_date) VALUES (?,?,?);'

		# Connect to database
		conn = sqlite3.connect(Database_Table.filepath)
		c = conn.cursor()

		# Make SQL query to update database table with new data
		c.execute(sql, tuple(data))
 
		# Save (commit) the changes and close connection
		conn.commit()
		conn.close()

	def check_data_already_exists(self, date):

		# Create SQL query if values already exists in database table
		check_sql = 'SELECT * FROM ' + self.table_name + ' WHERE update_date = ?'

		# Connect to database
		conn = sqlite3.connect(Database_Table.filepath)
		c = conn.cursor()

		# Make SQL query to check if data already exists
		c.execute(check_sql, (date,))

		# Check if anything retrieved from database table
		data = c.fetchall()
		if len(data) == 0:
			exists = False

		else:
			exists = True

		return exists

	def get_latest_data(self):

		# Create SQL query to retrieve latest data from database table
		sql_select = 'SELECT * FROM ' + self.table_name + ' ORDER BY id DESC LIMIT 1;'

		# Connect to database
		conn = sqlite3.connect(Database_Table.filepath)
		c = conn.cursor()

		# Make SQL query to retrieve latest data
		c.execute(sql_select)
		data = c.fetchone()

		# Close database connection
		conn.close()

		return data