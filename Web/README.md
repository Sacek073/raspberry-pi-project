# Info
This folder contains the web application which is used to display the data from the MQTT broker and the receiver.

## How to use
In order to run the web application and the receiver, please go to the Docker folder and follow the instructions there.

### The following part was used in time, when we did not used Docker and runned the app by the modules itself. It is not used anymore, but it is still here for reference.
- Receiver:
`pip install paho-mqtt`
- Webpage:
```
pip install flask
pip install pandas
pip install python-dateutil
pip install plotly
```
- MQTT broker
`sudo apt install mosquitto mosquitto-clients`
- MQTT config (/etc/mosquitto/mosquitto.conf):
```
pid_file /run/mosquitto/mosquitto.pid

persistence true
persistence_location /var/lib/mosquitto/

log_dest file /var/log/mosquitto/mosquitto.log

include_dir /etc/mosquitto/conf.d

listener 1883

allow_anonymous true
```
- To run:
1. You have to start the MQTT broker so, it can deliver messages to the `reciever.py`: `sudo systemctl start mosquitto`
2. Run the reciever: `python reciever.py` which stores the data in the JSON file.
