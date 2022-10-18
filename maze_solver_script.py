#!/usr/bin/env/ python3

# Handling imports
from pyamaze import maze, agent, COLOR
import sys
sys.path.append("./")
from Algorithms.aStar import aStar


class MazeSolver:
    def __init__(self, goal_row = 1, goal_col = 1, start_row = None, start_col = None, input_csv = None):
        
        # Setting initial variables
        self.goal_row = goal_row
        self.goal_col = goal_col
        self.start_row = start_row
        self.start_col = start_col
        self.input_csv = input_csv
        self.path = {}

        # Creating maze object for access later
        self.m = maze()

    # This method will solve the maze and output a dictionary with the proper path
    def generatePath(self):

        # Generates a maze from input_csv (if specified)
        # Sets goal cell
        self.m.CreateMaze(loadMaze = self.input_csv, x = self.goal_row, y = self.goal_col)

        # Creates default start location if none is specified
        if self.start_row is None:
            self.start_row = self.m.rows
        if self.start_col is None:
            self.start_col = self.m.cols

        # Uses aStar method stored in this repository under ./Algorithms to solve the maze
        # Accepts maze object and starting cell as parameters
        self.path = aStar(m = self.m, start = (self.start_row, self.start_col))

        # Returning solution
        return(self.path)

    # This method will display an animated GUI of the maze being solved
    def displayGUI(self):

        # Generates an agent that shows self.path being applied to the maze
        a = agent(self.m, x=self.start_row, y=self.start_col, goal=(self.goal_row, self.goal_col), footprints=True, color=COLOR.blue, shape='square', filled=True)
        
        # Specifies parameters for how the agent (a) will animate
        self.m.tracePath({a:self.path}, delay=300)

        # Displays GUI
        self.m.run()
    

