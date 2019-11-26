import threading
import CanNetworkSimulator
import time
from tkinter import *

startstop = 0


def start():
    global startstop
    if startstop == 0:
        startstop = 1
        textboxlogi.insert(END, "Rozpoczęto symulowanie kodów CAN.\n")


def stop():
    global startstop
    if startstop == 1:
        startstop = 0
        textboxlogi.insert(END, "Zatrzymano symulowanie kodów CAN.\n")


def symulowaniekodow():
    global startstop
    while True:
        while startstop == 1:
            kod = CanNetworkSimulator.readCANNetwork()
            if len(kod) == 11:
                canmodule = kod[0:2]
                canfunc = kod[2:5]
                canvalue = kod[5:10]
                textboxlogi.insert(END, "Otrzymano kod:" + canmodule + canfunc + canvalue + "\n")
                time.sleep(0.3)
                print(canmodule, canfunc, canvalue)
            else:
                textboxlogi.insert(END, "Otrzymano nieprawidłowy kod CAN:" + kod + "\n")
                time.sleep(0.3)


sprawdzanie = threading.Thread(target=symulowaniekodow, daemon=True)
sprawdzanie.start()

root = Tk()

infologi = Label(root, text="Logi programu")
infologi.grid(row=1, column=1)
textboxlogi = Text(root, height=20, width=50)
textboxlogi.grid(row=2, column=1)

infoengine = Label(root, text="ECM")
infoengine.grid(row=1, column=2)
infocomfort = Label(root, text="Comfort Module")
infocomfort.grid(row=1, column=3)
infoabs = Label(root, text="ABS")
infoabs.grid(row=1, column=4)
infohvac = Label(root, text="Air Conditioning")
infohvac.grid(row=1, column=5)
infowheel = Label(root, text="Steering Column")
infowheel.grid(row=1, column=6)
infonav = Label(root, text="Navigation")
infonav.grid(row=1, column=7)
inforadio = Label(root, text="Radio")
inforadio.grid(row=1, column=8)
infolock = Label(root, text="Central Lock")
infolock.grid(row=1, column=9)
textboxengine = Text(root, height=2, width=12)
textboxengine.grid(row=2, column=2)
textboxcomfort = Text(root, height=2, width=12)
textboxcomfort.grid(row=2, column=3)
textboxabs = Text(root, height=2, width=12)
textboxabs.grid(row=2, column=4)
textboxhvac = Text(root, height=2, width=12)
textboxhvac.grid(row=2, column=5)
textboxwheel = Text(root, height=2, width=12)
textboxwheel.grid(row=2, column=6)
textboxnav = Text(root, height=2, width=12)
textboxnav.grid(row=2, column=7)
textboxradio = Text(root, height=2, width=12)
textboxradio.grid(row=2, column=8)
textboxlock = Text(root, height=2, width=12)
textboxlock.grid(row=2, column=9)

przycisk1 = Button(root, text='Rozpocznij symulację', command=start)
przycisk1.grid(row=13, column=10)
przycisk2 = Button(root, text='Zatrzymaj symulację', command=stop)
przycisk2.grid(row=13, column=11)
przycisk2 = Button(root, text='Wyjdź', command=exit)
przycisk2.grid(row=13, column=12)

root.mainloop()
