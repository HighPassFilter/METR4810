# Class that handles all the flags(?)
from multiprocessing import Value
class States():
    def __init__(self):
        # State flags
        self.connected = 0
        self.lockIn = 0
        self.descent = 0
        self.abort = 0
        self.touchdown = 0
        self.shutDown = 0
        self.reset = 0
        self.restart_setup = 0

        # Available options for each state
        self.setupOptions = [1, 4, 5, "r"]
        self.readyOptions = [2, 3, 4, 5]
        self.descentOptions = [3, 4, 5]
        self.abortOptions = [4, 5]
    
    def notSetup(self):
        # Option S, R, 3, 4
        return self.lockIn == 0 and self.shutDown == 0 and self.reset == 0 and self.restart_setup == 0

    def notReady(self):
        # Option 1 and 3
        return self.lockIn == 0 and self.shutDown == 0 and self.reset == 0

    def notDescent(self):
        # Option 2, 3 and 4
        return self.descent == 0 and self.abort == 0 and self.shutDown == 0 and self.reset == 0

    def toDescent(self):
        # Option 3 and 4
        return  self.touchdown == 0 and self.abort == 0 and self.shutDown == 0 and self.reset == 0 # Not sure if we want to be able to shut down here

    def toAbort(self):
        # Option 4
        return self.touchdown == 0 and self.shutDown == 0 and self.reset == 0
