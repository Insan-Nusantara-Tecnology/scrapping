from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.bukalapak.com/c/handphone/hp-smartphone?from=nav_header'

req = requests.get(url)
# print(req)

soup = BeautifulSoup(req.text, 'html.parser')

phone_terlaris = soup.find(attrs= {'class': 'bl-flex-container flex-wrap is-gutter-16'})


# print(phone_terlaris)
# print(image)

file = open('hasil_convert.csv', 'w', newline='')
writer = csv.writer(file)
headers = ['Nama Toko', 'Nama Produk', 'Harga']
writer.writerow(headers)

for item in phone_terlaris:
	# print(item.find('a', 'bl-link').text) # judul
	# print(item.find('img')['src']) # gambar
	# print(item.find('p', 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1').text) # harga
	# print(item.find('span', 'bl-product-card__store bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1').find('a', 'bl-link')['href'])
	# toko = item.find('span', 'bl-product-card__store bl-text bl-text--body-14 bl-text--subdued bl-text--ellipsis__1').find('a', 'bl-link').text
	produk = item.find('a', 'bl-link').text
	harga = item.find('p', 'bl-text bl-text--subheading-20 bl-text--semi-bold bl-text--ellipsis__1').text
	image = item.find('img')['src']

	file = open('hasil_convert.csv', 'a', newline='', encoding='utf-8')
	writer = csv.writer(file)
	writer.writerow([toko, produk, harga])
	file.close()

	with open('images/'+ produk + '.jpg', 'wb') as f:
		img =  requests.get(image)
		f.write(img.content)
