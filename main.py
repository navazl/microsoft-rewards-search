import json
from datetime import date, timedelta
from random import randint
import pyautogui as pg
import requests
import time

def wait_write_and_enter():
    time.sleep(1)
    pg.press('enter')
    time.sleep(2)

def bingSearch(numberOfSearchs: int):
    i = 0
    search_terms = getGoogleTrends(numberOfSearchs)
    for word in search_terms:
        if i == 40:
            time.sleep(2)
            pg.hotkey('f12')
            time.sleep(3)
            pg.hotkey('ctrl', 'shift', 'm')

        i += 1
        print('[BING]', str(i) + "/" + str(numberOfSearchs))
        pg.hotkey('alt', 'd')
        pg.hotkey('altright', 'w')
        pg.write(word)
        print(word)
        wait_write_and_enter()

def getGoogleTrends(numberOfwords: int) -> list:
    search_terms = []

    b = date.today() - timedelta(days = 0)

    print('getting Google Trends')
    r = requests.get('https://trends.google.com/trends/api/dailytrends?hl=en_US&ed=' + b.strftime(
        '%Y%m%d') + '&geo=' + 'US' + '&ns=15')
    google_trends = json.loads(r.text[6:])
    for topic in google_trends['default']['trendingSearchesDays'][0]['trendingSearches']:

        search_terms.append(topic['title']['query'].lower())
        for related_topic in topic['relatedQueries']:
            search_terms.append(related_topic['query'].lower())
    search_terms = list(set(search_terms))

    i = 0
    while len(search_terms) < numberOfwords:
        random_words = ['cavalo', 'sofa', 'chão', 'marrom', 'cabelo', 'videos', 'parede', 'gato', 'céu', 'cachorro', 'batata', 'pato', 'nootbook', 'espelho', 'eletrodomestico']
        random = randint(0, len(random_words) - 1)
        print(random)
        search_terms.append(search_terms[i] + ' ' + random_words[random])
        i += 1

    print(len(search_terms))

    del search_terms[numberOfwords:(len(search_terms)+1)]
    return search_terms

def getRelatedTerms(word: str) -> list:
    try:
        r = requests.get('https://api.bing.com/osjson.aspx?query=' + word)
        return r.json()[1]
    except:
        return []


pg.press('win')

time.sleep(3)

pg.write('edge')

time.sleep(3)

pg.press('enter')

time.sleep(3)

pg.write('Comecando a pesquisar')

time.sleep(4)

wait_write_and_enter()

bingSearch(70)

