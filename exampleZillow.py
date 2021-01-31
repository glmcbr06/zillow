import os
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import sys
import numpy as np
import pandas as pd
import regex as re
import requests
import lxml
from lxml.html.soupparser import fromstring
import prettify
import numbers
import htmltext

pd.set_option('display.max_rows', None)

directory = os.getcwd()
dataDir = os.path.join(directory, 'data')


req_headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.8',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36'
}

with requests.Session() as s:
    # city = 'Carson-City,-NV_rb' #*****change this city to what you want*****
    # url = 'https://www.zillow.com/homes/for_sale/'+city
    state = 'Nevada_rb'
    url = 'https://www.zillow.com/homes/'+state
    url1 = 'https://www.zillow.com/nv/houses/2_p'
    url2 = 'https://www.zillow.com/nv/houses/3_p'
    url3 = 'https://www.zillow.com/nv/houses/4_p'
    url4 = 'https://www.zillow.com/nv/houses/5_p'
    url5 = 'https://www.zillow.com/nv/houses/6_p'
    url6 = 'https://www.zillow.com/nv/houses/7_p'
    url7 = 'https://www.zillow.com/nv/houses/8_p'
    url8 = 'https://www.zillow.com/nv/houses/9_p'
    url9 = 'https://www.zillow.com/nv/houses/10_p'
    url10 = 'https://www.zillow.com/nv/houses/11_p'
    url11 = 'https://www.zillow.com/nv/houses/12_p'
    url12 = 'https://www.zillow.com/nv/houses/13_p'
    url13 = 'https://www.zillow.com/nv/houses/14_p'
    url14 = 'https://www.zillow.com/nv/houses/15_p'
    url15 = 'https://www.zillow.com/nv/houses/16_p'
    url16 = 'https://www.zillow.com/nv/houses/17_p'
    url17 = 'https://www.zillow.com/nv/houses/18_p'
    url18 = 'https://www.zillow.com/nv/houses/19_p'
    url19 = 'https://www.zillow.com/nv/houses/20_p'

    r = s.get(url, headers=req_headers)
    r1 = s.get(url1, headers=req_headers)
    r2 = s.get(url2, headers=req_headers)
    r3 = s.get(url3, headers=req_headers)
    r4 = s.get(url4, headers=req_headers)
    r5 = s.get(url5, headers=req_headers)
    r6 = s.get(url6, headers=req_headers)
    r7 = s.get(url7, headers=req_headers)
    r8 = s.get(url8, headers=req_headers)
    r9 = s.get(url9, headers=req_headers)
    r10 = s.get(url10, headers=req_headers)
    r11 = s.get(url11, headers=req_headers)
    r12 = s.get(url12, headers=req_headers)
    r13 = s.get(url13, headers=req_headers)
    r14 = s.get(url14, headers=req_headers)
    r15 = s.get(url15, headers=req_headers)
    r16 = s.get(url16, headers=req_headers)
    r17 = s.get(url17, headers=req_headers)
    r18 = s.get(url18, headers=req_headers)
    r19 = s.get(url19, headers=req_headers)


soup = BeautifulSoup(r.content, 'html.parser')
soup1 = BeautifulSoup(r1.content, 'html.parser')
soup2 = BeautifulSoup(r2.content, 'html.parser')
soup3 = BeautifulSoup(r3.content, 'html.parser')
soup4 = BeautifulSoup(r4.content, 'html.parser')
soup5 = BeautifulSoup(r5.content, 'html.parser')
soup6 = BeautifulSoup(r6.content, 'html.parser')
soup7 = BeautifulSoup(r7.content, 'html.parser')
soup8 = BeautifulSoup(r8.content, 'html.parser')
soup9 = BeautifulSoup(r9.content, 'html.parser')
soup10 = BeautifulSoup(r10.content, 'html.parser')
soup11 = BeautifulSoup(r11.content, 'html.parser')
soup12 = BeautifulSoup(r12.content, 'html.parser')
soup13 = BeautifulSoup(r13.content, 'html.parser')
soup14 = BeautifulSoup(r14.content, 'html.parser')
soup15 = BeautifulSoup(r15.content, 'html.parser')
soup16 = BeautifulSoup(r16.content, 'html.parser')
soup17 = BeautifulSoup(r17.content, 'html.parser')
soup18 = BeautifulSoup(r18.content, 'html.parser')
soup19 = BeautifulSoup(r19.content, 'html.parser')


