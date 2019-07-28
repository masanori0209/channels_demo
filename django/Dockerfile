FROM python:3.6
ENV PYTHONUNBUFFERED 1

WORKDIR /server
ADD requirements.txt /server/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ADD . /server/