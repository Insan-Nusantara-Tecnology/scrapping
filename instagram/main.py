import requests, json
from bs4 import BeautifulSoup


url = 'https://www.instagram.com/api/graphql'

var = {
	'av': 17841400309327371,
	'__d': 'www',
	'__user': 0,
	'__a': 1,
	'__req': 'l',
	'__hs': '19767.HYP:instagram_web_pkg.2.1..0.1',
	'dpr': 1,
	'__ccg': 'UNKNOWN',
	'__rev': 1011413229,
	'__s': 'tb8ffv:4k5omp:0x9hqz',
	'__hsi': 7335449725682381741,
	'__dyn': '7xeUjG1mxu1syUbFp40NonwgU7SbzEdF8aUco2qwJxS0k24o0B-q1ew65xO0FE2awlU-cw5Mx62G3i1ywOwv89k2C1Fwc60D8vw8OfK0EUjwGzEaE7622362W2K0zK5o4q3y1Sx-0iS2Sq2-azqwt8dUaob82cwMwrUdUbGwmk0KU6O1FwlE6PhA6bxy4VUKUnAwHw',
	'__csr': 'gpFgRf5ihx5RkIQID9b4lbdQ_uCHtv8WhlJOyt2K8LXBW9CyvGcykUGaBjyqFBmFe6qV26OaXyWJelpqyFJy99poh8ciAABVpFA8VFrRgWbGcydo8Qi8zGwxxW00kuali028824xt09Uw0imw1HK1_EK7mitpN9E9o2_xu04bU1Mza480guw5Iw2pA00xZo',
	'__comet_req': 7,
	'fb_dtsg': 'NAcMIiH9PgySEMEifSNgJKw-4C5ex96erGlP-wBNhorbwRWyY4v_GGA:17843683195144578:1707751053',
	'jazoest': 26227,
	'lsd': 'OjbNA0tTvIzYZaOSEH8Nyu',
	'__spin_r': 1011413229,
	'__spin_b': 'trunk',
	'__spin_t': 1707917481,
	'fb_api_caller_class': 'RelayModern',
	'fb_api_req_friendly_name': 'PolarisPostLikedByListDialogQuery',
	'variables': {"id":"3300319677561372534"},
	'server_timestamps': 'true',
	'doc_id': 24452425501069647,
}
param = {
	'variables': json.dumps(var)
}

r = requests.get(url, params=param).json()

users = r['data']['data.xdt_api__v1__likes__media_id__likers']['users']

count = 0
for user in users:
	username = user['username']
	fullname = user['full_name']
	profile_pic = user['profile_pic_url']
	count +=1
	# print(username)
	# print(fullname)
	# print(profile_pic)
	# print(count)	
