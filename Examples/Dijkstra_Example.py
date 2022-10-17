#!/usr/bin/env/ python3

from pyamaze import maze
import sys

# Importing Dijkstra method and ParseFile object
sys.path.append("../")
from Algorithms.dijkstra import dijkstra
from parser_script import ParseFile

# Names for Output csv and Input csv
OUTPUT = "./dijsktra_example_output.csv"
INPUT = "./example_input_1.txt"

# Main function
def main():
    
    # Creating parse object.
    # Input file being used here is in proper order so we don't need to specify indexes of EWNS
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT)
    
    # creating maze object of name m
    m = maze(rows = parse.rows, cols = parse.cols)
    
    # Loading maze based on output csv
    # You can change goal location by following the format shown below:
    # m.CreateMaze(loadMaze = OUTPUT, x=1, y=1)
    m.CreateMaze(loadMaze = OUTPUT)
    
    # Using dijkstra to create fwdPath dictionary, which is used to find path from start to goal
    fwdPath, visited = dijkstra(m = m, start = None)
    
    # Print out fwdPath dictionary
    print(fwdPath)
    
    # If user passes in True as an argument after calling this script, a GUI will display the maze
    if len(sys.argv) > 1:
        if sys.argv[1] == "True":    
            m.run()

if __name__ == '__main__':
    main()
