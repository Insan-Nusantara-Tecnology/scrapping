import requests

# json_data = requests.get('https://www.floatrates.com/daily/idr.json')
# print(json_data.json())

json_rates = {
		'usd': {'code': 'USD', 'alphaCode': 'USD', 'numericCode': '840', 'name': 'U.S. Dollar', 'rate': 6.3803586773625e-05, 'date': 'Tue, 23 Jan 2024 23:55:02 GMT', 'inverseRate': 15673.10006486}, 
		'eur': {'code': 'EUR', 'alphaCode': 'EUR', 'numericCode': '978', 'name': 'Euro', 'rate': 5.8653311464107e-05, 'date': 'Tue, 23 Jan 2024 23:55:02 GMT', 'inverseRate': 17049.335749985},
	}
for data in json_rates.values():
	print(data['code'])
	print(data['name'])
	print(data['date'])
	print(data['inverseRate'])


