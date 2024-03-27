from flickr import BASE_ARGS, get_flickr
from bio_clip import classify_image
import json

imgs = get_flickr(BASE_ARGS)
with open('./verifications.txt', 'w') as f:
    for i in [i for i in imgs['photos']['photo'] if 'url_o' in i.keys()][0:5]:
        x = classify_image(i['url_o'], 'flamingo')
        vals = {k: float(v) for k, v in x.items()}
        f.write(json.dumps(vals))
        f.write(
            '\n'
        )
        f.write(i['url_o'])
        f.write(
            '\n'
        )