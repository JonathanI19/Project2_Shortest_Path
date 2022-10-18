#!/usr/bin/env/ python3

import sys
sys.path.append("../")
from maze_solver_script import MazeSolver
from parser_script import ParseFile

# Names for Output csv and Input csv
OUTPUT = "./_example_output_1.csv"
INPUT = "./example_input_1.txt"

# Main Function
def main():

    # Creating ParseFile object.
    # Output csv will be normalized to EWNS, provided proper input order is declared.
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT)

    # Creating MazeSolver object.
    # goal_row and goal_col point to the cell we want to reach; defaults to upper left of maze
    # start_row and start_col point to the starting point; defaults to lower right of maze
    # input_csv is used to specify the maze we want to load.
    # If no input csv is specified, a random 10x10 maze will be generated
    solve = MazeSolver(goal_row = 2, goal_col = 1, start_row = 4, start_col = 4, input_csv = OUTPUT)

    # Solves the maze generated above and outputs a dictionary with path instructions
    path = solve.generatePath()
    print(path)

    # This method can be called to display a GUI showing the path the maze is solved in
    # This method can be commented out if you only wish to receive the dictionary with the path information
    solve.displayGUI()

if __name__ == "__main__":
    run = main()

