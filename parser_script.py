#!/usr/bin/env python3

# Class for parsing files
class ParseFile:
    def __init__(self, input_file="./input.txt", output_file="./output.csv", N=2, S=3, E=0, W=1):

        # Variable Initialization
        self.N, self.S, self.E, self.W=N,S,E,W
        self.output_file=output_file
        self.file = open(input_file, 'r')
        self.lines = self.file.readlines()
        self.parsed_lines = []
        self.cols = 0
        self.rows = 0

        # Calling parse_lines() method
        self.parse_lines()

        # Calling get_dim() method
        self.get_dim()

        # Initialzing 3d matrix
        self.arr = [[[0 for x in range(4)] for y in range(self.cols)] for z in range(self.rows)]

        # Calling computer_arr() method
        self.compute_arr()

        # Calling write_csv() method
        self.write_csv()

    # Cleaning up lines for easier processing
    def parse_lines(self):
        
        # Looping through lines and removing extraneous characters
        for line in self.lines:
            temp = line.replace('"', '').replace(')', '').replace('(', '').replace(',',' ')
            temp = temp.split()

            # Appending parsed lines without extraneous characters
            self.parsed_lines.append(temp)
        return
    
    # Collecting number of columns and rows
    def get_dim(self):
        for line in self.parsed_lines:
            if int(line[0]) > self.rows:
                self.rows = int(line[0])
            if int(line[1]) > self.cols:
                self.cols = int(line[1])
        return

    # Computing and organizing array
    def compute_arr(self):
        for line in self.parsed_lines:
            row = int(line[0])-1
            col = int(line[1])-1
            for i in range (2,6):
                if float(line[i]) > 0.25:
                    line[i] = 1
                else:
                    line[i] = 0
            self.arr[row][col] = line[2:]

    #Writing to new csv with proper formatting for loading into pyamaze maze generation
    def write_csv(self):

        # Opening output file with write permissions
        output = open(self.output_file, "w")

        # Writing first line of csv
        output.write("  cell  ,E,W,N,S")

        # Incrementing through each line and data point
        for j in range(self.cols):
            for i in range(self.rows):
                
                # Writing data in proper formatting
                output.write('\n"({}, {})",{},{},{},{}'.format((i+1),(j+1),self.arr[i][j][self.E],self.arr[i][j][self.W],self.arr[i][j][self.N],self.arr[i][j][self.S]))
    
        
if __name__=="__main__":
    main = ParseFile()
