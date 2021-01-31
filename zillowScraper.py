import os
import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging.config
import locale
import numpy as np
import matplotlib.pyplot as plt
import re


# Will need a city and state lookup for zip code.


class zillowScraper():

    req_headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'zgsession=1|321ae93a-958f-4bfa-9919-bf99780428ab; _ga=GA1.2.989764791.1603411650; _gid=GA1.2.1565995536.1603411650; _gcl_au=1.1.1423389892.1603411650; KruxPixel=true; DoubleClickSession=true; _pxvid=bda7b5b6-14c3-11eb-a446-0242ac12000b; _fbp=fb.1.1603411649990.596303551; _pin_unauth=dWlkPU9UZ3laRGczWVdNdE9HWm1NUzAwTmpaaExXRmhaRFl0TmpjMU5EZ3pORGxsWlRoaw; __gads=ID=cbe9329d7b6d5aca:T=1603411659:S=ALNI_MZNERqXQGENAFxNFZcdXyW59BeQAQ; KruxAddition=true; ki_r=; G_ENABLED_IDPS=google; ki_s=211289%3A0.0.0.0.0%3B211290%3A0.0.0.0.0%3B211291%3A0.0.0.0.2; _gac_UA-21174015-56=1.1603503218.CjwKCAjw_sn8BRBrEiwAnUGJDu6a9ObFJVWJpyU4t7Yc7RsMmrdC8qYdC6cPyjMo0KUX6_S2HxemlBoCJp8QAvD_BwE; _gcl_aw=GCL.1603503219.CjwKCAjw_sn8BRBrEiwAnUGJDu6a9ObFJVWJpyU4t7Yc7RsMmrdC8qYdC6cPyjMo0KUX6_S2HxemlBoCJp8QAvD_BwE; ki_t=1603411789231%3B1603466492981%3B1603504298109%3B2%3B543; intercom-session-xby8p85u=OEZIRHR1Qm9wMXVXZFhRTSt0YTlGNEhOWnFpOVRobzVNeXNFTWFUbmtkODVZOUZZcnRZV3RlWXJUajdZMnBmUC0tb3cvbGpNMS9OZ25velBtZy80SEtTZz09--69ac4e50df6d873b7d65232702be25178741a4fe; zguid=23|%24318728a2-7f87-4e1e-aca7-4ef407110d10; zjs_anonymous_id=%22318728a2-7f87-4e1e-aca7-4ef407110d10%22; zjs_user_id=null; JSESSIONID=1DC8DDFA552F2B3E994F95F707C3656F; g_state={"i_p":1603677532305,"i_l":2}; _derived_epik=dj0yJnU9ZHI2WlA0dXh4cFJzVEZhZ0I5SU9YR1piQnNwbHAxU0Qmbj1hVHRhTlp6Mlp5bFozeTJ4YWk1Und3Jm09NyZ0PUFBQUFBRi1VNkhr; _px3=0cc850d45c3531d6966b88e557246af48f265da295eb1b128b67c1caf4ee6a54:RYTg96DBGynBkYco5oMG4x0ocJZM/n0FudiV3kkykdcUNZxvsyU1pNNFKzS1rgeNO/IYtr+EKIOy6crDJ/UlmA==:1000:cW2rGLV8ImUKqp2wGa4zoXExZJRRUwMr8fqunu0Kj6W4ejW4EnNPY3pkDYIaNglYu4AEtDAvA4NnC1DMTise/T5n6Cle0hsZiU/7ZO55dLHrX6fn7WOs9/xtzcE77TK7RHgFBvEjEPyP617oz3MpMpYqIPWzytR/lJ/80FS7/gs=; _uetsid=bdbad89014c311eba14f5fba062ef613; _uetvid=bdbb0dd014c311ebab22518633abcf5d; _gat=1; AWSALB=SvblxNRaPNyZ8QXZ7P8qCSJktg2mWh9PcMuYtu5FN/tpFJgHTNaqkrrWEy+wND/5knTLo3xlsVUSC7a6DW5fAAlevICS2aD9c4ZND56S9dq5/R+d5tSjfh4Lf8r5; AWSALBCORS=SvblxNRaPNyZ8QXZ7P8qCSJktg2mWh9PcMuYtu5FN/tpFJgHTNaqkrrWEy+wND/5knTLo3xlsVUSC7a6DW5fAAlevICS2aD9c4ZND56S9dq5/R+d5tSjfh4Lf8r5; search=6|1606187039450%7Crect%3D45.501231628567325%252C-122.51335090441893%252C45.465967881666984%252C-122.60450309558104%26rid%3D99159%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26z%3D1%26days%3D30%26fs%3D0%26fr%3D0%26mmm%3D0%26rs%3D1%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0999159%09%09%09%09%09%09',
        'pragma': 'no-cache',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'




    }

    def fetch(self, url):

        with requests.Session() as s:

            r = s.get(url, headers=self.req_headers)
            print(r)
            return r

    def parse(self, response):
        df = pd.DataFrame()
        content = BeautifulSoup(response, 'html.parser')
        # for i in content:

        address = [i.string for i in content.find_all(class_='list-card-addr')]
        price = [i.string for i in list(content.find_all(class_='list-card-price'))]
        bbsq = list(content.find_all("ul", class_="list-card-details"))
        # details = [i.string for i in content.find_all('div', {'class': 'list-card-details'})]
        home_type = [i.span.text for i in content.find_all('div', {'class': 'list-card-footer'})]
        last_updated = content.find_all('div', {'class': 'list-card-top'})
        brokerage = list(content.find_all(class_='list-card-brokerage list-card-img-overlay', text=True))
        sold = [i.string for i in list(content.find_all(class_='list-card-variable-text list-card-img-overlay', text=True))]

        link = content.find_all(class_='list-card-link')
        # create dataframe columns out of variables
        df['prices'] = price
        df['address'] = address
        df['bedBathFeet'] = bbsq
        # df['details'] = details
        df['home_type'] = home_type
        df['lat_updated'] = last_updated
        df['sold'] = sold
        # df['brokerage'] = brokerage
        return df

    def run(self, url):
        # Todo: this needs to be customizable for different areas...
        res = self.fetch(url)
        df = self.parse(res.text)
        return df

