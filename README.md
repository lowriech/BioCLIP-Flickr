
# Automating species detections in Flickr images with BioCLIP

<!-- badges: start -->
<!-- badges: end -->

This Python-based tool is designed to leverage the power of citizen science by automating the collection and identification of biodiversity images from Flickr, a popular online photo management and sharing application. By tapping into the vast repository of public domain images uploaded by everyday citizens, our script not only facilitates the aggregation of valuable ecological data but also employs cutting-edge AI to identify species captured in these images. This project aims to support biodiversity research, conservation efforts, and the broader scientific community by providing an efficient, automated tool for data collection and analysis.

## Getting Started
To get started with the Citizen Science Image Scraper & Classifier, you'll need to:

* Clone the repository: Get a copy of the project code on your local machine.
* Install dependencies: Install the required Python libraries and dependencies as listed in the requirements.txt file.
* Configure API keys: Obtain and configure the necessary API keys from Flickr to enable image scraping.
* Set your parameters: Customize your Flickr search parameters.
* Run the script: Execute the script to start scraping and predicting which species are likely in the  images from Flickr.

## How to use the model

The current demo allows users to search for images from Flickr using serval arguments including 'bbox', 'min_taken_date', 'max_taken_date', and 'text'. The tool will return the 100 images matching these arguments from a Flickr API and then run each image through the BioCLIP model. The BioCLIP model will then return the five most probable species in the images along with their probabilities.  

```
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
```

## Contributing
We welcome contributions from the community! Whether you're interested in improving the code, expanding the classifier's capabilities, or suggesting new features, please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is released under the MIT License, making it free and open source for personal and commercial use.
