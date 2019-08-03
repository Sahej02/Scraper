import pandas as pd
import requests
from bs4 import BeautifulSoup
import re
import os
#import sys

def find():
	city = str(input("Please enter city name:\n")) #sys.argv[1] #
	city = city.lower()
	list1 = [x for x in city]
	list1[0] = list1[0].upper()
	city = ''.join(list1)

	address = "https://www.weatheronline.in/India/"+ city +".htm"

	source = requests.get(address).text
	soup = BeautifulSoup(source, 'lxml')
	table = soup.find('table', class_= 'gr1')
	heading = soup.find('tr')
	rows = table.find_all('tr')[1:]

	index = []
	for row in rows:
	    index.append(row.find('td').text)
	index1 = []
	for item in index:
	    item = re.sub(r'[^A-Za-z]', '', item)
	    index1.append(item)

	heads = heading.text.split('\n')
	pd.set_option('display.max_colwidth', -1)
	df = pd.DataFrame(columns = heads, index = index1)
	df.drop(df.columns[0], axis=1, inplace = True)
	df.drop(df.columns[0], axis=1, inplace = True)

	for index, row in enumerate(table.find_all('tr')[1:3]):
	    
	    for i, column in enumerate(row.find_all('td')[1:], start = 0):
	        df.iloc[index,i] = column.text

	for index, row in enumerate(table.find_all('tr')[3:7],start = 2):
	    for i, column in enumerate(row.find_all('td')[1:], start = 0):
	        img = column.find('img')
	        df.iloc[index,i] = img['title']

	#df.to_csv('weather.csv', index = False, header = None)
	#print()
	#print()
	#print(df)
	df.to_html('weather.html', col_space = 100, border = 2)
	os.startfile("weather.html")
	#time.sleep(10)

if __name__ == '__main__':
	find()