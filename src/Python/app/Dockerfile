FROM continuumio/miniconda3
RUN conda install --yes -c conda-forge python=3.11
RUN conda install --yes -c pytorch pytorch torchvision cudatoolkit=11.0
RUN pip install ftfy regex tqdm fastapi uvicorn
RUN pip install git+https://github.com/openai/CLIP.git