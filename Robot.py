from WiFi import Server

class Robot():
    def __init__(self):
        # Setup server
        self.server = Server()

        # Setup navigation

        # Setup pilot


    def shutDown(self):
        # TODO: Shut everything down
        self.server.closeConnection

    def release(self):
        # TODO: Communicate with pilot to release the clamp
        hi = ""

    def abort(self):
        # TODO: Turn off the thrusters, camera, sensors 
        hi = ""
