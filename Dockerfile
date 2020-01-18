FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /petmate-docker
EXPOSE 8000
WORKDIR /petmate-docker
COPY requirements.txt /petmate-docker/
RUN pip install -r requirements.txt
# COPY . /petmate-docker/