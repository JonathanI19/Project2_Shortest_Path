#!/usr/bin/env/ python3

from pyamaze import maze, agent, COLOR
import sys

# Importing aStar method and ParseFile object
sys.path.append("../")
from Algorithms.aStar import aStar
from parser_script import ParseFile

# Names for Output csv and Input csv
OUTPUT = "./aStar_example_output.csv"
INPUT = "./example_input_2.txt"

# GOAL is location of goal cell
# Default is normally upper left corner (1,1)
GOAL_ROW = 2
GOAL_COL = None

# STARTx and STARTy are used to specify the starting location of the maze
# When set to None, they default to the respective end col or end row
START_ROW = 4
START_COL = None


# Highlighted Green is defined in createmaze

# Main function
def main():
    
    # Creating parse object.
    # Input csv is out of order, so N, S, E, W is used to specify the order that they are passed in.
    # Output csv will be normalized to EWNS, provided proper input order is declared.
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT, N=0, S=1, E=2, W=3)
    
    # creating maze object of name m
    m = maze(rows = parse.rows, cols = parse.cols)
    
    # Loading maze based on normalized output csv
    # x and y are taken from goal and used to show the appropriate cell
    goal_col,goal_row = GOAL_COL, GOAL_ROW
    if goal_row is None:
        goal_row = 1
    if goal_col is None:
        goal_col = 1
    m.CreateMaze(loadMaze = OUTPUT, x = goal_row, y = goal_col)
    
    # Using aStar to create fwdPath dictionary, which is used to find path from start to goal.
    start_x, start_y = START_COL,START_ROW
    if start_x is None:
        start_x = parse.cols
    if start_y is None:
        start_y = parse.rows
    fwdPath= aStar(m = m, start = (start_y,start_x))
    
    # Print out fwdPath dictionary
    print(fwdPath)

    # Creating agent object
    # This is what draws the path and allows us to specify the start and end location
    _goal = (goal_row, goal_col)
    print(_goal)
    a = agent(m, x=START_ROW, y=START_COL, goal=_goal, footprints=True, color=COLOR.blue, filled=True)
    #a = agent(m,)
    # Tells the maze to trace the path when the gui is displayed
    m.tracePath({a:fwdPath}, delay=300)

    # Displays the gui if the user passes in [display] (case insensitive) after calling the program
    if len(sys.argv) > 1:
        if sys.argv[1].casefold() == "display":    
            m.run()

if __name__ == '__main__':
    main()
