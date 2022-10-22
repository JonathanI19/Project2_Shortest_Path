Project2_Shortest_Path ECE 3432
======
Requirements
------
Install Pyamaze
```
git clone https://github.com/MAN1986/pyamaze.git ./
pip3 install pyamaze
```
Clone this repo
```
git clone https://github.com/JonathanI19/Project2_Shortest_Path.git ./
```

Basic Information
------
This repo is an advancement on the previous Maze Generation repo. A new function, MazeSolver, is incorporated to find the shortest path from a given start location and a goal location. The user can choose to display a GUI or not by commenting out a line in the example file. Regardless, the code will print the shortest path using the AStar algorithm  to the command line. An example code is provided for the user. 

maze_solver_script.py Info
------
This python script utilizes a class to parse the inputs goal row, goal column, start row, start column, and finally the input file. It outputs the shortest path to the command line. The default values for the goal row and coloumns are 1.

Example 1 Usage – maze_solver_example_1.py
------
In maze_solver_example_1.py, the input csv file is given in (and must be) the proper order of EWNS. The output csv will also be EWNS if the input csv file was correct. Comment out line 31 if you wish to disable the GUI.

```
python maze_solver_example_1.py
```
* *if that command doesn't work, replace python with python3*

Here is the output for this example if the GUI is enabled:
![GUI DIsplay](https://media.giphy.com/media/EGLTGdAqBSuICKPGKl/giphy.gif)



## Main Function



Example 2  Usage - maze_solver_example_2.py
------
This example is similar to example 1, except the input csv is out of order. N, S, E, W is used to specify the order that they are passed in. The output csv will be normalized to EWNS, provided proper input order is declared. Comment out line 35 if you do not wish to see the GUI.
```
python maze_solver_example_2.py
```
* *if that command doesn't work, replace python with python3*

Here is the output for this example if the GUI is enabled:
![GUI DIsplay](https://media.giphy.com/media/OHGjlPLvqeC4DzyFUa/giphy.gif)



## Main Function


