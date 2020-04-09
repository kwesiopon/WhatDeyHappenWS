import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

url = 'http://web.mta.info/developers/turnstile.html'
base = 'http://web.mta.info/developers/'

response = requests.get(url)
soup = BeautifulSoup(response.text,'html.parser')
for onetag in soup.find_all('a',href=True):
    if not onetag['href'].startswith('data/nyct/'):continue
    link = urljoin(base,onetag['href'])
    print(link)
