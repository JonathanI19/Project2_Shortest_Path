#!/usr/bin/env/ python3

from pyamaze import maze, agent, COLOR
import sys
sys.path.append("../")
from Algorithms.aStar import aStar
from parser_script import ParseFile

OUTPUT = "./aStar_example_output.csv"
INPUT = "./example_input_2.txt"
# GOAL is defined in agent
# START is defined in agent
# Highlighted Green is defined in createmaze

def main():
    parse = ParseFile(input_file = INPUT, output_file = OUTPUT, N=0, S=1, E=2, W=3)
    m = maze(rows = parse.rows, cols = parse.cols)
    m.CreateMaze(loadMaze = OUTPUT)
    fwdPath= aStar(m = m, start = None)
    print(fwdPath)
    a = agent(m, footprints=True, color=COLOR.blue, filled=True, goal=(2,2))
    m.tracePath({a:fwdPath}, delay=300)
    if len(sys.argv) > 1:
        if sys.argv[1] == "True":    
            m.run()

if __name__ == '__main__':
    main()