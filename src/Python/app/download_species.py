from huggingface_hub import hf_hub_download
import os

def download_hf_input_files():
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.npy",
        local_dir= os.path.join(script_abspath, "..", "..", "..", "data"),
        local_dir_use_symlinks = False,
    )
    hf_hub_download(
        repo_id = "imageomics/bioclip-demo",
        repo_type="space",
        filename = "txt_emb_species.json",
        local_dir= os.path.join(script_abspath, "..", "..", "..", "data"),
        local_dir_use_symlinks = False,
    )

if __name__ == '__main__':
    script_abspath = os.path.abspath(__file__)
    download_hf_input_files()