# create the first two dataframes
df = pd.DataFrame()

# all for loops are pulling the specified variable using beautiful soup and inserting into said variable

#######################   Soup    #################################
for i in soup:

    address = soup.find_all(class_='list-card-addr')

    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df['prices'] = price
    df['address'] = address
    df['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df['links'] = urls
df['links'] = df['links'].astype('str')
# remove html tags
df['links'] = df['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df['links'] = df['links'].replace('" tabindex="0"></a>', ' ', regex=True)


#######################   Soup1    #################################
df1 = pd.DataFrame()
for i in soup1:
    soup = soup1
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df1['prices'] = price
    df1['address'] = address
    df1['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup1.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df1['links'] = urls
df1['links'] = df1['links'].astype('str')
# remove html tags
df1['links'] = df1['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df1['links'] = df1['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df1, ignore_index=True)

#######################   Soup2    #################################
df2 = pd.DataFrame()

for i in soup2:
    soup = soup2
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df2['prices'] = price
    df2['address'] = address
    df2['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup2.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df2['links'] = urls
df2['links'] = df2['links'].astype('str')
# remove html tags
df2['links'] = df2['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df2['links'] = df2['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df2, ignore_index=True)

#######################   Soup3    #################################
df3 = pd.DataFrame()

for i in soup3:
    soup = soup3
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df3['prices'] = price
    df3['address'] = address
    df3['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup3.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df3['links'] = urls
df3['links'] = df3['links'].astype('str')
# remove html tags
df3['links'] = df3['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df3['links'] = df3['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df3, ignore_index=True)

#######################   Soup4    #################################
df4 = pd.DataFrame()

for i in soup4:
    soup = soup4
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df4['prices'] = price
    df4['address'] = address
    df4['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup4.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df4['links'] = urls
df4['links'] = df4['links'].astype('str')
# remove html tags
df4['links'] = df4['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df4['links'] = df4['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df4, ignore_index=True)


#######################   Soup5    #################################
df5 = pd.DataFrame()

for i in soup5:
    soup = soup5
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df5['prices'] = price
    df5['address'] = address
    df5['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup5.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df5['links'] = urls
df5['links'] = df5['links'].astype('str')
# remove html tags
df5['links'] = df5['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df5['links'] = df5['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df5, ignore_index=True)


#######################   Soup6    #################################
df6 = pd.DataFrame()

for i in soup6:
    soup = soup6
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df6['prices'] = price
    df6['address'] = address
    df6['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup6.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df6['links'] = urls
df6['links'] = df6['links'].astype('str')
# remove html tags
df6['links'] = df6['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df6['links'] = df6['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df6, ignore_index=True)

#######################   Soup7    #################################
df7 = pd.DataFrame()

for i in soup7:
    soup = soup7
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df7['prices'] = price
    df7['address'] = address
    df7['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup7.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df7['links'] = urls
df7['links'] = df7['links'].astype('str')
# remove html tags
df7['links'] = df7['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df7['links'] = df7['links'].replace('" tabindex="0"></a>', ' ', regex=True)
df = df.append(df7, ignore_index=True)


#######################   Soup8    #################################
df8 = pd.DataFrame()

for i in soup8:
    soup = soup8
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df8['prices'] = price
    df8['address'] = address
    df8['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup8.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df8['links'] = urls
df8['links'] = df8['links'].astype('str')
# remove html tags
df8['links'] = df8['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df8['links'] = df8['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df8, ignore_index=True)


#######################   Soup9    #################################
df9 = pd.DataFrame()

for i in soup9:
    soup = soup9
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df9['prices'] = price
    df9['address'] = address
    df9['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup9.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df9['links'] = urls
df9['links'] = df9['links'].astype('str')
# remove html tags
df9['links'] = df9['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df9['links'] = df9['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df9, ignore_index=True)

#######################   Soup10    #################################
df10 = pd.DataFrame()

for i in soup10:
    soup = soup10
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df10['prices'] = price
    df10['address'] = address
    df10['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup10.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df10['links'] = urls
df10['links'] = df10['links'].astype('str')
# remove html tags
df10['links'] = df10['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df10['links'] = df10['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df10, ignore_index=True)

#######################   Soup11    #################################
df11 = pd.DataFrame()

for i in soup11:
    soup = soup11
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df11['prices'] = price
    df11['address'] = address
    df11['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup11.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df11['links'] = urls
df11['links'] = df11['links'].astype('str')
# remove html tags
df11['links'] = df11['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df11['links'] = df11['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df11, ignore_index=True)

#######################   Soup12    #################################
df12 = pd.DataFrame()

for i in soup12:
    soup = soup12
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df12['prices'] = price
    df12['address'] = address
    df12['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup12.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df12['links'] = urls
df12['links'] = df12['links'].astype('str')
# remove html tags
df12['links'] = df12['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df12['links'] = df12['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df12, ignore_index=True)

#######################   Soup13    #################################
df13 = pd.DataFrame()

for i in soup13:
    soup = soup13
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df13['prices'] = price
    df13['address'] = address
    df13['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup13.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df13['links'] = urls
df13['links'] = df13['links'].astype('str')
# remove html tags
df13['links'] = df13['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df13['links'] = df13['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df13, ignore_index=True)

#######################   Soup14    #################################
df14 = pd.DataFrame()

for i in soup14:
    soup = soup14
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df14['prices'] = price
    df14['address'] = address
    df14['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup14.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df14['links'] = urls
df14['links'] = df14['links'].astype('str')
# remove html tags
df14['links'] = df14['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df14['links'] = df14['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df14, ignore_index=True)

#######################   Soup15    #################################
df15 = pd.DataFrame()

for i in soup15:
    soup = soup15
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df15['prices'] = price
    df15['address'] = address
    df15['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup15.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df15['links'] = urls
df15['links'] = df15['links'].astype('str')
# remove html tags
df15['links'] = df15['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df15['links'] = df15['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df15, ignore_index=True)

#######################   Soup16    #################################
df16 = pd.DataFrame()

for i in soup16:
    soup = soup16
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df16['prices'] = price
    df16['address'] = address
    df16['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup16.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df16['links'] = urls
df16['links'] = df16['links'].astype('str')
# remove html tags
df16['links'] = df16['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df16['links'] = df16['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df16, ignore_index=True)

#######################   Soup17    #################################
df17 = pd.DataFrame()

for i in soup17:
    soup = soup17
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df17['prices'] = price
    df17['address'] = address
    df17['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup17.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df17['links'] = urls
df17['links'] = df17['links'].astype('str')
# remove html tags
df17['links'] = df17['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df17['links'] = df17['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df17, ignore_index=True)

#######################   Soup18    #################################
df18 = pd.DataFrame()

for i in soup18:
    soup = soup18
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df18['prices'] = price
    df18['address'] = address
    df18['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup18.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df18['links'] = urls
df18['links'] = df18['links'].astype('str')
# remove html tags
df18['links'] = df18['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df18['links'] = df18['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df18, ignore_index=True)

#######################   Soup19    #################################
df19 = pd.DataFrame()

for i in soup19:
    soup = soup19
    address = soup.find_all(class_='list-card-addr')
    price = list(soup.find_all(class_='list-card-price'))
    beds = list(soup.find_all("ul", class_="list-card-details"))
    details = soup.find_all('div', {'class': 'list-card-details'})
    home_type = soup.find_all('div', {'class': 'list-card-footer'})
    last_updated = soup.find_all('div', {'class': 'list-card-top'})
    brokerage = list(soup.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
    link = soup.find_all(class_='list-card-link')

    # create dataframe columns out of variables
    df19['prices'] = price
    df19['address'] = address
    df19['beds'] = beds

# create empty url list
urls = []
# loop through url, pull the href and strip out the address tag
for link in soup19.find_all("article"):
    href = link.find('a', class_="list-card-link")
    addresses = href.find('address')
    addresses.extract()
    urls.append(href)
# import urls into a links column
df19['links'] = urls
df19['links'] = df19['links'].astype('str')
# remove html tags
df19['links'] = df19['links'].replace('<a class="list-card-link" href="', ' ', regex=True)
df19['links'] = df19['links'].replace('" tabindex="0"></a>', ' ', regex=True)

df = df.append(df19, ignore_index=True)

df.to_csv(os.path.join(dataDir, 'zillow_{}.csv'.format(state)))
print(df)
