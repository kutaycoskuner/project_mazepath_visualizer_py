#
# ============================================================================= 
# ==== Libraries
# ============================================================================= 
import curses                           # :: main module
import copy                             # :: for shallow copy
from argparse import ArgumentParser     # :: to add command line arguments 
from src import view as View            # :: self gui definition
from src import model as Model          # :: logic
from Data import test as test           # :: test maze
from tkinter import filedialog as fd    # :: tkinter file dialog for input file


# ==== Disabled Library
# from curses import wrapper              # :: wrapper 

# ============================================================================= 
# ==== Classes
# ============================================================================= 
class Args:
    def __init__(self):
        self.args = None
        self.crt_Args()
        self.validate()

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
        # :: 7 add gui
        parser.add_argument('-gui', nargs='?', const=1,        
                        help='use gui instead of command line')
        # :: create args
        self.args = parser.parse_args()

    def validate(self):
        # :: 1: time
        if self.args.t == None:
            self.args.t = .2
        # todo 2: data
        if Model.read_input(self.args.d) != None:
            pass
            # input = Model.adapt_input(Model.read_input(self.args.d))
        # :: 5: path color
        if self.args.cp != None:
            self.args.cp = Model.select_color(self.args.cp)
        else:
            self.args.cp = Model.select_color('green')
        # :: 6: obstacle color
        if self.args.co != None:
            self.args.co = Model.select_color(self.args.co)
        else:
            self.args.co = Model.select_color('blue')

class Controller:
    def __init__(self):
        def start_curses():
            self.stdscr = curses.initscr()
            curses.start_color()
        start_curses()
        #
        self.args = Args()
        self.model = Model.Model(self, self.args)
        self.view = View.View(self)

        self.path_list = None


    def start(self):
        input = test.maze
        # :: select inteface
        if self.args.args.gui:
            self.view.start()
        else:
            self.model.start(self.stdscr, input)


    def onbtn_Start(self):
        if self.path_list == None:
            result = self.model.read_input('Data/maze0.txt') # :: model e aktar veriyi al
        self.view.update_monitor(result)  # :: view e veriyi gonder
        self.view.slideCounter = 0

    def onbtn_End(self):
        if self.path_list == None:
            self.create_path_list()
        self.view.slideCounter = len(self.path_list)-1
        self.view.update_monitor(self.path_list[self.view.slideCounter])
        # todo if validate colorize

    def onbtn_Next(self):
        if self.path_list == None:
            self.create_path_list()
        if self.view.slideCounter < len(self.path_list):
            self.view.slideCounter += 1
        self.view.update_monitor(self.path_list[self.view.slideCounter])

    def onbtn_Prev(self):
        if self.path_list == None:
            self.create_path_list()
        if self.view.slideCounter > 0:
            self.view.slideCounter -= 1
        self.view.update_monitor(self.path_list[self.view.slideCounter])

    def onbtn_Browse(self):
        filename = fd.askopenfilename()
        lines = self.model.read_input(filename)
        result = self.model.adapt_input(lines)
        test.maze = result
        self.view.update_monitor(result)  # :: view e veriyi gonder
        self.view.slideCounter = 0

    def create_path_list(self):
        input = copy.deepcopy(test.maze)
        self.path_list = Model.find_path_gui(input)


# ============================================================================= 
# ==== Start
# ============================================================================= 
def main():
    controller = Controller()
    controller.start()