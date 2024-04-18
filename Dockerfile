# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /docker

COPY requirements.txt requirements.txt
COPY favourites.yml favourites.yml
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=9876"]