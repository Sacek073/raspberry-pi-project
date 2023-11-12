## Requirements
* for MQTT
    - Mosquito
```
sudo apt-get install libmosquitto-dev
sudo apt-get install libmosquittopp-dev
sudo apt-get install nlohmann-json3-dev
```

* for SenseHat Sample Program
```
sudo apt-get install sense-hat
```

### if SenseHat does not get recognized
```
sudo nano /boot/config.txt
```
add the following line towards the end of the file
```
dtoverlay=rpi-sense
```
save and reboot RPi

## Compilation
`g++ -o sender sender.cpp -lmosquittopp`

