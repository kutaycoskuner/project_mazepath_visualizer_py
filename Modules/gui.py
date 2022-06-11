#
# ==== Libraries
from tkinter import *
from tkinter import scrolledtext                   # :: gui library
from Modules import model as model

# ==== Functions
def test():
    outputFromData()

def outputFromData():
    lines = model.read_input("data/maze0.txt")
    for line in lines:
        for char in line:
            txt_io.insert(END, char + " ")
            # return
        txt_io.insert(END, '\n')
        
def pruneIO():
    txt_io.delete('1.0', END)

# ==== Variables
# :: main frame
gui = Tk() # instantiate gui class

# :: colors
col_darkGray1 = "#202020"
col_darkGray2 = "#242424"
col_darkGray3 = "#262626"
col_hellGray1 = "#dbdbdb"
col_white = "#ffffff"
col_test = "#ccc"

# == create sub-gui object
lbl_input =Label(gui, text="Input")
lbl_output =Label(gui, text="Output")

# :: title bar
frm_title = Frame(gui, bg=col_darkGray1, relief="raised", bd=0, highlightthickness=0)
btn_wndw_min = Button(frm_title, text="—", padx=4, pady=2, fg=col_white, bg=col_darkGray1, bd= 0, highlightthickness=0)# &#xE949;
btn_wndw_max = Button(frm_title, text="🗖", padx=4, pady=2, fg=col_white, bg=col_darkGray1, bd= 0, highlightthickness=0)# &#xE739;"
btn_wndw_ext = Button(frm_title, text="✕", padx=4, pady=2, command=gui.destroy, fg=col_white, bg=col_darkGray1, bd= 0, highlightthickness=0)# &#xE106;

# :: main window
frm_main = Frame(gui, bg=col_darkGray2, relief="raised", bd=0, highlightthickness=0)
txt_io = Text(frm_main, bg=col_darkGray3, fg=col_hellGray1, bd=1, highlightthickness=0)

# :: frame control
lbl_report = Label(frm_main, bg=col_darkGray2, width=60)
#
frm_ctrl = Frame(frm_main, bg=col_darkGray2, relief="raised", bd=0, highlightthickness=0)
btn_toStart = Button(frm_ctrl, text="Start", command=test)
btn_toEnd = Button(frm_ctrl, text="End", command=pruneIO)
btn_prev = Button(frm_ctrl, text="prev")
btn_next = Button(frm_ctrl, text="next")

# ==== Main
def run():
    # :: base frame
    gui.geometry("720x480")
    # gui.resizeable(False, False)
    # gui.overrideredirect(True) # turn off title bar, geometry
    gui.title("Mazepath Visualizer")
    # gui.iconbitmap()
    gui.configure(background=col_darkGray1)

    # :: title frame positioning
    frm_title.pack(fill=X)
    btn_wndw_ext.pack(side=RIGHT)
    btn_wndw_max.pack(side=RIGHT)
    btn_wndw_min.pack(side=RIGHT)
    
    # :: main frame
    frm_main.pack(fill='both', expand=1)
    txt_io.pack(pady=10)
    lbl_report.pack(side="top")

    frm_ctrl.pack()
    btn_toStart.pack(side="left", padx=10)
    btn_prev.pack(side="left", padx=10)
    btn_next.pack(side="left", padx=10)
    btn_toEnd.pack(side="left", padx=10)
    # txt_io.insert(INSERT, 'potato')
    # txt_output.pack()
    # entry1.grid(row=0, column=10, padx=10, pady=10, ipadx=20, ipady=20)
    # lbl_input.pack()

    # frm_output.pack()
    # lbl_output.pack()

    # btn_prev.pack()
    # btn_next.pack()

    # frm_mainWndw.pack(expand=1, fill=BOTH)


    # shoving it onto te screen
    # myLabel1.pack()
    # myLabel2.pack()

    # :: main loop
    gui.mainloop()