import matplotlib.pyplot as plt
import matplotlib.animation as animation

class UserInterface():
    def __init__(self):
        # Initialise states

        # Setup terminal for receiving user inputs
        self.terminal = UserInput()
        self.terminal.start()
        
    def setupPipe(self, pipe):
        self.terminal.main_pipe = pipe

# This class controls the states of the user interface
class UserInput(Thread):
    # Requirements:
    # 1. A way to communicate with the groundstation -> Setup the process of the groundStation (pipe)

    def __init__(self):
        self.queue = Queue()
        self.main_pipe = ""
        Thread.__init__(self)

    def run(self):
        host = "192.168.137.184"#input("Please enter the robot's host ip address: ")
        
        # Return host
        self.queue.put(host)

        while True:
            option = input("Please enter your command: ")

            # Return command
            self.queue.put(int(option))
            if int(option) == 3:
                break
    
    def getCommand(self):
        return self.queue.get()
class 