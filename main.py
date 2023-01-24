from random import randint
import pyautogui as pg
import time


def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words

def get_words(number_of_search):
    words = []
    english_words = load_words()
    list_words = list(english_words)
    for i in range(number_of_search):
        words.append(list_words[randint(0, len(list_words))])

    return words


def bing_search(numberOfSearchs, browser):
    i = 0
    search_terms = get_words(numberOfSearchs)

    for word in search_terms:
        sleep = 1
        if i == 33:
            time.sleep(2)
            pg.hotkey('ctrl', 'shift', 'i')
            time.sleep(2)

        i += 1
        print('[BING]', str(i) + "/" + str(numberOfSearchs))
        pg.hotkey('alt', 'd')
        time.sleep(0.2 * sleep)
        pg.write(word)
        print(word)
        time.sleep(0.7 * sleep)
        pg.press('enter')
        time.sleep(0.5 * sleep)

def search_browser(browser):
    pg.press('win')
    time.sleep(3)
    pg.write(browser)
    time.sleep(3)
    pg.press('enter')
    time.sleep(6)
    bing_search(55, browser)
    pg.hotkey('alt', 'd')
    pg.write('https://rewards.bing.com')
    time.sleep(1.5)
    pg.press('enter')
    time.sleep(1.5)



if __name__ == '__main__':
    navegadores = ["edge", "opera browser", "opera gx"]
    for navegador in navegadores:
        search_browser(navegador)
