## Requirements
* for MQTT
    - Mosquito
```
sudo apt-get install libmosquitto-dev
sudo apt-get install libmosquittopp-dev
sudo apt-get install nlohmann-json3-dev
```
* for SenseHat
    - QT5
```
sudo apt-get install qt5-default
```
* for  RTIMULib
    - clone repo from https://github.com/RPi-Distro/RTIMULib and follow ReadMe found in /Linux/

```
cd RTIMULib/RTIMULib
mkdir build
cd build
cmake ..
make -j4
sudo make install
sudo ldconfig
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
`g++ -o mqtt_example mqtt_example.cpp -lmosquittopp`
`g++ -o out/weatherstation src/weatherstation.cpp -I/include/RTIMULib/ -lmosquittopp -lRTIMULib`