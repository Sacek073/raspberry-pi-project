import paho.mqtt.client as mqtt
import os
import json


class OurCliennt():
    """
    Cerated just so we can keep our modificaions of mqtt client in one place
    use ths class in following maner:

    client = OurCliennt(config.topic).setup_client()
    """
    def __init__(self, topic: str, downloader) -> None:
        self.topic = topic
        # We add instance of the downloader class into OurClient,
        # so we can download the messages we receive
        self.downloader = downloader


    def on_connect(self, client: mqtt.Client, userdata, flags, rc: int) -> None:
        """
        Just to log info, whenwe connect to the broker
        We do not use param usrdata and flags
        """
        print("Connected with code: " + str(rc))

        self.downloader.checkFolerExistsOrCreate()
        if not self.downloader.checkFileExists():
            print("File for storing data does not exist, creating it")
            self.downloader.createFile()

        client.subscribe(self.topic)


    def on_message(self, client, userdata, msg) -> None:
        """
        Just to log info when we receive a message
        We do not use param client and userdata
        """
        print(f"Received message: {str(msg.payload)}")
        # The datacomes as bytes, so we need to decode it
        self.downloader.storeToFile(str(msg.payload.decode("utf-8")))


    def setup_client(self) -> mqtt.Client:
        """
        Sets up our client and returns it
        """
        client = mqtt.Client()
        client.on_connect = self.on_connect
        client.on_message = self.on_message
        return client


class Downloader:
    """
    Class for making the oprations with the incoming data - storing and updating
    """
    def __init__(self, folder: str, json_file: str) -> None:
        self.folder = folder
        self.json_file = json_file


    def checkFolerExistsOrCreate(self) -> None:
        """
        Just to check whether the folder exists, if not, create it
        """
        if os.path.exists(self.folder):
            return
        else:
            os.mkdir(self.folder)


    def checkFileExists(self) -> bool:
        """
        Just to check whether the file exists
        """
        return os.path.isfile(os.path.join(self.folder, self.json_file))


    def createFile(self) -> None:
        """
        Creates the master json
        """
        with open(os.path.join(self.folder, self.json_file), "w") as f:
            devices = []
            data = {"devices": devices}
            json.dump(data, f)


    def createJsonEntry(self, data: json) -> json:
        """
        Creates the json entry for the data
        """
        del data["device"]
        print(data)
        return data



    def storeToFile(self, data: str) -> None:
        """
        For stoing the data into existing json file,
        we need to check if the data from on device are already in the file,
        if yes, we need o append the data, if not, we need to create new entry
        """
        json_data = json.loads(data)
        name = json_data["device"]
        with open(os.path.join(self.folder, self.json_file), "r") as infile:
            try:
                master_json = json.load(infile)
            # TODO maybe this is not the best way
            except json.decoder.JSONDecodeError:
                master_json = {}

            entry = self.createJsonEntry(json_data)

            found = False
            for device in master_json["devices"]:
                if device["name"] == name:
                    device["values"].append(entry)
                    found = True
                    break

            if (master_json["devices"] == []) or (found == False):
                new = {
                    "name": name,
                    "values":[entry]
                }
                master_json["devices"].append(new)

            # write chages to the file
            with open(os.path.join(self.folder, self.json_file), "w") as f:
                    json.dump(master_json, f)



class Config:
    """
    Class to store our configuration
    We can load it from file
    """
    def __init__(self,
                 broker_ip="172.21.64.213",
                 port=1883,
                 topic="weather_info",
                 download_folder=os.path.join(os.getcwd(), "..", "data"),
                 json_file="data.json") -> None:
        self.broker_ip = broker_ip
        self.port = port
        self.topic = topic
        self.download_folder = download_folder
        self.json_file = json_file


def receive():
    print("Reciever running")
    with open("/app/ip.txt", "r") as f:
        ip = f.read().strip()
    config = Config(broker_ip=ip)

    downloader = Downloader(config.download_folder, config.json_file)

    client = OurCliennt(config.topic, downloader).setup_client()
    client.connect(config.broker_ip, config.port, 60)
    client.loop_forever()
