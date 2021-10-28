import requests
import time
import json
import re

proxies = {'http': 'socks5://194.5.176.248:1080',
           'https': 'socks5://194.5.176.248:1080'}

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}

BASE_URL = 'https://rezka.ag/ajax/get_cdn_series/?t={}'


def parse_quality(urls, quality=None):
    splited = urls.split(',')

    if not quality:
        using_quality = splited[-1].split('http')[0]
        print('Используем максимально доступное качество ({})'.format(using_quality))
        return splited[-1].split(' or')[0].replace(using_quality, '')

    intext_quality = '[{}p]'.format(quality)

    if intext_quality not in urls:
        print('Качества {} нет в списке доступных'.format(quality))

        # тут уже я не выдержал и импортировал регекс
        available_qualities = re.findall(r'\[(.+?)\]', urls)
        print('Доступные варианты: ', ', '.join(available_qualities))
        return None

    for url in splited:
        if intext_quality in url:
            return url.split(' or')[0].replace(intext_quality, '')


def get_urls(film_id, season, episode):
    payload = {'id': film_id,
               'translator_id': '1',
               'season': season,
               'episode': episode,
               'action': 'get_stream'}

    r = requests.post(BASE_URL.format(str(int(time.time()))), data=payload, proxies=proxies, headers=HEADERS)

    if r.status_code != 200:
        # тут нужно будет как нибудь обработать ошибку, если запрос не прошел
        print('Ошибка')
        return

    data = json.loads(r.text)

    if data.get('success') != True:
        # тут нужно будет как нибудь обработать ошибку, если запрос не прошел
        print('Ошибка')
        print(data)
        return

    return data['url']


if __name__ == '__main__':

    all_urls = get_urls(9364, 1, 5)

    if all_urls:
        url = parse_quality(all_urls)

        print(url)

        