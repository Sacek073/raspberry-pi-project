#include <iostream>
#include <mosquittopp.h>
#include <unistd.h> // sleep
#include <string>
#include <cstring>
#include <nlohmann/json.hpp>
#include <ctime>
#include <RTIMULib.h>  // sensehat

using json = nlohmann::json;

class MyMqttClient : public mosqpp::mosquittopp {
public:
    MyMqttClient(const char* id, const char* host, int port) : mosqpp::mosquittopp(id) {
        // It connects to the Broker on init
        connect(host, port, 60);
    }

    void on_connect(int rc) {
        if (rc == 0) {
            std::cout << "Connected to MQTT broker." << std::endl;
        }
        else {
            std::cerr << "Failed to connect to MQTT broker." << std::endl;
        }
    }

    void on_publish(int mid) {
        // Callback for publishing message
    }

    void on_error(){
        // Callback for error
    }

    void on_disconnect(){
        // Callback for disconnect, probably log something and try to reconnect
    }

    void send_message(const char* topic, const char* message) {
        // Our function for sending data
        std::cout << "Sending message: " << message << std::endl;
        publish(NULL, topic, strlen(message), message);
    }
};

float readAirPressure() {
    RTIMUSettings *settings = new RTIMUSettings("RTIMULib");
    RTIMU *imu = RTIMU::createIMU(settings);
    float pressure = 0.0;

    if ((imu == nullptr) || (imu->IMUType() == RTIMU_TYPE_NULL)) {
        std::cerr << "IMU not found" << std::endl;
        return 1;
    }

    imu->IMUInit();

    while (true) {
        if (imu->IMURead()) {
            RTIMU_DATA imuData = imu->getIMUData();

            std::cout << "Pressure: " << imuData.pressure << std::endl;
        }
        usleep(imu->IMUGetPollInterval() * 1000);
    }
    
    delete imu;
    delete settings;

    return pressure;
}

json get_data_from_sensors(){
    // This funtion should collect data from the sesnors
    // These data are paced into json object, which is part of json payload

    // TODO collect data from sensors
    json data;
    data["temperature"] = 33;
    data["humidity"] = 50;
    data["air_pressure"] = readAirPressure();

    return data;
}

const char* prepare_payload(){
    // This function prepares the payload for message which will be sent

    json object;
    // TODO fix getting name - figure out how - maybe IP adress??
    std::time_t current_time = std::time(nullptr);
    std::string time_str = std::ctime(&current_time);
    object["timestamp"] = time_str;
    object["device"] = "RPI_Jan";
    object["data"] = get_data_from_sensors();

    // Convert JSON to string
    std::string jsonData = object.dump();
    // Create an MQTT message, it has to be copy
    const char* message = strdup(jsonData.c_str());

    return message;
}



int main() {
    // TODO probablyload from some config file
    const char* mqtt_host = "172.21.64.213"; // MQTT broker ip
    int mqtt_port = 1883; // MQTT broker port
    const char* topic = "weather_info";

    MyMqttClient mqtt_client("client_id", mqtt_host, mqtt_port);

    while (1) {
        const char* message = prepare_payload();
        mqtt_client.send_message(topic, message);

        // We need to free the message
        // If we want to store the messages we need to free it elswhere
        // Something like:
        // if message is sent:
        //     free(message)
        // else:
        //     queue.append(message)

        free((void*)message);
        sleep(10); // Once in ten minutes
    }

    return 0;
}
