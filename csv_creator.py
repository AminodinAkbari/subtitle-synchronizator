import csv

"""Using csv library for creating results (csv files)"""
def creator(row , rows ,filename):

	"""add .csv to end the of name (if name have not 'csv Suffix' )"""
	if filename[:3] != '.csv':
		filename += '.csv'

	"""creating file"""
	with open(f'Docs/{filename}' , 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(row)
		csvwriter.writerows(rows)