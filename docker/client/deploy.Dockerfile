FROM python:3.7-alpine

WORKDIR /app

COPY docker/client/pip_requirements.txt /app/pip_requirements.txt
RUN pip install -r pip_requirements.txt

COPY . /app/celestial/
RUN python /app/celestial/setup.py install

RUN rm -rf /app/*