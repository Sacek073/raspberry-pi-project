#!/bin/sh

mosquitto -d

python3 Web/receiver.py &

python3 Web/webpage.py
