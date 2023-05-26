'========================Parsing==========================='
# парсинг - процесс автоматического сбора данных 

# Библиотеки
# 1. requests - отправляет запрос на сайт и в итоге получает html код страницы
# 2. Beautiful Soup - помогает извлечь информацию из html. Помогает обращаться к определенным тегам и вытаскивать инфо 
# 3. lxml - выступает в роли парсера для Beautiful Soup (разбивает на мелкие части и анализирует данные)

# python3 -m venv venv - создание виртуального окружение

# sorce venv/bin/activate
# . venv/bin/activate - активировавали виртуальное окружение  

import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://enter.kg/computers/noutbuki_bishkek'

def write_to_csv(data):
    with open('data.csv', 'a') as file:
        writer = csv.writer(file)
        writer.writerow([data['title'], data['price'], data['image']])

def get_html(url):
    response = requests.get(url)
    return response.text
print(get_html(URL))

def get_data(html):
    soup = BeautifulSoup(html, 'lxml')
    # return soup
    list_comp = soup.find_all('div', class_ = 'row')
    # return list_comp

    for comp in list_comp:
        title = comp.find('span', class_ = 'prouct_name').text
        price = comp.find('span', class_ = 'price').text
        image = 'https://enter.kg' + comp.find('img').get('src')
        print(image)
        dict_ = {'title':title, 'price':price,'image':image}
        write_to_csv( dict_)

print(get_data(get_html(URL)))

