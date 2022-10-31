import csv

def creator(row , rows ,filename):

	if filename[:3] != '.csv':
		filename += '.csv'

	with open(f'Docs/{filename}' , 'w') as csvfile:
		csvwriter = csv.writer(csvfile)
		csvwriter.writerow(row)
		csvwriter.writerows(rows)