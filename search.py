# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import csv
import os
import re

proxies = {'http': 'socks5://194.5.176.248:1080',
           'https': 'socks5://194.5.176.248:1080'}

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}




URL = f'https://hdrezka.sh/search/?do=search&subaction=search&q='
rez_all=[]

def get_html(url):
    resp = requests.get(url, headers=HEADERS, proxies=proxies)
    soup = BeautifulSoup(resp.text, 'html.parser')
    #items = soup.find_all('div', class_='b-content__inline_items')
    rez = [item['data-id'] for item in soup.find_all('div', class_='b-content__inline_item')]
    for i in rez:
        rez_all.append(i)
    return rez_all[0]






if __name__ == '__main__':
    get_html(URL)



# def get_pages_count(html):
# soup = BeautifulSoup(html, 'html.parser')
#  pagination = soup.find_all('span', class_='mhide')
# if pagination:
#      return int(pagination[-1].get_text())
#  else:
#     return 1


# cars = []
# for item in items:
#     uah_price = item.find('span', class_='grey size13')
#     if uah_price:
#         uah_price = uah_price.get_text()
#     else:
#         uah_price = 'Цены в UAH нет.'
#     cars.append({
#         'title': item.find('div', class_='proposition_title').get_text(strip=True),
#         'link': HOST + item.find('a').get('href'),
#         'usd_price': item.find('span', class_='green').get_text(strip=True),
#         'uah_price': uah_price,
#         'city': item.find('div', class_='proposition_region size13').find_next('strong').get_text(strip=True),
#     })

# return cars


# def save_file(items, path):
#     with open(path, 'w', newline='') as file:
#         writer  = csv.writer(file, delimiter=';')
#         writer.writerow(['Марка', 'Ссылка', 'Цена в $', 'Цена в UAH', 'Город'])
#         for item in items:
#             writer.writerow([item['title'], item['link'], item['usd_price'], item['uah_price'],item['city']])


# def parse():
#     URL = input(URL2)
#     URL = URL.strip()
#     html = get_html(URL)
#     if html.status_code == 200:
#         print(ok)
#         cars = []
#         pages_count = get_pages_count(html.text)
#         for page in range(1, pages_count + 1):
#             print(f'Парсится страница {page} из {pages_count}...')
#             html = get_html(URL, params={'page': page})
#             cars.extend(get_content(html.text))
#         save_file(cars, FILE)
#         print(f'Получено {len(cars)} автомобилей')
#         os.startfile(FILE)
#
#         # cars = get_content(html.text)
#     else:
#         print('Error')
