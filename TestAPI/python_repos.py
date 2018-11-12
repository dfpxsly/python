import requests
# Make an API call, and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
req = requests.get(url)
print('status code: ', req.status_code)

rsp_dict = req.json()

#print(rsp_dict.keys())

print("total repos:", rsp_dict['total_count'])

repo_dicts = rsp_dict['items']
print("respos returned:", len(repo_dicts))

'''
repo_dict = repo_dicts[0]
print("\nkeys:", len(repo_dict))
for key in sorted(repo_dict.keys()):
	print(key)
'''

for repo_dict in repo_dicts:
	print('Name:', repo_dict['name'])
	print('Owner:', repo_dict['owner']['login'])
	print('Stars:', repo_dict['stargazers_count'])
	print('Repository:', repo_dict['html_url'])
	print('Description:', repo_dict['description'])
