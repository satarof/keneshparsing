"""
1)	Спарсить все страницы из vesti.kg только названия новостей(title) и записать результат в csv файл
"""

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://vesti.kg/'

def write_to_csv(data):
    with open('task.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title']])

def get_html(url):
    response = requests.get(url)
    return response.text
print(get_html(URL))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    list_news = soup.find_all('div', class_ = 'itemBody')

    for titlenews in list_news:
        title = (titlenews.find('h2').text).strip()
        dict_ = {'title':title}
        write_to_csv(dict_)

def pars100p():
    count = 0
    for i in range(100):
        news_url = f'https://vesti.kg/itemlist.html?start={str(count)}'
        get_data(get_html(URL))
        count += 30


pars100p()