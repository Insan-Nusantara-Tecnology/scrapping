import requests, json, time
from bs4 import BeautifulSoup


url = 'https://www.instagram.com/api/graphql'

source_code = input('Please enter a source_code')

end_cursor = ''

count = 0
while 1:
	var = {
		'shortcode': source_code,
		'first': 50,
		'after': end_cursor,
	}

	param = {
		'variables': json.dumps(var)
	}

	r = requests.get(url, params=param).json()

	try:
		users = r['data']['data.xdt_api__v1__likes__media_id__likers']['users']
	except:
		print('wait for 30 secs')
		time.sleep(30)
		continue
	
	for user in users:
		username = user['username']
		fullname = user['full_name']
		profile_pic = user['profile_pic_url']
		count +=1
		print(count, username, fullname, profile_pic)
		# print(username)
		# print(fullname)
		# print(profile_pic)
		# print(count)	

	end_cursor = r['data']['data.xdt_api__v1__likes__media_id__likers']['page_info']['end_cursor']
	# print(end_cursor)
	has_next_page = r['data']['data.xdt_api__v1__likes__media_id__likers']['page_info']['has_next_page']
	if has_next_page == False: Break
	time.sleep(2)
	