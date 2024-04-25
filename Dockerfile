# syntax=docker/dockerfile:1

FROM python:3-slim-bullseye

WORKDIR /docker

COPY requirements.txt requirements.txt
COPY favourites.yml favourites.yml
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0", "--port=9876"]

# build command: docker build --tag helper-website .
# run command  : docker run -d -p 9876:9876 helper-website