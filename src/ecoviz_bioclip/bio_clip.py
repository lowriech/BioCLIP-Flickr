import open_clip
import uuid, urllib
import PIL
import torch
import numpy as np
import json
from torchvision import transforms
import torch.nn.functional as F
import collections
import heapq
min_prob = 1e-9

model, preprocess_train, preprocess_val = open_clip.create_model_and_transforms('hf-hub:imageomics/bioclip')
tokenizer = open_clip.get_tokenizer('hf-hub:imageomics/bioclip')
txt_emb_npy = "./data/txt_emb_species.npy"
txt_names_json = "./data/txt_emb_species.json"
txt_emb = torch.from_numpy(np.load(txt_emb_npy, mmap_mode="r"))
with open(txt_names_json) as fd:
    txt_names = json.load(fd)

preprocess_img = transforms.Compose(
    [
        transforms.ToTensor(),
        transforms.Resize((224, 224), antialias=True),
        transforms.Normalize(
            mean=(0.48145466, 0.4578275, 0.40821073),
            std=(0.26862954, 0.26130258, 0.27577711),
        ),
    ]
)

ranks = ("Kingdom", "Phylum", "Class", "Order", "Family", "Genus", "Species")

k = 5
rank = 6

def format_name(taxon, common):
    taxon = " ".join(taxon)
    if not common:
        return taxon
    return f"{taxon} ({common})"

def classify_image(remote_image, what_animal):
    presences = ["present", "not present"]
    tmp_id = str(uuid.uuid4())
    f = f"/tmp/{tmp_id}.jpg"
    urllib.request.urlretrieve( 
        remote_image, 
        f
    )
    img = PIL.Image.open(f)
    img = preprocess_val(img)
    img_features = model.encode_image(img.unsqueeze(0))
    img_features = F.normalize(img_features, dim=-1)
    logits = (model.logit_scale.exp() * img_features @ txt_emb).squeeze()
    probs = F.softmax(logits, dim=0)

    # If predicting species, no need to sum probabilities.
    if rank + 1 == len(ranks):
        topk = probs.topk(k)
        print(topk)
        return {
            format_name(*txt_names[i]): prob for i, prob in zip(topk.indices, topk.values)
        }
            

