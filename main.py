import threading
import time
from CanNetworkSimulator import readCANNetwork
from tkinter import *

startstop = 0
ilosckodow = 0


def start():
    global startstop
    if startstop == 0:
        startstop = 1
        textboxlogi.insert(END, "\nRozpoczęto symulowanie kodów CAN.\n")


def stop():
    global startstop
    if startstop == 1:
        startstop = 0
        textboxlogi.insert(END, "Zatrzymano symulowanie kodów CAN.\n")


def resetwyniki():
    global ilosckodow
    ilosckodow = 0
    textboxilosckodow.delete('1.0', END)


def resetlog():
    textboxlogi.delete('1.0', END)


def symulowaniekodow():
    global startstop
    global ilosckodow
    while True:
        while startstop == 1:
            kod = readCANNetwork()
            if len(kod) == 11:
                canmodule = kod[0:2]
                canfunc = kod[2:5]
                canvalue = kod[5:10]
                textboxlogi.insert(END, "Otrzymano kod:" + canmodule + canfunc + canvalue + "\n")
                textboxlogi.see("end")
                ilosckodow += 1
                textboxilosckodow.insert(END, "\n"+str(ilosckodow))
                textboxilosckodow.see("end")
                print(canmodule, canfunc, canvalue)
                time.sleep(0.3)
            else:
                textboxlogi.insert(END, "Otrzymano nieprawidłowy kod CAN:" + kod + "\n")
                textboxlock.see("end")
                time.sleep(0.3)


sprawdzanie = threading.Thread(target=symulowaniekodow, daemon=True)
sprawdzanie.start()

root = Tk()
root.title('Odczytywanie kodów CAN')

infologi = Label(root, text="Logi programu")
infologi.grid(row=1, column=1)
textboxlogi = Text(root, height=20, width=50)
textboxlogi.grid(row=2, column=1)
infoilosckodow = Label(root, text="Ilość otrzymanych kodów CAN:")
infoilosckodow.grid(row=20, column=1)
textboxilosckodow = Text(root, height=1, width=5)
textboxilosckodow.grid(row=20, column=1, columnspan=4)

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

przycisk1 = Button(root, text='Resetuj wyniki', command=resetwyniki)
przycisk1.grid(row=20, column=2, columnspan=1)
przycisk1 = Button(root, text='Resetuj logi', command=resetlog)
przycisk1.grid(row=20, column=2, columnspan=4)
przycisk2 = Button(root, text='Rozpocznij symulację', command=start)
przycisk2.grid(row=20, column=2, columnspan=6)
przycisk3 = Button(root, text='Zatrzymaj symulację', command=stop)
przycisk3.grid(row=20, column=2, columnspan=9)
przycisk4 = Button(root, text='Wyjdź', command=exit)
przycisk4.grid(row=20, column=9)

root.mainloop()
