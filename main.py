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
def read_input(file_path):
    if file_path != None:
        try:
            file = open(file_path)
        except IOError:
            print('I could not access the file')
            return None
        else:
            with file as data:
                lines = []
                for line in data:
                    lines.append([])
                    for char in line:
                        if char != "\n" and char != " ":
                            lines[-1].append(char)
            return lines

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

def find_path(maze, stdscr, delay, df, color_path, color_obs):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    if delay == None:
        delay = 0.0
    if df != None:
        nodeQue = queue.LifoQueue()
    else:
        nodeQue = queue.Queue()
    
    nodeQue.put((start_pos, [start_pos]))           # :: node, path
    visited = set()

    while not nodeQue.empty():
        current_pos, path = nodeQue.get()
        row, col = current_pos
        
        stdscr.clear()  # :: clear entire screen
        print_maze(maze, stdscr, color_path, color_obs,  path)
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

def print_maze(maze, stdscr, color_path, color_obs, path=[]):
    for ii, row in enumerate(maze):
        for jj, value in enumerate(row):
            if (ii, jj) in path:
                stdscr.addstr(ii, jj*2, "X", color_path)
            else:    
                stdscr.addstr(ii, jj*2, value, color_obs)

def adapt_input(input, start="0", end="1", open=".", closed="#"):
    for ii, line in enumerate(input):
        for jj, char in enumerate(line):
            if char == start:
                input[ii][jj] = "O"
            if char == end:
                input[ii][jj] = "X"
            if char == open:
                input[ii][jj] = " "
            if char == closed:
                input[ii][jj] = "#"
    return input

def select_color(color=None):
    color_red = curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)
    color_green = curses.init_pair(2,curses.COLOR_GREEN, curses.COLOR_BLACK)
    color_blue = curses.init_pair(3,curses.COLOR_BLUE, curses.COLOR_BLACK)

    if color != None:
        color = color.lower()
        if color == "red":
            return curses.color_pair(1)
        if color == "green":
            return curses.color_pair(2)
        if color == "blue":
            return curses.color_pair(3)
    return None



# ==== Main
def main(stdscr):   # :: standard output screen

    # :: variables
    input = maze

    # == argument decleration
    parser = ArgumentParser(description='Visualize path in MxN Maze')
    
    # :: value params
    parser.add_argument('-t', metavar='delay', type=float,
                    help='delay time on visualization in seconds')

    parser.add_argument('-d', metavar='data', type=str,
                    help='data path for visualization')

    # :: binary params
    parser.add_argument('-df', nargs='?', const=1,       
                    help='apply depth first search')

    parser.add_argument('-bf', nargs='?', const=1,        
                    help='apply breadth first search')

    # :: discrete params
    parser.add_argument('-cp', type=str,
                        choices=['red', "green", "blue"],
                        help="choose path color for maze")

    parser.add_argument('-co', type=str,
                        choices=['red', "green", "blue"],
                        help="choose obstacle color for maze")
    
    args = parser.parse_args()

    # todo validate args
    # == arg validation data
    if read_input(args.d) != None:
        input = adapt_input(read_input(args.d))

    # :: creating colors
    color_path, color_obs = None, None
    if args.cp != None:
        color_path = select_color(args.cp)
    if color_path == None:
        color_path = select_color('green')
    
    if args.co != None:
        color_obs = select_color(args.co)
    if color_obs == None:
        color_obs = select_color('blue')
            
    # == calling main algorithm
    find_path(input, stdscr, args.t, args.df, color_path, color_obs)
    stdscr.getch()

# ==== Initialize
def run():
    wrapper(main)
run()