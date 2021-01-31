import requests
from bs4 import BeautifulSoup


class zillowScraper():

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'no-cache',
        'cookie': 'zguid=23|%248952b7b9-9915-4c78-be31-ed1e831e2f2d; zgsession=1|321ae93a-958f-4bfa-9919-bf99780428ab; _ga=GA1.2.989764791.1603411650; _gid=GA1.2.1565995536.1603411650; zjs_anonymous_id=%228952b7b9-9915-4c78-be31-ed1e831e2f2d%22; JSESSIONID=ADE149B575A279A899C2E13675D96433; _gcl_au=1.1.1423389892.1603411650; KruxPixel=true; DoubleClickSession=true; _pxvid=bda7b5b6-14c3-11eb-a446-0242ac12000b; _fbp=fb.1.1603411649990.596303551; _pin_unauth=dWlkPU9UZ3laRGczWVdNdE9HWm1NUzAwTmpaaExXRmhaRFl0TmpjMU5EZ3pORGxsWlRoaw; __gads=ID=cbe9329d7b6d5aca:T=1603411659:S=ALNI_MZNERqXQGENAFxNFZcdXyW59BeQAQ; KruxAddition=true; ki_r=; G_ENABLED_IDPS=google; ZILLOW_SID=1|AAAAAVVbFRIBVVsVElSH3JacWCpyPlPcpaToGqUuMTemWTFEVjYQNHBaW4lL92Vd8uoZ9Jhx2ROTcRZ4WyJaSENylLr9; ZILLOW_SSID=1|AAAAAVVbFRIBVVsVEv%2BdqXNEXHiRPYSSm2aaWAW4fMzcsYlwMqFzQo3yYuMXEVxvXlwEtle37u9CoP7Y6Q5qvSzeawF%2F; loginmemento=1|216c79e0baf58e642ce3d93a93ecf6883c0514ce4da56120834631d720760c3a; userid=X|3|27bdc23c45de3adb%7C6%7C7d331jp56546EzTHphU9z2GTynDJBqPDNvp3edXwSzo%3D; zjs_user_id=%22X1-ZUxtvkvyb4vpxl_6cyoo%22; ki_s=211289%3A0.0.0.0.0%3B211290%3A0.0.0.0.0%3B211291%3A0.0.0.0.2; ki_t=1603411789231%3B1603411789231%3B1603412700358%3B1%3B51; _derived_epik=dj0yJnU9WFEyMzFBSnY4YklrRXFtVlNfcjBCWmpwMmx4LVdwMjYmbj1aZ2Y3S0l1OE5PRE90THk3RlpUSl9BJm09NyZ0PUFBQUFBRi1TS2sw; _uetsid=bdbad89014c311eba14f5fba062ef613; _uetvid=bdbb0dd014c311ebab22518633abcf5d; _px3=c45dc4f1e0b96fde303f70cd0109e94c7543573d52d141bf919b9fcc85ea8f3a:hcrNTOn5T8a1bCutKO+R41c6RSPZ8PsVNK3fAvar4As/AEpxfWalJPZg41YeWVI6TNOVIz/XpdXoLp5dPTmxBw==:1000:njkkO08QaMGM1chZMYbAkrt8o4CdTYiuo9G9lePz/nx5rS3LbIwFBvoLrlo98l9lpmNumzdKEo45Y5UeA53mOO+kVIC1rrMRshSzcHl4brh0YejgkwiFoIKJzkF3B8G3of22mQuil2Wr9msJFKImnnaEDRIuHB+gocJADXGdaeA=; intercom-session-xby8p85u=TEZsemlUSEZwS0VPaFFJK0FRSHoxQVZ2cUx2b3ZaeTdlQ0NORVFaUlNqZEtJM2FLaU5Oa21CNDFieDRHWHRnRS0tQitHRWFNOTd6TTl5SVN1dVZHUnVpUT09--8022341aee1a6d42cc33058d89cce231a3706042; AWSALB=M+L1SRp6fdZ7DHCdtjbP+xjfobkNvLU3lE3K4Nf/SfcfcIHWBGAgZAha5+Q9Ti2xx3OPSwDeyArvid/3/wD6OPf89jbdwN76X2qqt3gll6RlEJPF7vpHG8rNQQaC; AWSALBCORS=M+L1SRp6fdZ7DHCdtjbP+xjfobkNvLU3lE3K4Nf/SfcfcIHWBGAgZAha5+Q9Ti2xx3OPSwDeyArvid/3/wD6OPf89jbdwN76X2qqt3gll6RlEJPF7vpHG8rNQQaC; search=6|1606006865776%7Crect%3D36.39191517166588%252C-108.69576864652903%252C33.43766374893076%252C-114.52950888090403%26rid%3D31567%26disp%3Dmap%26mdm%3Dauto%26p%3D1%26sort%3Dpricea%26z%3D1%26days%3D90%26type%3Dhouse%26hoa%3D0-0%26fs%3D0%26fr%3D0%26mmm%3D0%26rs%3D1%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D0%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%09%0931567%09%09%09%09%09%09; _gat=1',
        'pragma': 'no-cache',
        'referer': 'https://www.zillow.com/flagstaff-az/sold/house_type/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Flagstaff%2C%20AZ%22%2C%22mapBounds%22%3A%7B%22west%22%3A-112.34185629301341%2C%22east%22%3A-110.88342123441966%2C%22south%22%3A34.04404526898158%2C%22north%22%3A35.80269995244768%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A31567%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22hoa%22%3A%7B%22max%22%3A0%7D%2C%22doz%22%3A%7B%22value%22%3A%2290%22%7D%2C%22sort%22%3A%7B%22value%22%3A%22pricea%22%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22pmf%22%3A%7B%22value%22%3Afalse%7D%2C%22pf%22%3A%7B%22value%22%3Afalse%7D%2C%22rs%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%2C%22con%22%3A%7B%22value%22%3Afalse%7D%2C%22mf%22%3A%7B%22value%22%3Afalse%7D%2C%22manu%22%3A%7B%22value%22%3Afalse%7D%2C%22land%22%3A%7B%22value%22%3Afalse%7D%2C%22tow%22%3A%7B%22value%22%3Afalse%7D%2C%22apa%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A9%7D',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    def fetch(self, url, params):
        response = requests.get(url=url, headers=self.headers, params=params)
        print(response)
        return response

    def parse(self, response):
        content = BeautifulSoup(response)
        print(content.text)

    def run(self):
        url = 'https://www.zillow.com/flagstaff-az/sold'
        params = {
            "pagination": '{},"usersSearchTerm":"Flagstaff, AZ","mapBounds":{"west":-114.52950888090403,"east":-108.69576864652903,"south":33.43766374893076,"north":36.39191517166588},"regionSelection":[{"regionId":31567,"regionType":6}],"isMapVisible":true,"filterState":{"hoa":{"max":0},"doz":{"value":"90"},"sort":{"value":"pricea"},"fsba":{"value":false},"fsbo":{"value":false},"nc":{"value":false},"fore":{"value":false},"cmsn":{"value":false},"auc":{"value":false},"pmf":{"value":false},"pf":{"value":false},"rs":{"value":true},"ah":{"value":true},"con":{"value":false},"mf":{"value":false},"manu":{"value":false},"land":{"value":false},"tow":{"value":false},"apa":{"value":false}},"isListVisible":true,"mapZoom":7'}

        res = self.fetch(url, params)
        self.parse(res.text)

if __name__ == '__main__':
    scraper = zillowScraper()
    scraper.run()