#
# ==== Libraries
import curses                           # :: main module
from curses import wrapper              # :: wrapper 
from argparse import ArgumentParser     # :: to add command line arguments 
from Modules import view as View        # :: self gui definition
from Modules import model as Model      # :: logic
from Data import test as test           # :: test maze

# ==== Classes
class Controller:
    def __init__(self):
        # self.model = Model.Model(self)
        self.view = View.View(self)
  
    def main(self):
        # print('i am controller')
        self.view.main()


# ==== Main

def controller(stdscr):   # :: standard output screen
    # == variables
    # :: default maze
    input = test.maze

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

    # == arg validation data
    # todo validate args
    if Model.read_input(args.d) != None:
        input = Model.adapt_input(Model.read_input(args.d))
    # :: creating colors
    color_path, color_obs = None, None
    if args.cp != None:
        color_path = Model.select_color(args.cp)
    if color_path == None:
        color_path = Model.select_color('green')
    if args.co != None:
        color_obs = Model.select_color(args.co)
    if color_obs == None:
        color_obs = Model.select_color('blue')


    # == Build gui test
    # View.run()

    return
    # == calling main algorithm
    Model.find_path(input, stdscr, args.t, args.df, color_path, color_obs)
    stdscr.getch()

# ==== Initialize
def run():
    controller = Controller()
    controller.main()
    # wrapper(controller)