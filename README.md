Project2_Shortest_Path ECE 3432
======
Requirements
------
**Install Pyamaze using PIP**
```
pip3 install pyamaze
```
* *see the [Pyamaze GitHub repository](https://github.com/MAN1986/pyamaze) if you want to install it without a package manager*

**Clone this repository to your working directory**
```
git clone https://github.com/JonathanI19/Project2_Shortest_Path.git
```

Basic Information
------
This repo is an advancement of the [Maze Generation repo](https://github.com/JonathanI19/Project1_Maze_Generation). A new class, MazeSolver, is added to find the shortest path from a given start location and a goal location. The user can choose to display a GUI or not by commenting out a line in the example file. Regardless, the code will print the shortest path using the AStar algorithm  to the command line. Two example codes are provided to the user. 

# maze_solver_script.py Info
This python script utilizes a class to parse the inputs goal row, goal column, start row, start column, and finally the input file. It requires the maze, agent, and COLOR classes from the pyamaze package. It outputs the shortest path to the command line. The default values for the goal row and columns are 1.

Examples
------
The example codes are found in the Examples Folder. For the main functions in both examples, if no input CSV file is specified, a random 10x10 maze will be generated. The default starting point is the bottom right corner. The default goal is the upper left corner.

## Example 1 Usage – maze_solver_example_1.py
In maze_solver_example_1.py, the input CSV file is given in (and must be) the proper order of East-West-North-South. The output CSV file will also be ordered East-West-North-South if the input CSV file was correct. **Comment out line 34 if you wish to disable the GUI.**

Command to run example 1 (make sure you are in the Examples directory):
```
python maze_solver_example_1.py
```
* *python command may very depending on your version. if that command doesn't work, replace python with python3. otherwise, check if Python is added to your system PATH*

Here is the output for this example if the GUI is enabled:

![GUI DIsplay](https://media.giphy.com/media/EGLTGdAqBSuICKPGKl/giphy.gif)

Here is the displayed output path:
```
{(2, 2): (2, 1), (1, 2): (2, 2), (1, 3): (1, 2), (2, 3): (1, 3), (2, 4): (2, 3), (3, 4): (2, 4), (4, 4): (3, 4)}
```
## Example 2  Usage - maze_solver_example_2.py
This example is similar to example 1, except the input csv is out of order. N, S, E, W is used to specify the order that they are passed in. The output csv will be normalized to EWNS, provided proper input order is declared. **Comment out line 35 if you do not wish to see the GUI.**

Command to run example 2 (make sure you are in the Examples directory):
```
python maze_solver_example_2.py
```
* *python command may very depending on your version. if that command doesn't work, replace python with python3. otherwise, check if Python is added to your system PATH*

Here is the output for this example if the GUI is enabled:

![GUI DIsplay](https://media.giphy.com/media/OHGjlPLvqeC4DzyFUa/giphy.gif)

Here is the displayed output path:
```
{(5, 4): (5, 5), (5, 3): (5, 4), (4, 3): (5, 3), (3, 3): (4, 3), (3, 2): (3, 3), (2, 2): (3, 2), (1, 2): (2, 2), (1, 1): (1, 2)}
```
