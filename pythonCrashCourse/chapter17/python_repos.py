import requests

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# 将API响应赋给一个变量
response_dict = r.json()

print(response_dict.keys())
print(f"Repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
print(f"Repositories: {len(repo_dicts)}")

repo_dic = repo_dicts[0]
print(f"\nKeys: {len(repo_dic.keys())}")

for key in sorted(repo_dic.keys()):
    print(key)

print("\nSelected information about each repository:")
for repo_dict in repo_dicts:      
    print(f"\nName: {repo_dict['name']}")      
    print(f"Owner: {repo_dict['owner']['login']}")      
    print(f"Stars: {repo_dict['stargazers_count']}")      
    print(f"Repository: {repo_dict['html_url']}")      
    print(f"Description: {repo_dict['description']}")    