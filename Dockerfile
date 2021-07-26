#################################################
# Production Dockerfile (Dependencies, Build)   #
#################################################
FROM python:3.8

MAINTAINER SEUNGRI

WORKDIR /app/

COPY requirements/ /app/requirements/

RUN pip install --no-cache-dir -r requirements/requirements.txt

COPY . /app/

ARG PORT=8000
ENV PORT $PORT
EXPOSE $PORT 8001 8002

CMD {"python", "manage.py", "runserver", "--host=0.0.0.0", "-p 8000"}