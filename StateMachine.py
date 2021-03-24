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

        # Available options for each state
        self.setupOptions = [1, 4]
        self.readyOptions = [2, 3, 4]
        self.descentOptions = [3, 4]
        self.abortOptions = [4]


    def notReady(self):
        # Option 1 and 3
        return self.lockIn == 0 and self.shutDown == 0

    def notDescent(self):
        # Option 2, 3 and 4
        return self.descent == 0 and self.abort == 0 and self.shutDown == 0

    def toDescent(self):
        # Option 3 and 4
        return self.abort == 0 and self.touchdown == 0 and self.shutDown == 0

    def toStopAbort(self):
        # Option 4
        return self.touchdown == 0 and self.shutDown == 0