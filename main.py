import requests
import json
from search import get_html



proxies = {'http': 'socks5://165.22.101.15:80',
           'https': 'socks5://165.22.101.15:80'}

HEADERS = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:71.0) Gecko/20100101 Firefox/71.0',
           'accept': '*/*'}
input_ser = input('Введите сериал: ')


def get_url(id, t_id, season, episode):
    '''Возвращает url видео '''
    URL = 'https://hdrezka.sh/ajax/get_cdn_series/?t=1590958856022' #const для запросов
    dict = {
             'id': id,
             'translator_id': t_id,  # озвучка
             'season': season,
             'episode': episode,
             'action': 'get_stream' #const
            }

    response = requests.post(URL, data=dict , proxies=proxies, headers=HEADERS) #сам запрос

    dict = json.loads(response.text.replace("'",'"')) #Строка в словарь
    print (dict)
    i = -1
    while dict['url'][i]!=' ':
        i-=1
    return dict['url'][i:] #Видео с лучшим качеством

Naruto = [get_html(f'https://hdrezka.sh/search/?do=search&subaction=search&q={input_ser}'), 14, 2, 37] # id сериала, озвучка,сезон , номер серии
Mr_Robot = [9364, 1, 1, 1] # id сериала, озвучка, сезон, номер серии

print('%d серия Наруто %d сезона : %s \n' % (Naruto[3], Naruto[2], get_url((*Naruto))))
print('%d серия Мистера Робота %d сезона : %s \n' % (Mr_Robot[3], Mr_Robot[2], get_url((*Mr_Robot))))