#
# ============================================================================= 
# ==== Libraries
# ============================================================================= 
import curses                           # :: main module
from argparse import ArgumentParser     # :: to add command line arguments 
from src import view as View        # :: self gui definition
from src import model as Model      # :: logic
from Data import test as test           # :: test maze

# ==== Disabled Library
# from curses import wrapper              # :: wrapper 

# ============================================================================= 
# ==== Classes
# ============================================================================= 
class Controller:
    def __init__(self):
        def init_curses():
            self.stdscr = curses.initscr()
            curses.start_color()

        init_curses()
        self.model = Model.Model(self)
        self.view = View.View(self)

    def start(self):
        input = test.maze
        self.model.start(input)
        # self.view.start()

    def onbtn_Start(self):
        # :: model e aktar veriyi al
        result = self.model.read_input('Data/maze0.txt')
        # :: view e veriyi gonder
        self.view.update_monitor(result)
        # 
        # lines = model.read_input("data/maze0.txt")
        #       for line in lines:
        #         for char in line:
        #             txt_io.insert(END, char + " ")
        #             # return
        #         txt_io.insert(END, '\n')

    def onbtn_End(self):
        pass

    def onbtn_Next(self):
        pass

    def onbtn_Prev(self):
        pass

# ============================================================================= 
# ==== Start
# ============================================================================= 
def main():
    controller = Controller()
    controller.start()