# pull official base image
# FROM python:3

# set environment variables
# ENV PYTHONUNBUFFERED 1
# ENV PYTHONDONTWRITEBYTECODE 1

# setting up work directory
# WORKDIR /petmate-docker

# install dependencies
# RUN pip install --upgrade pip
# COPY requirements.txt /petmate-docker/
# RUN pip install -r requirements.txt

# running server
# EXPOSE 8000
# CMD ["gunicorn", "-c", "./petmate/wsgi.py", "wsgi:get_wsgi_application"]


# COPY . /petmate-docker/
# RUN mkdir /petmate-docker
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


FROM python:3

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# RUN apk --update add \
#     build-base \
#     postgresql \
#     postgresql-dev \
#     libpq \
#     # pillow dependencies
#     jpeg-dev \
#     zlib-dev

RUN mkdir /petmate-docker
WORKDIR /petmate-docker
COPY requirements.txt /petmate-docker/
RUN pip install -r requirements.txt


COPY . /petmate-docker/

EXPOSE 8000