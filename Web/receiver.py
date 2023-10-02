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
            f.write("{}")


    def storeToFile(self, data: str) -> None:
        """
        For stoing the data into existing json file,
        we need to check if the data from on device are already in the file,
        if yes, we need o append the data, if not, we need to create new entry
        """
        json_data = json.loads(data)
        # TODO


class Config:
    """
    Class to store our configuration
    We can load it from file
    """
    def __init__(self,
                 broker_ip="localhost",
                 port=1883,
                 topic="weather_info",
                 download_folder=os.path.join(os.getcwd(), "..", "data"),
                 json_file="data.json") -> None:
        self.broker_ip = broker_ip
        self.port = port
        self.topic = topic
        self.download_folder = download_folder
        self.json_file = json_file


if __name__ == "__main__":
    config = Config()

    downloader = Downloader(config.download_folder, config.json_file)

    client = OurCliennt(config.topic, downloader).setup_client()
    client.connect(config.broker_ip, config.port, 60)
    client.loop_forever()
