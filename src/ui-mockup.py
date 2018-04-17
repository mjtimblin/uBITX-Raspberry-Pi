#!/usr/bin/env python3

from tkinter import *
from time import sleep

WIDTH = 480
HEIGHT = 320

class UI:
    master = None
    txRxLabel = None
    vfoLabel = None

    def __init__(self, master):
        self.master = master
        for i in range (0, 20):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)
        self.vfoLabel = Label(self.master, text="VFO", fg="white", bg="green", font=("Ariel", 20))
        self.txRxLabel = Label(self.master, text=" RX ", fg="white", bg="green", font=("Ariel", 20))
        self.vfoLabel.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")
        self.txRxLabel.bind("<Button-1>", self.txOn)
        self.txRxLabel.bind("<ButtonRelease-1>", self.txOff)

    def txOn(self, events):
        self.txRxLabel = Label(self.master, text=" TX ", fg="white", bg="red", font=("Ariel", 20))
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")
        self.txRxLabel.bind("<Button-1>", self.txOn)
        self.txRxLabel.bind("<ButtonRelease-1>", self.txOff)

    def txOff(self, events):
        self.txRxLabel = Label(self.master, text=" RX ", fg="white", bg="green", font=("Ariel", 20))
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")
        self.txRxLabel.bind("<Button-1>", self.txOn)
        self.txRxLabel.bind("<ButtonRelease-1>", self.txOff)

def quit(events):
    root.destroy()

root = Tk()
#root.attributes('-fullscreen', True)
root.geometry('%dx%d' % (WIDTH, HEIGHT))
root.configure(background="black")
root.bind("<Escape>", quit)
ui = UI(root)

root.mainloop()
