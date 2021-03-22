import GUI
from GroundStation import GroundStation
from StateMachine import States

class Computer():
    def __init__(self):
        # Setup states
        self.states = States()
        # Setup user interface
        self.user = GUI.UserInterface()

        # Setup ground station
        self.gs = GroundStation()

        # Setup communication between user and ground station
        self.user.setupPipe(self.gs.main_pipe)

        # Note that the user interface handles the initial setup of providing the ground station with the host information
        # User interface also handles the constant request for user input to issue the commands to the 




