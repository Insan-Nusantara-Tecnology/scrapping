
import requests
from bs4 import BeautifulSoup
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/idr-rates')
def idr_rates():
	source = requests.get('https://www.floatrates.com/daily/idr.json')

	json_data = source.json()

	return render_template('index.html', datas=json_data.values())


if __name__ == '__main__':
	app.run(debug=True)
