import requests
from bs4 import BeautifulSoup
import csv

URL = 'http://kenesh.kg/ru/news/all/list'

def csv_code(data):
    with open('kenesh.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['image'], data['date'], data['title'], data['description']])

def html_code(link):
    source = requests.get(link)
    return source.text

def get_data(html):
    sp = BeautifulSoup(html, 'lxml')
    list_news = sp.find_all('div', class_="news__item news__item__3")


    for news in list_news:
        image = 'http://kenesh.kg/' + news.find('img').get('src') if news.find('img') != None else 'None'
        date = news.find('div', class_="news__item__date").text
        title = news.find('h3', class_="news__item__title").text
        description = news.find('p',class_="news__item__desc").text if news.find('p') != None else news.find('a', class_="news__item__title__link").text
        dict_ = {'image':image, 'date': date,'title':title, 'description':description}
        csv_code(dict_)


def pars20p():
    count = 1
    for i in range(21):
        news_url = f'http://kenesh.kg/ru/news/all/list?page={str(count)}'
        # get_data(html_code(URL))
        get_data(html_code(news_url))

        count += 15
        
pars20p()