def getBedsFromString(string):

    lst = re.split('bds|ba|sqft', string)

    if len(lst) == 4:

        beds = re.search('<li>(.+?)<abbr', lst[0]).group(1)
        if beds.isdigit():
            beds = int(beds)
        else:
            beds = None
    else:
        beds = None
    return beds


def getBathsFromString(string):
    lst = re.split('bds|ba|sqft', string)
    if len(lst) == 4:
        baths = float(re.search('<li>(.+?)<abbr', lst[1]).group(1))
    else:
        baths = None
    return baths


def getFeetFromString(string):
    lst = re.split('bds|ba|sqft', string)

    if len(lst) == 4:
        feet = float(re.search('<li>(.+?)<abbr', lst[2]).group(1).replace(',', ''))

    else:
        feet = None
    return feet


def main(args):

    # DEFINE THE ARGS
    directory = args.directory
    dataDir = os.path.join(directory, 'data')

    # CREATE AN EMPTY DATAFRAME
    df = pd.DataFrame(columns=['price', 'address', 'bed', 'bath', 'sqft'])
    # url = 'https://www.zillow.com/portland-or-97266/sold/house_type/'
    fname = os.path.join(dataDir, 'sold_97266.csv')
    if not os.path.exists(fname):
        pages = 20
        scraper = zillowScraper()
        for i in range(pages):
            num = i + 1
            pg = str(num) + str('_p')
            zillow = 'https://www.zillow.com/portland-or-97266/sold/'
            query1 = '?searchQueryState=%7B%22mapBounds%22%3A%7B%22west%22%3A-122.652224958374%2C%22east%22%3A-122.46992057604979%2C%22south%22%3A45.45296407284594%2C%22north%22%3A45.52348576595561%7D%2C%22mapZoom%22%3A12%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A99159%2C%22regionType%22%3A7%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22pagination%22%3A%7B%7D%7D'

            query2 = '?searchQueryState=%7B"mapBounds"%3A%7B"west"%3A-122.652224958374%2C"east"%3A-122.46992057604979%2C"south"%3A45.45296407284594%2C"north"%3A45.52348576595561%7D%2C"mapZoom"%3A12%2C"regionSelection"%3A%5B%7B"regionId"%3A99159%2C"regionType"%3A7%7D%5D%2C"isMapVisible"%3Atrue%2C"filterState"%3A%7B"pmf"%3A%7B"value"%3Afalse%7D%2C"fore"%3A%7B"value"%3Afalse%7D%2C"ah"%3A%7B"value"%3Atrue%7D%2C"sort"%3A%7B"value"%3A"globalrelevanceex"%7D%2C"auc"%3A%7B"value"%3Afalse%7D%2C"nc"%3A%7B"value"%3Afalse%7D%2C"rs"%3A%7B"value"%3Atrue%7D%2C"fsbo"%3A%7B"value"%3Afalse%7D%2C"cmsn"%3A%7B"value"%3Afalse%7D%2C"pf"%3A%7B"value"%3Afalse%7D%2C"fsba"%3A%7B"value"%3Afalse%7D%7D%2C"isListVisible"%3Atrue%2C"pagination"%3A%7B"currentPage"%3A2%7D%7D'
            if num == 0:
                url = zillow + query1
                tmp = scraper.run(url)
                df = df.append(tmp, ignore_index=True)
                print(df)
                exit()
            elif num > 0:
                url = zillow + pg + query2
                tmp = scraper.run(url)
                df = df.append(tmp, ignore_index=True)
            else:
                print('did not work....')
        df.to_csv(fname)
    else:
        df = pd.read_csv(fname, index_col=0)

    df['prices'] = df['prices'].apply(lambda x: int(str(x[1:]).replace(',', '')))
    df['dates'] = df['sold'].apply(lambda x: pd.to_datetime(str(x).split(' ')[1]))
    df['beds'] = df['bedBathFeet'].apply(lambda x: getBedsFromString(x))
    df['baths'] = df['bedBathFeet'].apply(lambda x: getBathsFromString(x))
    df['feet'] = df['bedBathFeet'].apply(lambda x: getFeetFromString(x))

    f, ax = plt.subplots()
    ax.scatter(df['baths'], df['feet'])

    plt.show()

    print(df['beds'])



if __name__ == '__main__':

    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('--directory', help='directory to save the data')
    parser.add_argument("-v", action='store_true', help="Show DEBUG log")
    parsedArgs = parser.parse_args()

    if parsedArgs.v:
        logging.basicConfig(level=logging.DEBUG)
    else:
        logging.basicConfig(level=logging.INFO)
    main(parsedArgs)






