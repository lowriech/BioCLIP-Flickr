FROM continuumio/miniconda3
RUN conda install --yes -c conda-forge python=3.11
COPY ./src/ecoviz_bioclip /app
COPY ./data /app/data
COPY ./output /app/output
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN conda install --yes -c pytorch pytorch torchvision cudatoolkit=11.0 
RUN apt update && apt install -y gcc
RUN pip3 install -r requirements.txt



ENTRYPOINT ["python3"]
CMD ["app.py"]