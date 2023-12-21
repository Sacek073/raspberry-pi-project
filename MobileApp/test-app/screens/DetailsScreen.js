import React from 'react';
import { View,Text,StyleSheet} from 'react-native';
import { TouchableOpacity } from 'react-native-gesture-handler';

const DetailsScreen = ({navigation}) => {
    return (
        <View style={styles.containerView}>
            <Text>These are really amazing details!</Text>
        </View>
    );
};

const styles = StyleSheet.create({
    containerView: {
        flex:1,
        alignItems: 'center',
        justifyContent: 'center',
    }
});

export default DetailsScreen;
