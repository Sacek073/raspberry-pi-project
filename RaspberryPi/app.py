from flask import Flask, jsonify
from your_sensor_script import get_data_from_sensors

app = Flask(__name__)

@app.route('/api/sensor-data', methods=['GET'])
def sensor_data():
    data = get_data_from_sensors()
    return jsonify(data)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
