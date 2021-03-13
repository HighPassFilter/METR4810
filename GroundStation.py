from WiFi import Client

class GroundStation():
    def __init__(self, host):
        # Setup client connection to robot
        self.client = Client(host)

        # Setup User interface

    def shutDown(self):
        self.client.closeConnection()

    def command(self, option):
        if option == 1:
            # Abort
            print("Abort!")
            self.client.sendData("abort")

        elif option == 2:
            # Release
            print("Release!")
            self.client.sendData("release")

        elif option == 3:
            # Shutdown
            print("Shutting system down")
            self.client.sendData("shutdown")
            self.shutDown()

