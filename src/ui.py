#!/usr/bin/env python3

from tkinter import *
from tkinter import messagebox
from time import sleep
import os

# Color Definitions
BLACK = "#000000"
DARK_GRAY = "#282828"
WHITE = "#FFFFFF"
GREEN = "#00FF00"
RED = "#FF0000"
LIGHT_BLUE = "#4496FF"
BLUE = "#0000FF"
YELLOW = "#FFFF00"

BANDS = ["80m", "40m", "30m", "20m", "17m", "15m", "12m", "10m"]
MIN_BAND = [3500000, 7000000, 10100000, 14000000, 18068000, 21000000, 24890000, 28000000]
MAX_BAND = [4000000, 7300000, 10150000, 14350000, 18168000, 21450000, 24990000, 29700000]
WIDTH = 480
HEIGHT = 320


class UI:
    master = None
    exitLabelButton = None
    rxLabel = None
    txLabel = None
    freqALabel = None
    freqBLabel = None
    vfoABLabelButton = None
    modeLabelButton = None
    bandLabelButton = None
    splitLabelButton = None

    def __init__(self):
        self.master = Tk()
        #self.master.attributes('-fullscreen', True)
        self.master.geometry('%dx%d' % (WIDTH, HEIGHT))
        self.master.configure(background="black")
        self.master.bind("<Escape>", quit)
        
        self.showTxOff()
        self.showFrequencyA(12345678)
        self.showFrequencyB(1234567)
        
        self.vfoABLabelButton = Label(self.master, text="VFO A/B", fg=WHITE, bg=LIGHT_BLUE, height=2, width=8, font=("Ariel", 12))
        self.vfoABLabelButton.place(x = 390, y = 10)
        self.modeLabelButton = Label(self.master, text="Mode", fg=WHITE, bg=LIGHT_BLUE, height=2, width=8, font=("Ariel", 12))
        self.modeLabelButton.place(x = 390, y = 60)
        self.bandLabelButton = Label(self.master, text="Band", fg=WHITE, bg=LIGHT_BLUE, height=2, width=8, font=("Ariel", 12))
        self.bandLabelButton.place(x = 390, y = 110)
        self.bandLabelButton = Label(self.master, text="Split", fg=WHITE, bg=LIGHT_BLUE, height=2, width=8, font=("Ariel", 12))
        self.bandLabelButton.place(x = 390, y = 160)

        powerImage = PhotoImage(file=os.path.dirname(os.path.realpath(__file__)) + "/images/shutdown-48x48.png")
        self.exitLabelButton = Label(self.master, image=powerImage, bg=BLACK)
        self.exitLabelButton.place(x = 425, y = 265)
        self.exitLabelButton.bind("<Button-1>", self.promptExit)
        
        self.master.mainloop()

    def showBand(self, band):
        self.bandLabel = Label(self.master, text=band, fg=WHITE, bg=BLUE, height=1, width=6, font=("Ariel", 20))
        self.bandLabel.place(x = 0, y = 100)

    def showFrequencyA(self, frequency):
        displayFreq = str(int(frequency / 1000000)) + "." + str(int((frequency / 1000) % 1000)) + "." + str(frequency % 1000)
        self.freqALabel = Label(self.master, text=displayFreq, fg=YELLOW, bg=BLACK, height=1, width=10, font=("LCD Solid", 30), anchor="e")
        self.freqALabel.place(x = 20, y = 10)

    def showFrequencyB(self, frequency):
        displayFreq = str(int(frequency / 1000000)) + "." + str(int((frequency / 1000) % 1000)) + "." + str(frequency % 1000)
        self.freqBLabel = Label(self.master, text=displayFreq, fg=LIGHT_BLUE, bg=BLACK, height=1, width=10, font=("LCD Solid", 30), anchor="e")
        self.freqBLabel.place(x = 20, y = 100)

    def showTxOff(self, events=None):
        self.rxLabel = Label(self.master, text="RX", fg=GREEN, bg=BLACK, font=("Ariel", 16))
        self.rxLabel.place(x = 10, y = 290)
        self.txLabel = Label(self.master, text="TX", fg=DARK_GRAY, bg=BLACK, font=("Ariel", 16))
        self.txLabel.place(x = 50, y = 290)

    def showTxOn(self, events=None):
        self.rxLabel = Label(self.master, text="RX", fg=DARK_GRAY, bg=BLACK, font=("Ariel", 16))
        self.rxLabel.place(x = 10, y = 290)
        self.txLabel = Label(self.master, text="TX", fg=RED, bg=BLACK, font=("Ariel", 16))
        self.txLabel.place(x = 50, y = 290)

    def promptExit(self, events=None):
        result = messagebox.askquestion("Shutdown", "Are you sure you want to shutdown?", icon='warning')
        if result == 'yes':
            os.system("shutdown now -h")

    def quit(self, events):
        self.master.destroy()

ui = UI()