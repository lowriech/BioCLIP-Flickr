import requests, json, urllib

BASE_URL = "https://www.flickr.com/services/rest/"
API_KEY = "1c6bc9eda634d3b3d2cc63174d3e8ddb"
BBOX = "-82.09,24.765,-79.181,27.092"
D1 = "2022-01-01"
D2 = "2022-01-30"
BASE_ARGS = {
    "bbox": BBOX, 
    "min_taken_date": D1,
    "max_taken_date": D2,
    "extras": "url_o",
    "text": "wildlife"
}

def get_flickr(args):
    args["method"] = "flickr.photos.search"
    args["api_key"] = API_KEY
    args["format"] = "json"
    args["nojsoncallback"] = 1
    # args["license"] = 9
    encoded_params = urllib.parse.urlencode(args)

    full_url = f"{BASE_URL}?{encoded_params}"
    r = requests.get(full_url)
    return json.loads(r.content)
