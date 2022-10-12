import curses
from curses import wrapper
import queue
import time
maze = [
    ["#", "O", "#", "#", "#", "#", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", " ", "#", "#", " ", "#", "#", " ", "#"],
    ["#", " ", "#", " ", " ", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", " ", "#"],
    ["#", " ", "#", " ", "#", " ", "#", "#", "#"],
    ["#", " ", " ", " ", " ", " ", " ", " ", "#"],
    ["#", "#", "#", "#", "#", "#", "#", "X", "#"]
]

def print_maze(maze,stdscr,path=[]):
    BLUE=curses.color_pair(1)
    RED=curses.color_pair(2)
    for i,row in enumerate(maze):
        for j, value in enumerate(row):
            if (i,j) in path:
                stdscr.addstr(i,j*2,"@",RED)
            else:
                stdscr.addstr(i,j*2,value,BLUE)

def find_start(maze,start_symbol):
    for i ,row in enumerate(maze):
        for j,value in enumerate(row):
            if value==start_symbol:
                return i,j
    return None

def find_path(maze,stdscr):
    start_symbol="O"
    end="X"
    start_pos=find_start(maze,start_symbol)
    #Defining queue to traverse within Maze
    q=queue.Queue()
    q.put((start_pos,[start_pos]))

    #Adding a set to store all the visited nodes
    visited=set()
    
    #Till queue is not empty or loops returns the path
    while not q.empty():
        current_pos,path=q.get()
        row,col=current_pos

        print_maze(maze,stdscr,path)
        time.sleep(0.3)
        stdscr.refresh()
        

        if maze[row][col]==end:
            return path
        neigbours=find_neigbours(maze,row,col)
        for neigbour in neigbours:
            if neigbour in visited:
                continue
            r,c = neigbour
            if maze[r][c]=="#":
                continue
            new_path=path+[neigbour]
            q.put((neigbour,new_path))
            visited.add(neigbour)

        
        
def find_neigbours(maze,row,col):
    """THis fuction will return a list of all the possible neighbouring postion from starting postion

    Args:
        path (list): Store the row and columns for the BFS
        row (int): it is the row value
        col (int): it is the colum value of the maze
    """
    #Storing all the possible path to traverse within maze
    #FOr UP movement
    neigbours=[]
    if row>0:
        neigbours.append((row-1,col))
    #FOr DOWN movement
    if row+1 <len(maze):
        neigbours.append((row+1,col))

    #For left Movement
    if col>0:
        neigbours.append((row,col-1))
    #For Right Movement
    if col+1<len(maze[0]):
        neigbours.append((row,col+1))
    return neigbours


def main(stdscr):
    #Initialize a Pair of blue and black and id=1
    curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED,curses.COLOR_BLACK)

    blue_and_black=curses.color_pair(1)

    #clearing the curses terminal   
    stdscr.clear()
    #addstr take rows and column
    #stdscr.addstr(0,0,"Hello World!!",blue_and_black)
    #print_maze(maze,stdscr,[])
    find_path(maze,stdscr)
    stdscr.getch()


wrapper(main)