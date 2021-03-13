from WiFi import Server

class Robot():
    def __init__(self):
        # Setup server
        self.server = Server()

        # Setup navigation

        # Setup pilot
    def receiveData(self):
        message = self.server.receiveData()
        if message == "abort":
            self.abort()
        if message == "release":
            self.release()
        if message == "shutdown":
            print("HI")
            self.shutDown()

        return message

    def shutDown(self):
        # TODO: Shut everything down
        server.listener.join()
        print("Robot shutting down")
        self.server.closeConnection()

    def release(self):
        # TODO: Communicate with pilot to release the clamp
        print("Release!")

    def abort(self):
        # TODO: Turn off the thrusters, camera, sensors 
        print("Abort!")
