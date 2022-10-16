#!/usr/bin/env/ python3

from pyamaze import maze
import sys
sys.path.append("../")
from Algorithms.dijkstra import dijkstra
from parser_script import ParseFile

OUTPUT = "./dijsktra_example_output.csv"
INPUT = "./example_input_1.txt"

def main():
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT)
    m = maze(rows = parse.rows, cols = parse.cols)
    m.CreateMaze(loadMaze = OUTPUT)
    fwdPath, visited = dijkstra(m = m, start = None)
    print(fwdPath)
    if len(sys.argv) > 1:
        if sys.argv[1] == "True":    
            m.run()

if __name__ == '__main__':
    main()