#
# ==== Libraries
import curses                           # :: main module
from curses import wrapper              # :: wrapper 
from argparse import ArgumentParser     # :: to add command line arguments 
from Modules import view as View        # :: self gui definition
from Modules import model as Model      # :: logic
from Data import test as test           # :: test maze

# ==== Classes
class Args:
    def __init__(self, controller):
        self.controller = controller
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
        # todo 1: time
        if self.args.t == None:
            self.args.t = .2
        # todo 2: data
        if Model.read_input(self.args.d) != None:
            pass
            # input = Model.adapt_input(Model.read_input(self.args.d))
        # todo 3: depth first
        #
        # todo 4: breadth first
        #
        # todo 5: path color
        if self.args.cp != None:
            self.args.cp = Model.select_color(self.args.cp)
        else:
            self.args.cp = Model.select_color('green')
        # todo 6: obstacle color
        if self.args.co != None:
            self.args.co = Model.select_color(self.args.co)
        else:
            self.args.co = Model.select_color('blue')
        return True
        

class Controller:
    def __init__(self):
        def init_curses():
            self.stdscr = curses.initscr()
            curses.start_color()

        init_curses()
        self.args = Args(self)
        if self.args.validate():
            self.model = Model.Model(self.args, self)
            self.view = View.View(self)
        else:
            print('invalid args')
            return

    def init(self):
        input = test.maze
        Model.find_path(input, 
            self.stdscr, 
            self.args.args.t, 
            self.args.args.df, 
            self.args.args.cp, 
            self.args.args.co)
        self.stdscr.getch()
        # self.view.init()

    def onbtn_Start(self):
        # :: model e aktar veriyi al
        result = self.model.read_input('Data/maze0.txt')
        # :: view e veriyi gonder
        self.view.update_monitor(result)

    def onbtn_End(self):
        pass

    def onbtn_Next(self):
        pass

    def onbtn_Prev(self):
        pass


# ==== Main

def controller(stdscr):   # :: standard output screen
    # == variables
    # :: default maze
    # == arg validation data
    # == Build gui test
    # View.run()

    return
    # == calling main algorithm
    Model.find_path(input, stdscr, args.t, args.df, color_path, color_obs)
    stdscr.getch()

# ==== Initialize
def run():
    controller = Controller()
    controller.init()


# def onbtn_Start(): # todo button naming convention | onBtn_start
#     lines = model.read_input("data/maze0.txt")
#     for line in lines:
#         for char in line:
#             txt_io.insert(END, char + " ")
#             # return
#         txt_io.insert(END, '\n')