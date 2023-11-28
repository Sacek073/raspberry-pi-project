# Docker image for running webpage and receiver

## How to use
- In order to run the webpage and the receiver you have to first run the mosquitto broker on your machine, so it can deliver messages to the receiver (running in the docker). For more information see the [Setting up the MQTT broker](#setting-up-the-mqtt-broker) section.
1. On your local machine (where the docker will run) run the mosquitto broker: `sudo systemctl start mosquitto`.

- In order to not duplicate files in the github follow these instructions:
1. Copy the Web directory to this directory: `cp -r ../Web .`
2. Change the contents of the ip.txt file with the ip address of the machine where the mosquitto broker will run.
3. Build the image: `sudo docker build -t <Image> .`
4. Run the image: `sudo docker run --name <Container> --network=host <Image>`

## Setting up the MQTT broker
- Installation:
`sudo apt install mosquitto mosquitto-clients`
- MQTT config (/etc/mosquitto/mosquitto.conf) - change the contnent of the file to:
```
pid_file /run/mosquitto/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

listener 1883

allow_anonymous true
```