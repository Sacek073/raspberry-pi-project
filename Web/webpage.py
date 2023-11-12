from flask import Flask, render_template, request
import json
import plotly.graph_objs as go
from dateutil import parser

def get_rpi_names():
    with open("../data/data.json", "r") as f:
        data = json.load(f)
        rpis = []
        for rpi in data["devices"]:
            rpis.append(rpi["name"])
        return rpis

app = Flask(__name__, template_folder='./templates', static_folder='./static')
devices = get_rpi_names()

def get_values(data, type):
    """
    Returns a list of temperatures from the data
    Args:
    data -- the data for specific device from master json
    type -- string, 'temperature', 'humidity', 'air_pressure'
    """
    temperatures = {}
    for item in data:
        timestamp = item["timestamp"]
        temp = item["data"][type]
        temperatures[timestamp] = temp
    return temperatures

@app.route('/')
def index():
    """
    Show the index page
    """
    if len(devices) == 1:
        return process_form(devices[0])
    return render_template('index.html', devices=devices)


def prepare_plot(data, y_axis):
    """
    Function prepare a plot for iven data (already selcetd temeparure, humidity or pressure)"""
    data = dict(sorted(data.items(), key=lambda item: item[0]))
    dates = list(data.keys())
    date_objects = [parser.parse(date_str) for date_str in dates]
    values = [float(val) for val in data.values()]

    fig = go.Figure()
    fig.add_trace(go.Scatter(x=date_objects, y=values, mode='lines+markers', name=y_axis))
    fig.update_xaxes(title_text='Time')
    fig.update_yaxes(title_text=y_axis)
    return fig.to_html()

@app.route('/device', methods=['POST'])
def process_form(opt_arg=None):
    """
    Processes data from the form in tha navigation bar
    and displays the graph for the selected device
    """
    if opt_arg is None:
        selected_device = request.form.get('selected_device')
    else:
        selected_device = opt_arg
    current_data = []
    with open("../data/data.json", "r") as f:
        data = json.load(f)
        for rpi in data["devices"]:
            if rpi["name"] == selected_device:
                current_data = rpi["values"]

    temp_plot = prepare_plot(get_values(current_data, "temperature"), "Temperature (°C)")
    humidity_plot = prepare_plot(get_values(current_data, "humidity"), "Humidity (%)")
    pressure_plot = prepare_plot(get_values(current_data, "air_pressure"), "Air pressure (Pa)")

    return render_template('device.html',
                           device=selected_device,
                           devices=devices, # for the navigation bar from global variable
                           temperature=temp_plot,
                           humidity=humidity_plot,
                           pressure=pressure_plot
                           )





@app.route('/device', methods=['GET'])
def device():
    """
    Just to return to index.html, if user uses GET on /device
    """
    return index()

if __name__=='__main__':
    # app.run(debug = True)
    app.run()
