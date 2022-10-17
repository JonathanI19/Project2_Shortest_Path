#!/usr/bin/env/ python3

from pyamaze import maze
import sys

# Importing aStar method and ParseFile object
sys.path.append("../")
from Algorithms.aStar import aStar
from parser_script import ParseFile

# Names for Output csv and Input csv
OUTPUT = "./aStar_example_output.csv"
INPUT = "./example_input_2.txt"

# Main function
def main():
    
    # Creating parse object.
    # Input csv is out of order, so N, S, E, W is used to specify the order that they are passed in.
    # Output csv will be normalized to EWNS, provided proper input order is declared.
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT, N=0, S=1, E=2, W=3)
    
    # creating maze object of name m
    m = maze(rows = parse.rows, cols = parse.cols)
    
    # Loading maze based on normalized output csv
    # set x and y variables in CreateMaze to change goal; Default is 1,1
    m.CreateMaze(loadMaze = OUTPUT)
    
    # Using aStar to create fwdPath dictionary, which is used to find path from start to goal.
    fwdPath= aStar(m = m, start = None)
    
    # Print out fwdPath dictionary
    print(fwdPath)
    
    # If user passes in True as an argument after calling this script, a GUI will display the maze
    if len(sys.argv) > 1:
        if sys.argv[1] == "True":    
            m.run()

if __name__ == '__main__':
    main()
