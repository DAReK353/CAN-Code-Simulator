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
        textboxlogi.insert(END, "Analysis of CAN codes started.\n")


def stop():
    global startstop
    if startstop == 1:
        startstop = 0
        textboxlogi.insert(END, "Analysis of CAN codes stopped.\n")


def resetwyniki():
    global ilosckodow
    ilosckodow = 0
    textboxilosckodow.delete('1.0', END)


def resetlog():
    textboxlogi.delete('1.0', END)


def insertengine(canmodule, canfunc, canvalue):
    textboxenginemodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxenginemodule.see("end")


def insertcomfort(canmodule, canfunc, canvalue):
    textboxcomfortmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxcomfortmodule.see("end")


def insertabs(canmodule, canfunc, canvalue):
    textboxabsmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxabsmodule.see("end")


def inserthvac(canmodule, canfunc, canvalue):
    textboxhvacmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxhvacmodule.see("end")


def insertwheel(canmodule, canfunc, canvalue):
    textboxwheelmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxwheelmodule.see("end")


def insertnav(canmodule, canfunc, canvalue):
    textboxnavmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxnavmodule.see("end")


def insertradio(canmodule, canfunc, canvalue):
    textboxradiomodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxradiomodule.see("end")


def insertlock(canmodule, canfunc, canvalue):
    textboxlockmodule.insert(END, "Code: " + canmodule + " OK" + "\n")
    textboxlockmodule.see("end")


def symulowaniekodow():
    global startstop
    global ilosckodow
    while True:
        while startstop == 1:
            kod = readCANNetwork()
            canmodule = kod[0:2]
            canfunc = kod[2:5]
            canvalue = kod[5:]
            if len(kod) == 11:
                textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
                textboxlogi.see("end")
                ilosckodow += 1
                textboxilosckodow.insert(END, "\n"+str(ilosckodow))
                textboxilosckodow.see("end")
                strcanmodule = str(canmodule)
                print(canmodule, canfunc, canvalue)
                if strcanmodule == '01':
                    insertengine(canmodule, canfunc, canvalue)
                elif strcanmodule == '46':
                    insertcomfort(canmodule, canfunc, canvalue)
                elif strcanmodule == '03':
                    insertabs(canmodule, canfunc, canvalue)
                elif strcanmodule == '08':
                    inserthvac(canmodule, canfunc, canvalue)
                elif strcanmodule == '16':
                    insertwheel(canmodule, canfunc, canvalue)
                elif strcanmodule == '37':
                    insertnav(canmodule, canfunc, canvalue)
                elif strcanmodule == '56':
                    insertradio(canmodule, canfunc, canvalue)
                elif strcanmodule == '35':
                    insertlock(canmodule, canfunc, canvalue)
                else:
                    textboxlogi.insert(END, "Unknown CAN code received::" + kod + "\n")
                    textboxlogi.see("end")
                time.sleep(0.3)
            else:
                textboxlogi.insert(END, "Wrong CAN code received::" + kod + "\n")
                textboxlogi.see("end")
                print(canmodule, canfunc, canvalue)
                time.sleep(0.3)


sprawdzanie = threading.Thread(target=symulowaniekodow, daemon=True)
sprawdzanie.start()

root = Tk()
root.title('CAN Code Inspector')

infologi = Label(root, text="Program logs")
infologi.grid(row=1, column=1)
textboxlogi = Text(root, height=20, width=50)
textboxlogi.grid(row=2, column=1)
infoilosckodow = Label(root, text="Number of CAN codes received:")
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
textboxenginemodule = Text(root, height=2, width=12)
textboxenginemodule.grid(row=2, column=2)
textboxcomfortmodule = Text(root, height=2, width=12)
textboxcomfortmodule.grid(row=2, column=3)
textboxabsmodule = Text(root, height=2, width=12)
textboxabsmodule.grid(row=2, column=4)
textboxhvacmodule = Text(root, height=2, width=12)
textboxhvacmodule.grid(row=2, column=5)
textboxwheelmodule = Text(root, height=2, width=12)
textboxwheelmodule.grid(row=2, column=6)
textboxnavmodule = Text(root, height=2, width=12)
textboxnavmodule.grid(row=2, column=7)
textboxradiomodule = Text(root, height=2, width=12)
textboxradiomodule.grid(row=2, column=8)
textboxlockmodule = Text(root, height=2, width=12)
textboxlockmodule.grid(row=2, column=9)

przycisk1 = Button(root, text='Reset results', command=resetwyniki)
przycisk1.grid(row=20, column=2)
przycisk1 = Button(root, text='Reset logs', command=resetlog)
przycisk1.grid(row=20, column=3)
przycisk2 = Button(root, text='Start', command=start)
przycisk2.grid(row=20, column=4)
przycisk3 = Button(root, text='Stop', command=stop)
przycisk3.grid(row=20, column=5)
przycisk4 = Button(root, text='Exit', command=exit)
przycisk4.grid(row=20, column=9)

root.mainloop()
