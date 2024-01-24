import requests
from bs4 import BeautifulSoup


html = requests.get('https://www.detik.com/terpopuler')

soup = BeautifulSoup(html.text, 'html.parser')

populer = soup.find(attrs={'class': 'grid-row list-content'})
titles = populer.find_all(attrs={'class': 'media__title'})
images = populer.find_all(attrs={'class': 'media__image'})

for image in images:
	print(image.find('a').find('img')['title'])

