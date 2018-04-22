#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from time import sleep
import os

WIDTH = 480
HEIGHT = 320

class UI:
    master = None
    txRxLabel = None
    vfoLabel = None
    exitLabel = None

    def __init__(self):
        self.master = Tk()
        #self.master.attributes('-fullscreen', True)
        self.master.geometry('%dx%d' % (WIDTH, HEIGHT))
        self.master.configure(background="black")
        self.master.bind("<Escape>", quit)
        for i in range (0, 20):
            self.master.grid_columnconfigure(i, weight=1)
            self.master.grid_rowconfigure(i, weight=1)
        powerImage = PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + "/images/shutdown-48x48.png")
        self.vfoLabel = Label(self.master, text="VFO", fg="white", bg="green", font=("Ariel", 20))
        self.txRxLabel = Label(self.master, text=" RX ", fg="white", bg="green", font=("Ariel", 20))
        self.exitLabel = Label(self.master, image=powerImage, bg="black")
        self.vfoLabel.grid(row=0, column=0, columnspan=4, sticky="nsew")
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")
        self.exitLabel.grid(row=19, column=19, sticky="nsew")
        self.exitLabel.bind("<Button-1>", self.promptExit)
        self.master.mainloop()

    def txOn(self, events):
        self.txRxLabel = Label(self.master, text=" TX ", fg="white", bg="red", font=("Ariel", 20))
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")

    def txOff(self):
        self.txRxLabel = Label(self.master, text=" RX ", fg="white", bg="green", font=("Ariel", 20))
        self.txRxLabel.grid(row=0, column=16, columnspan=4, sticky="nsew")

    def promptExit(self, events):
        result = messagebox.askquestion("Shutdown", "Are you sure you want to shutdown?", icon='warning')
        if result == 'yes':
            os.system("shutdown now -h")

    def quit(self, events):
        self.master.destroy()

ui = UI()