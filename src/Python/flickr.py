import requests, json, urllib

BASE_URL = "https://www.flickr.com/services/rest/"
API_KEY = "1c6bc9eda634d3b3d2cc63174d3e8ddb"
BBOX = "-92.601560,40.518931,-80.121092,48.873402" #"-82.09,24.765,-79.181,27.092"
D1 = "2008-01-01"
D2 = "2022-01-30"
PER_PAGE = 250  # Set to 500 as per requirement
MAX_IMAGES = 4000  # Maximum number of images to retrieve

BASE_ARGS = {
    "bbox": BBOX,
    "min_taken_date": D1,
    "max_taken_date": D2,
    "extras": "url_o",
    "text": "wildlife",
    "per_page": PER_PAGE,
}

def get_flickr(args):
    args["method"] = "flickr.photos.search"
    args["api_key"] = API_KEY
    args["format"] = "json"
    args["nojsoncallback"] = 1
    encoded_params = urllib.parse.urlencode(args)

    full_url = f"{BASE_URL}?{encoded_params}"
    r = requests.get(full_url)
    return json.loads(r.content)

# Function to iterate over pages until we hit the limit or run out of returns
def get_images(base_args, max_images):
    total_images = 0
    page = 1
    all_photos = []

    while total_images < max_images:
        base_args["page"] = page
        response = get_flickr(base_args)

        if 'photos' in response and 'photo' in response['photos']:
            photos = response['photos']['photo']
            if not photos:
                break  # Exit if no photos are returned

            all_photos.extend(photos)
            total_images += len(photos)
            #print(f"Retrieved {total_images} images")
            
            if total_images >= max_images:
                break  # Exit if we've reached the maximum number of images

            page += 1
        else:
            break  # Exit if there's an error in the response

    return all_photos[:max_images]  # Return the list of photos, capped at MAX_IMAGES
