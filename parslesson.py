import requests
import bs4

import json
from pprint import pprint


response = requests.get('https://dtf.ru/games')
soup = bs4.BeautifulSoup(response.text, features='lxml')

articles_list = soup.findAll('div', class_="content--short")

parsed_data = []

for article in articles_list:
	link = f"https://dtf.ru{article.find("a", class_="content__link")['href']}"
	response = requests.get(link)
	soup = bs4.BeautifulSoup(response.text, features='lxml')
	title = soup.find('h1').text.strip()
	time = soup.find('time')['datetime']
	text = soup.find('article', 'content__blocks').text

	parsed_data.append({
		'title': title,
		'link': link,
		'time': time,
		'text': text
	})

# pprint(parsed_data)
with open('articles.json', 'w', encoding='utf-8') as f:
	f.write(json.dumps(parsed_data, ensure_ascii=False, indent=4))