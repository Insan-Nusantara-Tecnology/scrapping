import requests, json, time, csv

url = 'https://www.instagram.com/api/graphql'

short_code = input('Please enter a short code:')

end_cursor = ''
count = 0
counter_file = 1
jumlah_per_file = 1000

write = csv.writer(open('hasil_comments/{} {}.csv'.format(short_code, counter_file), 'w', newline=''))
headers = ['User Name', 'Comments']
write.writerow(headers)

while 1:
	var = {'shortcode': short_code, 'first':50, 'after': end_cursor}

	params = {
		'query_hash': 'NAcP8lkHtMwTQReJAqBMUqDr1nsGwuDIyM7JnjBqOYEk_7uomUKPmQA:17843683195144578:1707751053'
		'variables': json.dumps(var)
	}

	r = requests.get(url, params=params).json()
	# print(r)

	try:
		users = r['data']['shortcode_media']['edge_media_to_parent_comment']['edges']
	except:
		print('Wait for 30 secs')
		time.sleep(30)
		continue

	# print(users)
	for user in users:
		if count % count_of_file == 0 and count != 0:
			write = csv.writer(open('hasil_comments/{} {}.csv'.format(source_code, counter_file), 'w', newline=''))
			headers = ['User Name', 'Comments']
			write.writerow(headers)
			counter_file += 1
		username = user['node']['owner']['username']
		text = user['node']['text']

		write = csv.writer(open('hasil_comments/{} {}.csv'.format(short_code, counter_file), 'a', newline='', endcoding='utf-8'))
		data = [username, text]
		write.writerow(data)
		count += 1
		print(count, username, text)

		end_cursor = r['data']['edge_media_to_parent_comment']['page_info']['end_cursor']
	# print(end_cursor)
	has_next_page = r['data']['edge_media_to_parent_comment']['page_info']['has_next_page']
	if has_next_page == False: Break
	time.sleep(2)

