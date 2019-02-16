import requests

query = 'zimbabwe'
url = f'https://api.github.com/search/users?q={query}'

res = requests.get(url)
print(res.text)


