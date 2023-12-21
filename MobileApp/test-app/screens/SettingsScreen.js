import React, { useState } from 'react';
import { View, Text, TextInput, Button, StyleSheet } from 'react-native';

const SettingsScreen = ({ navigation }) => {
    const [deviceName, setDeviceName] = useState('');
    const [mqttIpAddress, setMqttIpAddress] = useState('');
    const [timeZone, setTimeZone] = useState('');

    const saveSettings = () => {
        // You can save the entered values to some storage (e.g., AsyncStorage)
        // For simplicity, let's just navigate back to the home screen with the entered values
        navigation.navigate('Home', { deviceName, mqttIpAddress, timeZone });
    }

    return (
        <View style={styles.containerView}>
            <Text style={styles.settingsText}>Device Name</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter Device Name"
                onChangeText={text => setDeviceName(text)}
                value={deviceName}
            />

            <Text style={styles.settingsText}>MQTT IP-Address</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter MQTT IP Address"
                onChangeText={text => setMqttIpAddress(text)}
                value={mqttIpAddress}
            />

            <Text style={styles.settingsText}>Time Zone</Text>
            <TextInput
                style={styles.input}
                placeholder="Enter Time Zone"
                onChangeText={text => setTimeZone(text)}
                value={timeZone}
            />

            <Button onPress={saveSettings} title="Save" />
        </View>
    );
};

const styles = StyleSheet.create({
    containerView: {
        flex: 1,
        alignItems: 'center',
        justifyContent: 'center',
    },
    settingsText: {
        marginBottom: 10,
        fontSize: 18,
        fontWeight: 'bold',
    },
    input: {
        height: 40,
        borderColor: 'gray',
        borderWidth: 1,
        marginBottom: 20,
        paddingLeft: 10,
        width: '80%',
    }
});

export default SettingsScreen;
