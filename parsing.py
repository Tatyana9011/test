
from bs4 import BeautifulSoup

""" передаем в функцию штмл страницу и ищем там теги див с нужными нам атрибутами"""


def parse(html_data):
    soup = BeautifulSoup(data, 'lxml')

    reviews = soup.findAll('div', attrs={'class': 'review'})
    for review in reviews:
        print(review.find('div', attrs={'class': 'name'}).text)


""" open используют для открития документа, первый арг путь, второй мод для чего хотим открыть('r' - для чтерия, для записей , третий арг кодировка) """
""" управление над файлом мы засунули в переменную file """
file = open('./index.html', 'r', encoding='utf-8')
""" открытий файл ми счивываем командой read() """
data = file.read()
""" закрываем открытий файл что бы его потом еще раз можно было открыть """
file.close()
""" выводим данные? которые мы считали print(data)"""
soup = BeautifulSoup(data, 'lxml')

reviews = soup.findAll('div', attrs={'class': 'review'})
for review in reviews:
    print(review.find('div', attrs={'class': 'name'}).text)

parse(data)
