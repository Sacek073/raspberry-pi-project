FROM alpine:3.14

RUN apk update && apk add python3 py3-pip

RUN pip install paho-mqtt flask plotly

RUN apk add py3-pandas

RUN apk add py3-dateutil

EXPOSE 5000

WORKDIR /app

COPY ./Web/ /app/Web

COPY ./ip.txt /app/

COPY ./data/ /app/data

CMD ["python3", "/app/Web/webpage.py"]
