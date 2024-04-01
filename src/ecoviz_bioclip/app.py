from ecoviz_bioclip.flickr import BASE_ARGS, get_flickr
from ecoviz_bioclip.bio_clip import classify_image
from ecoviz_bioclip.eol import get_eol
import json
import csv
import re


THRESHOLD = 0.7


def extract_text_in_parentheses(text):
    pattern = r"\((.*?)\)"  # Regular expression pattern to match text within parentheses
    matches = re.findall(pattern, text)
    return matches

def main():
    imgs = get_flickr(BASE_ARGS)
    with open('./output/verifications.csv', 'w') as f:
        writer = csv.writer(f)
        for i in [i for i in imgs['photos']['photo'] if 'url_o' in i.keys()][0:5]:
            flickr_img = i['url_o']
            x = classify_image(flickr_img)
            vals = {k: float(v) for k, v in x.items() if float(v) != THRESHOLD}
            if len(vals.keys()) > 0:
                species, likelihood = next(iter(vals.items()))
                common_name = extract_text_in_parentheses(species)
                eol_response = get_eol(common_name)
                if 'results' in eol_response.keys() and len(eol_response['results']) > 0:
                    eol_link = eol_response['results'][0]['link']
                else:
                    eol_link = "NONE"
                writer.writerow([flickr_img, species, common_name, likelihood, eol_link])


if __name__ == "__main__":
    main()
    

