import os
import clip
import torch
from torchvision.datasets import CIFAR100
import PIL
import urllib
import uuid

# Load the model
device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load('ViT-B/32', device)

def classify_image(remote_image, what_animal):
    presences = ["present", "not present"]
    tmp_id = str(uuid.uuid4())
    f = f"/tmp/{tmp_id}.jpg"
    urllib.request.urlretrieve( 
        remote_image, 
        f
    )
    image = PIL.Image.open(f)
    image_input = preprocess(image).unsqueeze(0).to(device)
    text_inputs = torch.cat([clip.tokenize(f"a photo of a {what_animal} is {presence}") for presence in presences]).to(device)

    # Calculate features
    with torch.no_grad():
        image_features = model.encode_image(image_input)
        text_features = model.encode_text(text_inputs)

    # Pick the top 5 most similar labels for the image
    image_features /= image_features.norm(dim=-1, keepdim=True)
    text_features /= text_features.norm(dim=-1, keepdim=True)
    similarity = (100.0 * image_features @ text_features.T).softmax(dim=-1)
    values, indices = similarity[0].topk(2)

    # Print the result
    print("\nTop predictions:\n")
    for value, index in zip(values, indices):
        print(f"{presences[index]}: {100 * value.item():.2f}%")
        if presences[index] == "present" and 100 * value.item() > 60:
            print(remote_image)