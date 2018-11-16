from bs4 import BeautifulSoup
import requests
from urllib import request
import os
# 线程库
import threading

BASE_PACE_URL = 'http://www.doutula.com/photo/list/?page='
PACE_URL_LIST = []
FACE_URL_LIST = []

# 线程锁
gLock = threading.Lock()


for i in range(1, 30):
    url = BASE_PACE_URL + str(i)
    PACE_URL_LIST.append(url)

def download_images(url, savaPath='images'):
    split_list = url.split('/')
    fileName = split_list.pop()
    path = os.path.join(savaPath, fileName)
    request.urlretrieve(url, filename=path)

def procuder():
    while True:
        gLock.acquire()
        if len(PACE_URL_LIST) == 0:
            gLock.release()
            break
        else:
            page_url = PACE_URL_LIST.pop()
            gLock.release()

            reaponse = requests.get(page_url)
            content = reaponse.content
            soup = BeautifulSoup(content, 'lxml')
            img_list = soup.find_all('img', attrs={'class': 'img-responsive lazy image_dta'})
            gLock.acquire()
            for img in img_list:
                FACE_URL_LIST.append(img['data-original'])
            gLock.release()

def customer():
    while True:
        gLock.acquire()
        if len(FACE_URL_LIST) == 0:
            gLock.release()
            continue
        else:
            face_url = FACE_URL_LIST.pop()
            gLock.release()
            split_list = face_url.split('/')
            fileName = split_list.pop()
            path = os.path.join('images', fileName)
            request.urlretrieve(face_url, filename=path)


def main():
    for x in range(3):
        th = threading.Thread(target=procuder)
        th.start()

    for x in range(5):
        th = threading.Thread(target= customer)
        th.start()



if __name__ == '__main__':
    main()




