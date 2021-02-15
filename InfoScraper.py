import requests
from bs4 import BeautifulSoup
import os

url = 'https://www.walmart.ca/en/ip/rockstar-sugar-free-energy-drink/6000196142125'

def imagedown(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(),folder))
    
    except:
        pass
    
    os.chdir(os.path.join(os.getcwd(),folder))
    r = requests.get(url)

    soup = BeautifulSoup(r.text, 'html.parser')

    print(soup.title.text)

    images = soup.find_all('img')

    counter=0

    for image in images:
        name='images'
        link = image['src']
        
        with open(str(counter) + '.jpg', 'wb') as f:
            im = requests.get(link)
            f.write(im.content)

        counter+=1

upc = '3338360004'
imagedown('https://www.walmart.ca/search?q='+upc, 'check')

html = requests.get('https://www.walmart.ca/search?q=5580024882')
bsobj = BeautifulSoup(html.content,'lxml')

items_names = []

bsobj.findAll('span',{'class':'css-s3vnpn esdkp3p2'})[0].findAll('span',{'class':'aria-label'})[0].text
