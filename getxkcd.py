import requests

r = requests.get('https://www.xkcd.com/971')

print(r.content)
