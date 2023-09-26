#include <iostream>
#include <cstring>
#include <mosquittopp.h>
#include <unistd.h>
#include <string>
#include <cstring>

class MyMqttClient : public mosqpp::mosquittopp {
public:
    MyMqttClient(const char* id, const char* host, int port) : mosqpp::mosquittopp(id) {
        connect(host, port, 60);
    }

    void on_connect(int rc) {
        if (rc == 0) {
            std::cout << "Connected to MQTT broker." << std::endl;
        } else {
            std::cerr << "Failed to connect to MQTT broker." << std::endl;
        }
    }

    void on_publish(int mid) {
        //std::cout << "Message published with ID: " << mid << std::endl;
    }

    void send_message(const char* topic, const char* message) {

        std::cout << "Sending message: " << message << std::endl;
        publish(NULL, topic, strlen(message), message);
    }
};

int main() {
    const char* mqtt_host = "172.21.64.213";
    int mqtt_port = 1883; // MQTT broker port

    MyMqttClient mqtt_client("client_id", mqtt_host, mqtt_port);

    int i = 0;
    while (1) {
        try
        {
            mqtt_client.loop();
        }
        catch (...)
        {
            std::cout << "Error" << std::endl;
        }

        const char* topic = "your/topic";
        std::string msg = std::to_string(i);

        char* message = new char [msg.length()+1];
        std:strcpy(message, msg.c_str());
        mqtt_client.send_message(topic, message);
        sleep(10);
        i++;
    }

    return 0;
}
