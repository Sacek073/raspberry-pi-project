import React from 'react';
import { View, Text, StyleSheet } from 'react-native';

const WeatherScreen = ({ route }) => {
    const { sensorData } = route.params;

    return (
        <View style={styles.containerView}>
            <Text>Temperature: {sensorData.temperature}</Text>
            <Text>Humidity: {sensorData.humidity}</Text>
            <Text>Air Pressure: {sensorData.air_pressure}</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    containerView: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    }
});

export default WeatherScreen;
