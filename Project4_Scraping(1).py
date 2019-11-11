#!/usr/bin/env python
# coding: utf-8

# In[5]:


print('# importing models')
import requests
from bs4 import BeautifulSoup
import time
import re

pages = range(10)
# there are actually 1014 pages range(1014)

#getting the data from the website
print('scraping data from meqasa.com')
responses = []
for page in pages:
    response = requests.get('https://meqasa.com/houses-for-rent-in-ghana?w={}'.format(page+1))
    responses.append(response)
    print('{}->{}'.format(page,response.status_code))
    time.sleep(0.5)
    
len(responses)

#converting the list into a string
print('converting into a string')
count = 0
res = ''
for each in responses:
    count = count +1
    res = res + each.text
#     if count == 10:
#         break
    print(count)

#parsing the string to a beautifulSoup object
soup = BeautifulSoup(res, 'lxml')
results = soup.find_all('div', attrs={'class':'mqs-featured-prop-inner-wrap'})
print('parsing into BeautifulSoup')

# An exception function for garage and area
def c(x):
    'if the results is empty, return nothing'
    if x == None:
        return 0
    else:
        return x.span.text
    
# An exception function for price and rent_period
def test_price(x):
    'if the results is empty, return nothing'
    if x == None:
        return 0
    else:
        return x.group(1)
    
#regular expressions
price_regex = r".(\d+[,\d+]*)"
currency_regex = r".\w+(GH₵|[$])"
month_regex = r"(/\d*\s.\w+)"
print('regular expression counter')
#constructing a list of all the results    
records = []
for result in results:
    property_name = result.find('a').img['title'].split(',')[0]
    beds = result.find('li', class_='bed').find('span').text
    showers = result.find('li', class_='shower').find('span').text
    garages = c(result.find('li', class_='garage'))
    area = c(result.find('li', attrs={'class':'area'}))
    description = result.find('p', class_ = None).text
    price = test_price(re.search(price_regex, result.find('p').text, re.MULTILINE | re.IGNORECASE))
    currency = test_price(re.search(currency_regex, result.find('p', attrs = {'span class':None}).text, re.MULTILINE | re.IGNORECASE))
    rent_period = test_price(re.search(month_regex, result.find('p').text, re.MULTILINE | re.IGNORECASE))
    url = 'www.meqasa.com' + result.find('a')['href']
    address = result.find('a').img['title'].split('at')[1]
    time_posted = result.find('p', attrs={'class':'wsnr'}).text
    records.append((property_name, beds, showers, garages, area, description, price, currency, rent_period, url, address, time_posted))

print('changing into a list for dataframe')
    
#constructing the dataFrame
import pandas as pd
df = pd.DataFrame(records, columns=['property_name', 'beds', 'showers', 'garages', 'area', 'description', 'price', 'currency', 'rent_period', 'url', 'address', 'time_posted'])
print('constructing DataFrame')
print(df.head())

#writing to a csv format
print('writing to csv format with pandas')
df.to_csv('meqasa_records.csv', index=False, encoding='utf-8')


# In[ ]:




