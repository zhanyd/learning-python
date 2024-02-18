import requests
from plotly.graph_objects import Bar
from plotly import offline

url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")
# 将API响应赋给一个变量
response_dict = r.json()

print(response_dict.keys())
print(f"Repositories: {response_dict['total_count']}")

repo_dicts = response_dict['items']
repo_names, stars = [], []

for repo_dict in repo_dicts:
    repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

# 可视化
data = [{
    'x': repo_names,
    'y': stars,
    'type': 'bar'
}]

my_layout = {
    'title': 'Most-Starred Python Projects on GitHub',
    'xaxis': {'title': 'Repository'},
    'yaxis': {'title': 'Stars'}
}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='python_repos.html')