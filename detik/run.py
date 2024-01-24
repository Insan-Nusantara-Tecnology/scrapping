import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/detik-populer')
def detik_populer():
	html = requests.get('https://www.detik.com/terpopuler')

	soup = BeautifulSoup(html.text, 'html.parser')

	populer = soup.find(attrs={'class': 'grid-row list-content'})
	titles = populer.find_all(attrs={'class': 'media__title'})
	images = populer.find_all(attrs={'class': 'media__image'})

	return render_template('index.html', images=images)


if __name__ == '__main__':
	app.run()
