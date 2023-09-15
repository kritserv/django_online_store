FROM python:3.9

ENV PYTHONUNBUFFERED 1


RUN apt-get update
RUN apt-get install python3-dev build-essential libmariadb-dev default-libmysqlclient-dev -y

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /code/