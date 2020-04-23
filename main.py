from bs4 import BeautifulSoup
from requests import get


# Создать список из нужных квартир appartments = [] и циклом for проходить по каждой и возвращать данные, которые записаваются в csv


headers = ({'User-Agent':
            'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/80.0.3987.163 Chrome/80.0.3987.163 Safari/537.36'})


url = "https://r.onliner.by/pk/apartments/338743"
response = get(url, headers=headers)


html_soup = BeautifulSoup(response.text, 'lxml')

room = html_soup.find('span', {'class': 'apartment-bar__value'}).text
adress = html_soup.find('div', {'class': 'apartment-info__sub-line apartment-info__sub-line_large'}).text.strip()
price = html_soup.find('span', {'class': 'apartment-bar__price-value apartment-bar__price-value_complementary'}).text.strip()
trs = html_soup.find('tbody').find_all('tr')
tds = trs[1].find_all('td')
sq = tds[1].text.strip() 


# print(room)
print(f'{room} по адресу: {adress}\nПлощадь: {sq}, цена: {price}')
