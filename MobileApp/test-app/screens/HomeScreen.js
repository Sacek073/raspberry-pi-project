import React, { useState, useEffect } from 'react';
import { View, Button, Text, StyleSheet } from 'react-native';
import { useRoute } from '@react-navigation/native';

const HomeScreen = ({ navigation }) => {
    const [sensorData, setSensorData] = useState({});
    const route = useRoute();
    const mqttIpAddress = route.params?.mqttIpAddress || 'localhost';
    const deviceName = route.params?.deviceName || 'Unknown Device';
    const timeZone = route.params?.timeZone || 'Unknown Time Zone';

    useEffect(() => {
        fetch(`http://${mqttIpAddress}:5000/api/sensor-data`)
            .then(response => response.json())
            .then(data => {
                setSensorData(data);
            })
            .catch(error => console.error('Error fetching sensor data:', error));
    }, [mqttIpAddress]);

    const showWeather = () => {
        navigation.push('Weather', { sensorData });
    }

    const showSettings = () => {
        navigation.push('Settings');
    }

    return (
        <View style={styles.containerView}>
            <View style={styles.infoContainer}>
                <Text style={styles.infoText}>Device Name: {deviceName}</Text>
                <Text style={styles.infoText}>MQTT IP Address: {mqttIpAddress}</Text>
                <Text style={styles.infoText}>Time Zone: {timeZone}</Text>
            </View>
            <Button onPress={showWeather} title="Weather" />
            <Button onPress={showSettings} title="Settings" />
        </View>
    );
};

const styles = StyleSheet.create({
    containerView: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    infoContainer: {
        marginBottom: 20,
    },
    infoText: {
        fontSize: 16,
        marginBottom: 5,
    },
});

export default HomeScreen;
