import GUI
from GroundStation import GroundStation
from StateMachine import States
from multiprocessing import Pipe


comp = ""
# The overarching class that handles shared resources between the two processes
class Computer():
    def __init__(self):
        # Setup the pipe for communication between the processes
        self.main_pipe, self.tele_pipe = Pipe()

        # Setup user interface
        self.user = GUI.UserInterface(self.main_pipe)
        
        # Setup ground station
        self.gs = GroundStation(self.tele_pipe)

        # Setup the graph interface
        self.user.startGraph(self.gs)
        # Note that the user interface handles the initial setup of providing the ground station with the host information
        # User interface also handles the constant request for user input to issue the commands to the 
    
if __name__ == '__main__':
    comp = Computer()