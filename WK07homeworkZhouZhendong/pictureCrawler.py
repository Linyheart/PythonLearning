import requests
from bs4 import BeautifulSoup
import re
import os

picurl = "http://xteaching.com/book2019/images/"


def download_picture(url):
    request = requests.get(url)
    request.encoding = 'utf-8'
    soup = BeautifulSoup(request.text, 'lxml')
    xml = soup.find_all('a', clsss_='')
    pictures_label = []
    for xml_label in xml:
        if re.match('^(BingWallpaper).*(\.jpg)$', xml_label['href']):
            pictures_label.append(xml_label)
    folder_path = "c:\\BingWP\\"
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
    for picture in pictures_label:
        request_picture = requests.get(url + picture['href'])
        if request_picture.status_code == 200:
            if int(request_picture.headers['Content-Length'])/1024 < 500:
                with open(picture['href'], 'wb') as picture_file:
                    picture_file.write(request_picture.content)
                picture_path = folder_path + picture['href']
                with open(picture_path, 'wb') as picture_file:
                    picture_file.write(request_picture.content)


download_picture(picurl)