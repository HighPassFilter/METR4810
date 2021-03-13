from WiFi import Client

class GroundStation():
    def __init__(self, host):
        self.client = Client(host)

    def shutDown(self):
        self.client.closeConnection()
