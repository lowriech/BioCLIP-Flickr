from huggingface_hub import hf_hub_download
import os
import requests

def download_species_names(target_path):
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.npy",
        local_dir= target_path,
        local_dir_use_symlinks = False,
    )
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.json",
        local_dir= target_path,
        local_dir_use_symlinks = False,
    )

def species_threat(species_name):
    #
    # token taken from example https://apiv3.iucnredlist.org/api/v3/docs#threat-name
    token = "9bb4facb6d23f48efbf424bb05c0c1ef1cf6f468393bc745d42179ac4aca5fee"
    end_point = f"/api/v3/threats/species/name/{species_name}?token='{token}'"
    base_url = "https://apiv3.iucnredlist.org"
    #
    response = requests.request("GET", base_url+end_point)
    return response.json() # dict
    

if __name__ == '__main__':
    script_abspath = os.path.abspath(__file__)
    target_path = os.path.join(script_abspath, "..", "..", "..", "data")
    download_species_names(target_path)