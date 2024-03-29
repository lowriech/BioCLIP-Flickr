
# BioCLIP Flickr Analysis

<!-- badges: start -->
<!-- badges: end -->

This repo serves as a proof of concept of analyzing species distribution from a social media source.  It leverages Flickr as a source of input images, and [BioCLIP](https://github.com/Imageomics/BioCLIP) as a species identification model.  

### Folder structure

This folder structure is based off a template.  Not all of the folders are currently in use.  The analysis entrypoing is `src/Python/app.py`, which calls the Flickr API and sends the results through BioCLIP.  The input is a set of arguments to the Flickr API, currently representing a bounding box and a keyword search.  

```
├── data
├── figs
├── notebooks
├── output
├── paper
├── pipeline
└── src
    └── Python
```

* `data/` - raw data only
* `figs/` - static figures generated during pipeline
* `notebooks/` - literate programming files (e.g., Jupyter, Quarto) explaining the pipeline
* `output/` - derived data generated during pipeline
* `pipeline/` - pipeline scripts
* `src/` - source files supporting the pipeline (e.g., functions, classes, constants)

### Computational environment

This script is intended to be run in Docker using the commands below.  This should work outside of Docker as well, provided that the data path is updated.

```
├── Dockerfile
└── requirements.txt
```

These are conventional files used for recording package dependencies. 

`requirements.txt` is a file used to record Python package dependencies. Users can install dependencies by running `pip install -r requirements.txt` at the command line.

`Dockerfile` defines a full computational environment.  You can build and run the container using:

To build:
```
IMAGE=bioclip-flickr
docker build -t $IMAGE .
```

To run as-is:
```
docker run -it $IMAGE
```

To run while changing the data or the src code directory:
```
docker run -it \
    -v $PWD/src/Python:/app \
    -v $PWD/data:/app/data \
    -v $PWD/output:/app/output \
    -v $PWD/notebooks:/app/notebooks \
    $IMAGE
```
