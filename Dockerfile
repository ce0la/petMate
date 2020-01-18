# pull official base image
FROM python:3

# set environment variables
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# setting up work directory
WORKDIR /petmate-docker

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /petmate-docker/
RUN pip install -r requirements.txt

# running server
EXPOSE 8000
CMD ["gunicorn", "-c", "gunicorn_config.py", "wsgi:get_wsgi_application"]


# COPY . /petmate-docker/
# RUN mkdir /petmate-docker
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]