import requests

url = "https://ndownloader.figshare.com/files/2292169"
r = requests.get(url, allow_redirects=True)
open('data/portal_data_joined.csv', 'wb').write(r.content)
