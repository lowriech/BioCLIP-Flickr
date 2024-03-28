FROM continuumio/miniconda3
RUN conda install --yes -c conda-forge python=3.11
COPY ./src/Python /app
COPY ./data /app/data
COPY ./outputs /app/outputs
COPY ./requirements.txt /app/requirements.txt
WORKDIR /app
# RUN conda install --yes -c pytorch pytorch torchvision cudatoolkit=11.0 
RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]
CMD ["app.py"]