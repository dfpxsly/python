import requests
import json
import pygal
import math
from itertools import groupby

json_url = 'https://raw.githubusercontent.com/muxuezi/btc/master/btc_close_2017.json'
req = requests.get(json_url)
with open('btc_close_2017_urllib.json', 'w') as f:
	f.write(req.text)
btc_data = req.json()

dates, months, weeks, weekdays, closes = [], [], [], [], []

for btc_dict in btc_data:
	dates.append(btc_dict['date'])
	months.append(int(btc_dict['month']))
	weeks.append(int(btc_dict['week']))
	weekdays.append(btc_dict['weekday'])
	closes.append(int(float(btc_dict['close'])))


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价（¥）'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
line_chart.add('收盘价', closes)
line_chart.render_to_file('Btc_Price.svg')


line_chart = pygal.Line(x_label_rotation=20, show_minor_x_labels=False)
line_chart.title = '收盘价log10（￥）'
line_chart.x_labels = dates
line_chart.x_labels_major = dates[::20]
close_log = [math.log10(x) for x in closes]
line_chart.add('log收盘价', close_log)
line_chart.render_to_file('Btc_Price_log10.svg')


def draw_line(x_data, y_data, title, y_legend):
	xy_map = []
	xy_list = sorted(zip(x_data, y_data)) #将x，y轴的数据合并，排序

	for key_x, group_y in groupby(xy_list, key=lambda k: k[0]): #利用groupby分组，分组依据为key
		y_list = [v for k, v in group_y]
		xy_map.append([key_x, sum(y_list)/len(y_list)]) #分组后求出每组平均值

	x_unque, y_mean= [*zip(*xy_map)] #x,y轴数据分离
	line_chart = pygal.Line()
	line_chart.title = title
	line_chart.x_labels = x_unque
	line_chart.add(y_legend, y_mean)
	line_chart.render_to_file(title+'.svg')
	return line_chart

idx_month = dates.index('2017-12-01') #获得'2017-12-01' 的索引值
line_chart_month = draw_line(months[:idx_month], closes[:idx_month], '收盘价月日均值','月日均值')


with open ('dashboard.html', 'w', encoding='utf8') as f:
	f.write('<html><head><title>收盘价Dashboard</title><meta charset="utf-8"></head><body>\n')
	for svg in ['Btc_Price.svg', 'Btc_Price_log10.svg', '收盘价月日均值.svg']:
		f.write('<object type="image/svg+xml" data="{0}" height=500> </object>\n'.format(svg))
	f.write('</body></html>')



	