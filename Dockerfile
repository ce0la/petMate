FROM python:3
ENV PYTHONUNBUFFERED 1
# RUN mkdir /petmate-docker
WORKDIR /petmate-docker
COPY requirements.txt /petmate-docker/
RUN pip install -r requirements.txt
# COPY . /petmate-docker/
CMD "python manage.py runserver 0.0.0.0:8000"
EXPOSE 8000