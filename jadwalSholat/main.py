from bs4 import BeautifulSoup
import requests

url = 'https://jadwalsholat.org/jadwal-sholat/monthly.php?id=232'
contents = requests.get(url)
# print(contents.text)

soup = BeautifulSoup(contents.text, 'html.parser')
jadwalSekarang = soup.find_all('tr', 'table_highlight')
data = jadwalSekarang[0]

sholat = {}
for time in data:
	print(time.get_text())
