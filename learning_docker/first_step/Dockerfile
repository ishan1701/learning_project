

FROM python:3.9-slim

USER root
RUN apt-get update && apt-get install -y jq

RUN pip install pyspark==3.1.2
RUN pip install pylint