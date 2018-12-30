from tkinter import *
import json
from pprint import pprint
import manifestgenerator as mfg

metadata = []
master = Tk()
len_  = 0
var = []
list_pkg = []

def center_window(width=300, height=200):
    master.title('Salesforce Manifest Generator')
    # get screen width and height
    screen_width = master.winfo_screenwidth()
    screen_height = master.winfo_screenheight()

    # calculate position x and y coordinates
    x = (screen_width/2) - (width/2)
    y = (screen_height/2) - (height/2)
    master.geometry('%dx%d+%d+%d' % (width, height, x, y))
    Button(master, text='Submit', command=mfg.call_stack).grid(row=4, sticky=W, pady=4)
    Button(master, text='Quit', command=master.quit).grid(row=10, sticky=W, pady=4)

def util():
    with open('./config.json') as f:
        data = json.load(f)
    global metadata
    metadata  = list(data["metadata"])

def checkbox():
    global len_
    len_ = len(metadata)
    global var
    var = [None] * len_
    car = [None] * len_
    for i in range(len_):
        var[i] = IntVar()
        Checkbutton(master, text=str(metadata[i]), variable=var[i]).grid(row=i, sticky=W)
    mainloop()

def flow():
    center_window(500, 400) 
    util()
    checkbox()


if __name__ == "__main__":
    flow()