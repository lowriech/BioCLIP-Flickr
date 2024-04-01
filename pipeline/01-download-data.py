import os

from ecoviz_bioclip import download_species_names

if __name__ == "__main__":
    script_abspath = os.path.abspath(__file__)
    target_path = os.path.join(
        script_abspath, 
        "..",
        "data",
    )
    download_species_names(target_path)