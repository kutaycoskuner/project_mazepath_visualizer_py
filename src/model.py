#
# ============================================================================= 
# ==== Libraries
# ============================================================================= 
import curses                           # :: main module
import queue                            # :: queue data structure
import time                             # :: for implementing delay
from argparse import ArgumentParser     # :: to add command line arguments 

# == Disabled
from curses import wrapper              # :: wrapper


# ============================================================================= 
# ==== Classes
# =============================================================================
class Args:
    def __init__(self):
        self.args = None
        self.crt_Args()

    def crt_Args(self):
        # == argument decleration
        parser = ArgumentParser(description='Visualize path in MxN Maze')
        # :: 1 delay in seconds
        parser.add_argument('-t', metavar='delay', type=float,
                        help='delay time on visualization in seconds')
        # :: 2 data
        parser.add_argument('-d', metavar='data', type=str,
                        help='data path for visualization')
        # :: 3 depth first
        parser.add_argument('-df', nargs='?', const=1,       
                        help='apply depth first search')
        # :: 4 breadth first
        parser.add_argument('-bf', nargs='?', const=1,        
                        help='apply breadth first search')
        # :: 5 path color
        parser.add_argument('-cp', type=str,
                            choices=['red', "green", "blue"],
                            help="choose path color for maze")
        # :: 6 path obstacle
        parser.add_argument('-co', type=str,
                            choices=['red', "green", "blue"],
                            help="choose obstacle color for maze")
        self.args = parser.parse_args()

    def validate(self):
        # :: 1: time
        if self.args.t == None:
            self.args.t = .2
        # todo 2: data
        if read_input(self.args.d) != None:
            pass
            # input = Model.adapt_input(Model.read_input(self.args.d))
        # :: 5: path color
        if self.args.cp != None:
            self.args.cp = select_color(self.args.cp)
        else:
            self.args.cp = select_color('green')
        # :: 6: obstacle color
        if self.args.co != None:
            self.args.co = select_color(self.args.co)
        else:
            self.args.co = select_color('blue')
        return True
        

class Model:
    def __init__(self, controller):
        def start_curses():
            self.stdscr = curses.initscr()
            curses.start_color()
        start_curses()

        self.args = Args()
        self.controller = controller
        
    def start(self, input):
        if self.args.validate():
            find_path(input, 
                self.stdscr, 
                self.args.args.t, 
                self.args.args.df, 
                self.args.args.cp, 
                self.args.args.co)
            self.stdscr.getch()
            
    def read_input(self, file_path):
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

# ============================================================================= 
# ==== Functions
# =============================================================================
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
    #
    curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)
    curses.init_pair(2,curses.COLOR_GREEN, curses.COLOR_BLACK)
    curses.init_pair(3,curses.COLOR_BLUE, curses.COLOR_BLACK)
    #
    color_map = {
        'red': curses.color_pair(1),
        'green': curses.color_pair(2),
        'blue': curses.color_pair(3),
    }
    #
    if color != None:
        if type(color) is str:
            color = color.lower()
        if color in color_map:
            return color_map[color] 
    return None