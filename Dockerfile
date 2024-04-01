FROM continuumio/miniconda3
RUN conda install --yes -c conda-forge python=3.11
COPY ./src/ecoviz_bioclip /app
COPY ./data /app/data
COPY ./output /app/output
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN conda install --yes -c pytorch pytorch torchvision cudatoolkit=11.0 
RUN apt update && apt install -y gcc
# installing our package ecoviz_bioclip (requirements.txt installed as dependencies)
RUN pip3 install .
# RUN pip3 install -r requirements.txt
RUN python3 -m pipeline/01-download-data.py


ENTRYPOINT ["python3"]
CMD ["app.py"]