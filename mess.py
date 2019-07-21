import requests
from bs4 import BeautifulSoup
import os
import re

details = {'login':'f20170359', 'password':''}
url_login = 'http://swd.bits-hyderabad.ac.in/checklogin.php?'
request_url = 'http://swd.bits-hyderabad.ac.in/home.php'

session = requests.Session()
post = session.post(url_login, data = details)
source = session.get(request_url+'#mess').text

soup = BeautifulSoup(source,'lxml')
table = soup.find('div', class_= 'table-responsive')


list1 = [x.text for x in table.find_all('th')]

import pandas as pd
pd.set_option('display.max_colwidth', -1)
df = pd.DataFrame(columns = list1, index = [0,1])

for index, row in enumerate(table.find_all('tr')[2:5], start = 0):
    
    for i, column in enumerate(row.find_all('td'),start = 0):
        string = column.text
        string = re.sub(r'\r\n', ', ',string)
        df.iat[index,i] = string
    
df.to_html('mess.html', col_space = 10, border = 1, index = False, justify = 'center')
os.startfile("mess.html")

session.close()



