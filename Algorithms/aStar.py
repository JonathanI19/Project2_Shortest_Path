#copied from MAN1986/pyamaze
from pyamaze import maze,agent,textLabel
from queue import PriorityQueue
import sys
def h(cell1,cell2):
    x1,y1=cell1
    x2,y2=cell2

    return abs(x1-x2) + abs(y1-y2)
def aStar(m,start=None):
    if start is None:
       start=(m.rows,m.cols)
    g_score={cell:float('inf') for cell in m.grid}
    g_score[start]=0
    f_score={cell:float('inf') for cell in m.grid}
    f_score[start]=h(start,m._goal)

    open=PriorityQueue()
    open.put((h(start,m._goal),h(start,m._goal),start))
    aPath={}
    while not open.empty():
        currCell=open.get()[2]
        if currCell==m._goal:
            break
        for d in 'ESNW':
            if m.maze_map[currCell][d]==True:
                if d=='E':
                    childCell=(currCell[0],currCell[1]+1)
                if d=='W':
                    childCell=(currCell[0],currCell[1]-1)
                if d=='N':
                    childCell=(currCell[0]-1,currCell[1])
                if d=='S':
                    childCell=(currCell[0]+1,currCell[1])

                temp_g_score=g_score[currCell]+1
                temp_f_score=temp_g_score+h(childCell,m._goal)

                if temp_f_score < f_score[childCell]:
                    g_score[childCell]= temp_g_score
                    f_score[childCell]= temp_g_score + h(childCell, m._goal)
                    open.put((temp_f_score,h(childCell,m._goal),childCell))
                    aPath[childCell]=currCell
    fwdPath={}
    cell=m._goal
    while cell!=start:
        fwdPath[aPath[cell]]=cell
        cell=aPath[cell]
    return fwdPath

if __name__=='__main__':
    m=maze(5,5)
    m.CreateMaze(loadMaze = sys.argv[1])
    m.CreateMaze()
    path=aStar(m)

    a=agent(m,footprints=True)
    m.tracePath({a:path})
    l=textLabel(m,'A Star Path Length',len(path)+1)

    for key in path:
        print(f"{key},{path[key]}")

    if (bool(sys.argv[2])):
        m.run()
    m.run()