# Project2_Shortest_Path ECE 3432

## Requirements
Install [Pyamaze](https://github.com/MAN1986/pyamaze)

```
pip3 install pyamaze
```

Clone this repo
```
git clone https://github.com/JonathanI19/Project2_Shortest_Path.git ./
```


## Basic Information
This repo is an evolution of [Project1_Maze_Generation](https://github.com/JonathanI19/Project1_Maze_Generation)

For information on how to parse and generate a properly formatted maze csv, please see the above link. Instructions are located in the README.

The main purpose of this repo is to create a maze solver class that enables the user to generate a path file from a specified start point within the maze, to a specified end point.


## maze_solver_script.py Info
This python script utilizes a class to create the appropriate pyamaze objects and generate a maze from a specified input csv.

Currently, the script is set up to utilize the A-Star algorithm, which is located in the Algorithms directory.

Additionally, there is a displayGUI() method, that will enable the user to activate an animated display of the maze being solved.


## Example 1 Usage

Example 1 takes in a set of input data, parses it into a properly formatted csv document, and then loads this data into a maze object

