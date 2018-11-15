from bs4 import BeautifulSoup
import requests
from urllib import request
import os
BASE_PACE_URL = 'http://www.doutula.com/photo/list/?page='
PACE_URL_LIST = []

def download_images(url, savaPath='images'):
    split_list = url.split('/')
    fileName = split_list.pop()
    path = os.path.join(savaPath, fileName)
    request.urlretrieve(url, filename=path)



reaponse = requests.get('http://www.doutula.com/photo/list/?page=1')
content = reaponse.content
soup = BeautifulSoup(content, 'lxml')
img_list = soup.find_all('img', attrs={'class':'img-responsive lazy image_dta'})
for img in img_list:
    download_images(img['data-original'])


#for i in range(1,2019):
    #url = BASE_PACE_URL + i


