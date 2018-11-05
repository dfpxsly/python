import requests
# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print('status code: ', req.status_code)

rsp_dict = req.json()

print(rsp_dict.keys())

for idx, column_head in enumerate(rsp_dict['items']):
	print(idx, column_head)