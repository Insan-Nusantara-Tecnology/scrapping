import os
import json
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://id.indeed.com/jobs?'
site = 'https://id.indeed.com'
params = {
	'q': 'python developer',
	'l': 'new york',
}

headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}

res = requests.get(url, params=params, headers=headers)
print(res.status_code)

def get_total_pages(query, location):
	params = {
		'q': query,
		'l': location,
	}

	res = requests.get(url, params=params, headers=headers)

	try:
		os.mkdir('temp')
	except FileExistsError:
		pass

	with open('temp/res.html', 'w+') as outfile:
		outfile.write(res.text)
		outfile.close()

	total_pages = []
	# Scrapping Step
	soup = BeautifulSoup(res.text, 'html.parser')
	pagination = soup.find('ul', 'pagination-list')
	pages = pagination.find_all('li')
	for page in pages:
		total_pages.append(pages.text)

	total = int(max(total_pages))
	return total

def get_all_items(query, location, start, page):
	params = {
		'q': query,
		'l': location,
		'start': start,
	}
	res = requests.get(url, params=params, headers=headers)

	with open('temp/res.html', 'w+') as outfile:
		outfile.write(res.text)
		outfile.close()

	soup = BeautifulSoup(res.text, 'html.parser')

	# scrapping prosses
	contents = soup.find_all('table', 'jobCard_mainContent big6_visualChanges')
	print(contents)

	''' 
	pick item
	* title
	* compani name
	* company link
	* company addres
	'''

	job_list = []
	for item in contents:
		title = item.find('h2', 'jobTitle').text
		company = item.find('span', 'companyName')
		company_name = company.text
		try:
			company_link = site + company.find('a')['href']
		except:
			company_link = 'Link dosn\'t not available'

		# sorting data
		data_dict = {
			'title': title,
			'company_name': company_name,
			'company_link': company_link,
		}
		job_list.append(data_dict)

	# writing json file
	try:
		os.mkdir('json_result')
	except FileExistsError:
		pass

	with open('json_result/{query}_in_{location}_page_{page}.json', 'w+') as json_data:
		json.dump(job_list, json_data)
	print('json created')
	return job_list


def create_document(dataFrame, filename):
	try:
		os.mkdir('data_result')
	except:
		pass

	df = pd.DataFrame(dataFrame)
	df.to_csv(f'data_result/{filename}.csv', index=False)
	df.to_excel(f'data_result/{filename}.xlsx', index=False)

	# data created
	print(f'Data {filename} Created Sucsess')

def run():
	query = input('Enter your  Query')
	location = input('Enter your location')

	total = get_total_pages(query, location)
	
	final_result = []

	counter = 0
	for page in range(total):
		page += 1
		counter += 10
		final_result += get_all_items(query, location, counter, page)

	# formating data
	try:
		os.mkdir('reports')
	except:
		pass

	with open(f'reports/{query}.json', 'w+') as final_data:
		json.dump(final_result, final_data)

	print('data json created')

	# create document
	create_document(final_result, query)


if __name__ == '__main':
	get_all_items()

