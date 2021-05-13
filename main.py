from Robot import Robot
import argparse

# Create parser for putting robot in experiment mode
gs_parser = argparse.ArgumentParser(description='Specify the mode of the computer -> Experiment(1), Demo(0)')
gs_parser.add_argument('-e',
                       '--experiment',
                       action='store_true',
                       help='Experiment mode')


args = gs_parser.parse_args()
robot = Robot(args.experiment)
robot.stateReady()
