#
# ==== Libraries
# from tkinter import *
import tkinter as tk
from tkinter import ttk
# from tkinter import scrolledtext                   # :: gui library
from Modules import model as model

# ==== Classes
class View(tk.Tk):

    # == Variables
    # :: colors
    col_darkGray1 = "#202020"
    col_darkGray2 = "#242424"
    col_darkGray3 = "#262626"
    col_hellGray1 = "#dbdbdb"
    col_white = "#ffffff"
    col_test = "#ccc"
    # :: padding
    cnstPad = 10

    # == constructor
    def __init__(self, controller):
        # :: inherit from tk
        super().__init__() 
        #
        # self.controller = controller
        #
        # self.title('Potato')
        self.value_var = tk.StringVar()
        #
        # self._crt_titlebar()
        self._crt_main_frame()
        # self._crt_entry()
        self._crt_ctrl_buttons()

    # == elements
    def main(self):
        self.geometry("720x480")
        # self.resizeable(False, False)
        # self.overrideredirect(True) # turn off title bar, geometry
        self.title("Mazepath Visualizer")
        self.iconbitmap()
        self.configure(background=self.col_darkGray1)
        self.mainloop()

    def _crt_titlebar(self):
        frm_title = tk.Frame(self, bg=self.col_darkGray1, relief="raised", bd=0, highlightthickness=0)
        frm_title.pack(fill='x')
        #
        btn_wndw_ext = tk.Button(frm_title, text="✕", padx=4, pady=2, command=self.destroy, fg=self.col_white, bg=self.col_darkGray1, bd= 0, highlightthickness=0)# &#xE106;
        btn_wndw_ext.pack(side='right')
        #
        btn_wndw_max = tk.Button(frm_title, text="🗖", padx=4, pady=2, fg=self.col_white, bg=self.col_darkGray1, bd= 0, highlightthickness=0)# &#xE739;"
        btn_wndw_max.pack(side='right')
        #
        btn_wndw_min = tk.Button(frm_title, text="—", padx=4, pady=2, fg=self.col_white, bg=self.col_darkGray1, bd= 0, highlightthickness=0)# &#xE949;
        btn_wndw_min.pack(side='right')

    def _crt_main_frame(self):
        # :: main window
        self.frm_main = tk.Frame(self, bg=self.col_darkGray2, relief="raised", bd=0, highlightthickness=0)
        self.frm_main.pack(fill='both', expand=1)
        # :: input output screen
        txt_io = tk.Text(self.frm_main, bg=self.col_darkGray3, fg=self.col_hellGray1, bd=1, highlightthickness=0)
        txt_io.pack(pady=10)
        # :: report line
        lbl_report = tk.Label(self.frm_main, bg="gray", width=60)
        lbl_report.pack()
        #
        # self.main_frm = ttk.Frame(self)
        # self.main_frm.pack(padx=self.cnstPad, pady=self.cnstPad)

    def _crt_ctrl_buttons(self):
        frm_ctrl = tk.Frame(self.frm_main, bg=self.col_darkGray2, relief="raised", bd=0, highlightthickness=0)
        frm_ctrl.pack()
        #
        btn_toStart = tk.Button(frm_ctrl, text="Start", command=self.onbtn_Start)
        btn_toStart.pack(side="left", padx=10)
        btn_toEnd = tk.Button(frm_ctrl, text="End", command=self.onbtn_End)
        btn_toEnd.pack(side="left", padx=10)
        btn_prev = tk.Button(frm_ctrl, text="prev", command=self.onbtn_Prev)
        btn_prev.pack(side="left", padx=10)   
        btn_next = tk.Button(frm_ctrl, text="next", command=self.onbtn_Next)
        btn_next.pack(side="left", padx=10)

    def onbtn_Start(self):
        print('hello world')

    def onbtn_End(self):
        pass

    def onbtn_Next(self):
        pass

    def onbtn_Prev(self):
        pass

# ==== Functions
# def onbtn_Start(): # todo button naming convention | onBtn_start
#     lines = model.read_input("data/maze0.txt")
#     for line in lines:
#         for char in line:
#             txt_io.insert(END, char + " ")
#             # return
#         txt_io.insert(END, '\n')

