import csv
from matplotlib import pyplot as plt
from datetime import datetime as dt

filename='death_valley_2014.csv'

with open(filename) as f:
	reader = csv.reader(f)
	reader_row = next(reader)
	print(reader_row)

	for idx, column_head in enumerate(reader_row):
		print(idx, column_head)

	high_temperatures, low_temperatures, dates = [], [], []
	for row in reader:
		try:
			cur_data = dt.strptime(row[0],'%Y-%m-%d')
			high = int(row[1])
			low = int(row[3])
		except ValueError:
			print(cur_data,'missing data!')
		else:
			dates.append(cur_data)
			high_temperatures.append(high)
			low_temperatures.append(low)


	fig = plt.figure(figsize=(10, 6), dpi=128)
	plt.plot(dates, high_temperatures, c='red', alpha=0.5)
	plt.plot(dates, low_temperatures, c='blue', alpha=0.5)

	plt.fill_between(dates, high_temperatures, low_temperatures, facecolor='green', alpha=0.1)

	plt.title('Daily high and low temperatures, 2014', fontsize=24)
	plt.xlabel('', fontsize=16)
	fig.autofmt_xdate()
	
	plt.ylabel('Temperature(F)', fontsize=16)
	plt.tick_params(axis='both', width=2, colors='gold', labelsize=16)

	plt.show()