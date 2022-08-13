#
# ============================================================================= 
# ==== Libraries
# ============================================================================= 
import curses                           # :: main module
import queue                            # :: queue data structure
import time                             # :: for implementing delay
import copy                             # :: copy parameter
from argparse import ArgumentParser     # :: to add command line arguments 
from library import Queue as Que        # :: self queue

# == Disabled
from curses import wrapper              # :: wrapper


# ============================================================================= 
# ==== Classes
# =============================================================================
class Model:
    def __init__(self, controller, args):
        self.controller = controller
        self.args = args

    def start(self, stdscr, input):
            find_path_cli(input, 
                stdscr, 
                self.args.args.t, 
                self.args.args.df, 
                self.args.args.cp, 
                self.args.args.co)
            stdscr.getch()
            
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

    def print_2d_array(self, maze):
        for ii, row in enumerate(maze):
            print(row)

    def adapt_input(self, input, start="0", end="1", open=".", closed="#"):
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

    def validate_input(self, maze):
        dict = {
            "O": False,
            "X": False,
        }
        block = "#"
        set_inner = {"#", " "}
        maxSize = 20

        if len(maze) > maxSize or len(maze[0]) > maxSize:
            return False

        for ii, line, in enumerate(maze):
            for jj, char in enumerate(line):
                if ii==0 or ii==len(maze)-1 or jj==0 or jj==len(line)-1:
                    if not char in dict and char != block:
                        return False
                    if char in dict:
                        if dict[char] == False:
                            dict[char] = True
                        else:
                            return False
                else:
                    if char not in set_inner:
                        self.print_2d_array(maze)
                        print(char)
                        return False

        return True

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

def find_path_cli(maze, stdscr, delay, df, color_path, color_obs):
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

    steps = [maze]
    # counter = 0
    while not nodeQue.empty():
        # counter += 1
        current_pos, path = nodeQue.get()
        row, col = current_pos
        
        if True:
            stdscr.clear()  # :: clear entire screen
            print_maze(maze, stdscr, color_path, color_obs,  path)
            stdscr.refresh()
            time.sleep(delay)
            #
            # print(maze[row][col], path)
            if maze[row][col] == end:
                return path
        else: 
            steps.append(produce_path(maze, path))

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

def find_path_gui(maze):
    start = "O"
    end = "X"
    start_pos = find_start(maze, start)
    
    if True:
        delay = 0.0
    # todo df/bf ayari yap
    if False:
        nodeQue = queue.LifoQueue()
    else:
        nodeQue = queue.Queue()
    
    nodeQue.put((start_pos, [start_pos]))           # :: node, path
    visited = set()
    visited.add(start_pos)

    steps = []
    counter = 0
    while not nodeQue.empty():
        counter += 1
        current_pos, path = nodeQue.get()
        # nodeQue.pop()
        row, col = current_pos
        # path listesine ekleme
        steps.append(produce_path(maze, path))
        # cozume geldiysek bitir
        if maze[row][col] == end:
            steps[-1] = final_path(steps[-1], path, visited)
            break

        visited.add(current_pos)
        links = find_linked(maze, row, col)
        
        for link in links:
            if link in visited:
                continue

            row, col = link
            if maze[row][col] == "#":
                continue

            new_path = path + [link]
            nodeQue.put((link, new_path))
                
    return steps

def check_blocked(maze, row, col, visited):
    links = find_linked(maze, row, col)
    blocked = True
    for link in links:
        if link in visited:
            continue
        row, col = link
        if maze[row][col] == "#":
            continue
        blocked = False

    return blocked

def print_maze(maze, stdscr, color_path, color_obs, path=[]):
    for ii, row in enumerate(maze):
        for jj, value in enumerate(row):
            if (ii, jj) in path:
                stdscr.addstr(ii, jj*2, "X", color_path)
            else:    
                stdscr.addstr(ii, jj*2, value, color_obs)

def produce_path(maze, path=[], pathfinding=None):
    no_edit = {"#", "O", "X"}
    # print(path)
    if pathfinding is None:
        pathfinding = copy.deepcopy(maze)
    for ii, row in enumerate(maze):
        for jj, value in enumerate(row):
            if (ii, jj) in path and (maze[ii][jj] not in no_edit):
                pathfinding[ii][jj] = "1"
    return pathfinding

def final_path(maze, path=[], visited=[]):
    last = copy.deepcopy(maze)
    bond = {'O','X','0','1'}
    for ii, cell in enumerate(reversed(path)):
        row, col = cell        
        if last[row][col] in bond:
            last[row][col] = '2'
    return last


def reset_path(maze, path=[]):
    pass

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
