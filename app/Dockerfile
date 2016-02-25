FROM gliderlabs/alpine:3.2

MAINTAINER Allan Costa "allaninocencio@yahoo.com.br"

RUN apk --update add python-dev py-pip

ADD . /src/app

WORKDIR /src/app

RUN pip install -r requirements.txt

CMD python app.py
