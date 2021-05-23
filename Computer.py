import GUI
from GroundStation import GroundStation
from multiprocessing import Pipe

comp = ""
# The overarching class that manages the shared resources between the two processes
class Computer():
    def __init__(self):
        # Setup the pipe for communication between the processes
        self.main_pipe, self.tele_pipe = Pipe()

        # Setup user interface
        self.user = GUI.UserInterface(self.main_pipe)
        
        # Setup ground station
        self.gs = GroundStation(self.tele_pipe)

        # Note that the user interface handles the initial setup of providing the ground station with the host information
    
if __name__ == '__main__':
    comp = Computer()