FROM alpine:3.14

RUN apk update && apk add python3 py3-pip

RUN pip install paho-mqtt flask plotly

RUN apk add py3-pandas

RUN apk add py3-dateutil

RUN apk add mosquitto mosquitto-clients

EXPOSE 1883

EXPOSE 5000

WORKDIR /app

COPY ./Web/ /app/Web

COPY ./start.sh /app/

RUN chmod +x ./start.sh

CMD ["sh", "./start.sh"]
