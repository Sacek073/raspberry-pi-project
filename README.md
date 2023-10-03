# Raspberry Pi Project

## Data Sending
- If it is possible to send the `.json` payload with MQTT we will prepare the payload with the C++ code on the RPI.
- The data will be sent once in 15 minutes.
- Send also the timezone (setting is in mobile app).



## Data Store
- On the server there will be one `.json` file for each raspberry pi (weather station).
- There will be one method which will


## Android App
- Probably WiFi
- Can displey current weather.
- Will poll the data from raspberry every 5 minutes.
- Configure the station (MQTT, name).


## Extensions
- Use the LED display
- OpenWeatherMaps -> public free API for current weather, also uses `.json` with same structure as we purposed.

## Data Format
multiple formats with their own standards but no standard which format to use ([Source](https://climatedataguide.ucar.edu/climate-tools/common-climate-data-formats-overview))
- HDF and NetCDF (file formats)
- GRIB (record format)
