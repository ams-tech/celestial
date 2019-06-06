FROM python:3.7-alpine

WORKDIR /app

COPY pip_dev_requirements.txt /app/pip_test_requirements.txt
RUN pip install -r pip_test_requirements.txt


COPY pip_requirements.txt /app/pip_requirements.txt
RUN pip install -r pip_requirements.txt