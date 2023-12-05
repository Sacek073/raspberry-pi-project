## Requirements
* for MQTT
    - Mosquito
```
sudo apt-get install libmosquitto-dev
sudo apt-get install libmosquittopp-dev
sudo apt-get install nlohmann-json3-dev
```

## Used libraries
* RTIMULib2
    * used to communicate with the SenseHat over I2C

## Compilation
`g++ -o out/weatherstation src/weatherstation.cpp -I/include/RTIMULib/ -lmosquittopp -lRTIMULib`

## Run
`./out/weatherstation`

## For the testing purposes:

* for SenseHat
    activate the I2C interface in settings

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