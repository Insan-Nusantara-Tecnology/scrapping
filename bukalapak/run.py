import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')


@app.route('/handphone-terlaris')
def hendphone_terlaris():
	url = 'https://www.bukalapak.com/c/handphone/hp-smartphone?from=nav_header'

	req = requests.get(url)

	soup = BeautifulSoup(req.text, 'html.parser')

	phone_terlaris = soup.find(attrs= {'class': 'bl-flex-container flex-wrap is-gutter-16'})

	return render_template('index.html', titles=phone_terlaris)

if __name__== '__main__':
	app.run(debug=True)