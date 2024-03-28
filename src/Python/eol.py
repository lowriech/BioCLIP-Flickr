import requests, urllib, json

BASE_URL = "https://eol.org/api/search/1.0.json"

def get_eol(text):
    args = {}
    args["q"] = text
    args["page"] = 1
    encoded_params = urllib.parse.urlencode(args)
    print(f"{BASE_URL}?{encoded_params}")
    x = requests.get(f"{BASE_URL}?{encoded_params}")
    try:
        return json.loads(x.content)
    except json.decoder.JSONDecodeError:
        return dict()
    