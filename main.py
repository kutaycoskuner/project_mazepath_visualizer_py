#
# ==== Libraries
import curses                           # :: main module
from curses import wrapper              # :: wrapper
import queue                            # :: queue data structure
import time                             # :: for implementing delay
from argparse import ArgumentParser     # :: to add command line arguments 
# import sys                            # :: to add command line arguments


#==== Test Data
maze = [
    ["#","#","#","#","#","#","O","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#"," ","#","#"," ","#","#"," ","#"],
    ["#"," ","#"," "," "," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#"," ","#"],
    ["#"," ","#"," ","#"," ","#","#","#"],
    ["#"," "," "," "," "," "," "," ","#"],
    ["#","#","#","#","#","#","#","X","#"]
]

# ==== Functions
def find_start(maze, start):
    for ii, row in enumerate(maze):
        for jj, value in enumerate(row):
            if value == start:
                return ii, jj

def find_linked(maze, row, col):
    linked = []

    if row > 0:
        linked.append((row-1, col))
    if row + 1 < len(maze):
        linked.append((row+1, col))
    if col > 0:
        linked.append((row, col-1))
    if col+1 < len(maze[0]):
        linked.append((row, col+1))

    return linked

def find_path(maze, stdscr, delay):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    if delay == None:
        delay = 0.0

    nodeQue = queue.Queue()
    nodeQue.put((start_pos, [start_pos]))           # :: node, path
    visited = set()

    while not nodeQue.empty():
        current_pos, path = nodeQue.get()
        row, col = current_pos
        
        stdscr.clear()  # :: clear entire screen
        print_maze(maze, stdscr, path)
        stdscr.refresh()
        time.sleep(delay)
        
        if maze[row][col] == end:
            return path

        links = find_linked(maze, row, col)
        for link in links:
            if link in visited:
                continue

            row, col = link
            if maze[row][col] == "#":
                continue

            new_path = path + [link]
            nodeQue.put((link, new_path))
            visited.add(link)

def print_maze(maze, stdscr, path=[]):
    blue = curses.color_pair(1)
    red = curses.color_pair(2)

    for ii, row in enumerate(maze):
        for jj, value in enumerate(row):
            if (ii, jj) in path:
                stdscr.addstr(ii, jj*2, "X", red)
            else:    
                stdscr.addstr(ii, jj*2, value, blue)


# ==== Main
def main(stdscr):   # :: standard output screen

    # :: argument decleration
    parser = ArgumentParser(description='Visualize path in MxN Maze')
    parser.add_argument('-t', metavar='delay', type=float,
                    help='delay time on visualization in seconds')

    args = parser.parse_args()
    # print(args.t)
    # return

    # :: creating colors
    curses.init_pair(1,curses.COLOR_BLUE, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_RED, curses.COLOR_BLACK)
    blue_black = curses.color_pair(1)

    # stdscr.clear()  # :: clear entire screen
    # stdscr.addstr(2,2, "hello world", blue_black) # :: top left corner of the screen 
    # print_maze(maze, stdscr)
    # stdscr.refresh()
    find_path(maze, stdscr, args.t)
    stdscr.getch()

# ==== Initialize
def run():
    wrapper(main)
run()