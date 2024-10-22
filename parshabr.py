import requests
import bs4
import time
import json
from pprint import pprint
from fake_headers import Headers


headers = Headers(browser='chrome', os='windows').generate()
url = 'https://habr.com/ru/articles'
response = requests.get(url, headers=headers)
soup = bs4.BeautifulSoup(response.text, features='lxml')
articles = soup.find_all('article', class_='tm-articles-list__item')


KEYWORDS = ['дизайн', 'фото', 'web', 'python', 'IT-компании', 'Зарабатывать', 'Glarus']
KEYWORDS = set(map(str.lower, KEYWORDS))


parsed_data = []

for article in articles:
	#Название статьи
	title_element = article.find('a', class_='tm-title__link')
	title = title_element.text
	title_set = set(map(str.lower, title.strip().split()))

	#Ссылка
	link = f"https://habr.com{title_element['href']}"

	#Дата
	date = article.find('time')['datetime'][:10]

	#Хабы
	hubs_element = article.find_all('a', class_='tm-publication-hub__link')
	hubs_set = set([hub.find('span').text.lower() for hub in hubs_element])

	#Текст
	text_element = article.find('div', class_='article-formatted-body')
	text_set = set(text_element.text.lower().strip().split())

	if KEYWORDS & title_set or KEYWORDS & hubs_set or KEYWORDS & text_set:
		parsed_data.append({
			"Дата": date,
			"Заголовок": title,
			"Ссылка": link
		})

pprint(parsed_data)





