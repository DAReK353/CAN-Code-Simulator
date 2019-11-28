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
    textboxenginemodule.delete('1.0', END)
    textboxcomfortmodule.delete('1.0', END)
    textboxabsmodule.delete('1.0', END)
    textboxhvacmodule.delete('1.0', END)
    textboxwheelmodule.delete('1.0', END)
    textboxnavmodule.delete('1.0', END)
    textboxradiomodule.delete('1.0', END)
    textboxlockmodule.delete('1.0', END)
    textboxenginefunc.delete('1.0', END)
    textboxcomfortfunc.delete('1.0', END)
    textboxabsfunc.delete('1.0', END)
    textboxhvacfunc.delete('1.0', END)
    textboxwheelfunc.delete('1.0', END)
    textboxnavfunc.delete('1.0', END)
    textboxradiofunc.delete('1.0', END)
    textboxlockfunc.delete('1.0', END)
    textboxenginevalue.delete('1.0', END)
    textboxcomfortvalue.delete('1.0', END)
    textboxabsvalue.delete('1.0', END)
    textboxhvacvalue.delete('1.0', END)
    textboxwheelvalue.delete('1.0', END)
    textboxnavvalue.delete('1.0', END)
    textboxradiovalue.delete('1.0', END)
    textboxlockvalue.delete('1.0', END)


def resetlog():
    global ilosckodow
    textboxlogi.delete('1.0', END)
    ilosckodow = 0
    textboxilosckodow.delete('1.0', END)


def insertengine(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxenginemodule.see("end")
        textboxenginemodule.insert(END, canmodule + " OK" + "\n")
        textboxenginefunc.see("end")
        textboxenginefunc.insert(END, canfunc + "\n")
        textboxenginevalue.see("end")
        textboxenginevalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxenginemodule.see("end")
        textboxenginemodule.insert(END, canmodule + " Error" + "\n")


def insertcomfort(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxcomfortmodule.see("end")
        textboxcomfortmodule.insert(END, canmodule + " OK" + "\n")
        textboxcomfortfunc.see("end")
        textboxcomfortfunc.insert(END, canfunc + "\n")
        textboxcomfortvalue.see("end")
        textboxcomfortvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxcomfortmodule.see("end")
        textboxcomfortmodule.insert(END, canmodule + " Error" + "\n")


def insertabs(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxabsmodule.see("end")
        textboxabsmodule.insert(END, canmodule + " OK" + "\n")
        textboxabsfunc.see("end")
        textboxabsfunc.insert(END, canfunc + "\n")
        textboxabsvalue.see("end")
        textboxabsvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxabsmodule.see("end")
        textboxabsmodule.insert(END, canmodule + " Error" + "\n")


def inserthvac(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxhvacmodule.see("end")
        textboxhvacmodule.insert(END, canmodule + " OK" + "\n")
        textboxhvacfunc.see("end")
        textboxhvacfunc.insert(END, canfunc + "\n")
        textboxhvacvalue.see("end")
        textboxhvacvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxhvacmodule.see("end")
        textboxhvacmodule.insert(END, canmodule + " Error" + "\n")


def insertwheel(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxwheelmodule.see("end")
        textboxwheelmodule.insert(END, canmodule + " OK" + "\n")
        textboxwheelfunc.see("end")
        textboxwheelfunc.insert(END, canfunc + "\n")
        textboxwheelvalue.see("end")
        textboxwheelvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxnavmodule.see("end")
        textboxnavmodule.insert(END, canmodule + " Error" + "\n")


def insertnav(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxnavmodule.see("end")
        textboxnavmodule.insert(END, canmodule + " OK" + "\n")
        textboxnavfunc.see("end")
        textboxnavfunc.insert(END, canfunc + "\n")
        textboxnavvalue.see("end")
        textboxnavvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxnavmodule.see("end")
        textboxnavmodule.insert(END, canmodule + " Error" + "\n")


def insertradio(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlogi.see("end")
        textboxlogi.insert(END, "CAN code received:" + canmodule + canfunc + canvalue + "\n")
        textboxradiomodule.see("end")
        textboxradiomodule.insert(END, canmodule + " OK" + "\n")
        textboxradiofunc.see("end")
        textboxradiofunc.insert(END, canfunc + "\n")
        textboxradiovalue.see("end")
        textboxradiovalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxradiomodule.see("end")
        textboxradiomodule.insert(END, canmodule + " Error" + "\n")


def insertlock(canmodule, canfunc, canvalue):
    if len(canmodule) + len(canfunc) + len(canvalue) == 11:
        textboxlockmodule.see("end")
        textboxlockmodule.insert(END, canmodule + " OK" + "\n")
        textboxlockfunc.see("end")
        textboxlockfunc.insert(END, canfunc + "\n")
        textboxlockvalue.see("end")
        textboxlockvalue.insert(END, canvalue + "\n")
    else:
        textboxlogi.see("end")
        textboxlogi.insert(END, "Wrong CAN code format:" + canmodule + canfunc + canvalue + "\n")
        textboxlockmodule.see("end")
        textboxlockmodule.insert(END, canmodule + " Error" + "\n")


def symulowaniekodow():
    global startstop
    global ilosckodow
    while True:
        while startstop == 1:
            kod = readCANNetwork()
            canmodule = kod[0:2]
            canfunc = kod[2:5]
            canvalue = kod[5:]
            ilosckodow += 1
            textboxilosckodow.see("end")
            textboxilosckodow.insert(END, "\n"+str(ilosckodow))
            strcanmodule = str(canmodule)
            if strcanmodule == '01':
                threngine = threading.Thread(target=insertengine, daemon=False, args=(canmodule, canfunc, canvalue))
                threngine.start()
            elif strcanmodule == '46':
                thrcomfort = threading.Thread(target=insertcomfort, daemon=False, args=(canmodule, canfunc, canvalue))
                thrcomfort.start()
            elif strcanmodule == '03':
                thrabs = threading.Thread(target=insertabs, daemon=False, args=(canmodule, canfunc, canvalue))
                thrabs.start()
            elif strcanmodule == '08':
                thrhvac = threading.Thread(target=inserthvac, daemon=False, args=(canmodule, canfunc, canvalue))
                thrhvac.start()
            elif strcanmodule == '16':
                thrwheel = threading.Thread(target=insertwheel, daemon=False, args=(canmodule, canfunc, canvalue))
                thrwheel.start()
            elif strcanmodule == '37':
                thrnav = threading.Thread(target=insertnav, daemon=False, args=(canmodule, canfunc, canvalue))
                thrnav.start()
            elif strcanmodule == '56':
                thrradio = threading.Thread(target=insertradio, daemon=False, args=(canmodule, canfunc, canvalue))
                thrradio.start()
            elif strcanmodule == '35':
                thrlock = threading.Thread(target=insertlock, daemon=False, args=(canmodule, canfunc, canvalue))
                thrlock.start()
            else:
                textboxlogi.see("end")
                textboxlogi.insert(END, "Unknown CAN code received::" + kod + "\n")
            print(canmodule, canfunc, canvalue)
            time.sleep(float(szybkosc.get()))


sprawdzanie = threading.Thread(target=symulowaniekodow, daemon=True)
sprawdzanie.start()

root = Tk()
root.title('CAN Code Inspector')

infologi = Label(root, text="Logs")
infologi.grid(row=1, column=1)
textboxlogi = Text(root, height=20, width=50)
textboxlogi.grid(row=2, column=1, rowspan=10)
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

textboxenginemodule = Text(root, height=1, width=13)
textboxenginemodule.grid(row=2, column=2)
textboxcomfortmodule = Text(root, height=1, width=13)
textboxcomfortmodule.grid(row=2, column=3)
textboxabsmodule = Text(root, height=1, width=13)
textboxabsmodule.grid(row=2, column=4)
textboxhvacmodule = Text(root, height=1, width=13)
textboxhvacmodule.grid(row=2, column=5)
textboxwheelmodule = Text(root, height=1, width=13)
textboxwheelmodule.grid(row=2, column=6)
textboxnavmodule = Text(root, height=1, width=13)
textboxnavmodule.grid(row=2, column=7)
textboxradiomodule = Text(root, height=1, width=13)
textboxradiomodule.grid(row=2, column=8)
textboxlockmodule = Text(root, height=1, width=13)
textboxlockmodule.grid(row=2, column=9)

infofunct = Label(root, text="Parameter")
infofunct.grid(row=3, column=2, columnspan=9)
textboxenginefunc = Text(root, height=1, width=13)
textboxenginefunc.grid(row=4, column=2)
textboxcomfortfunc = Text(root, height=1, width=13)
textboxcomfortfunc.grid(row=4, column=3)
textboxabsfunc = Text(root, height=1, width=13)
textboxabsfunc.grid(row=4, column=4)
textboxhvacfunc = Text(root, height=1, width=13)
textboxhvacfunc.grid(row=4, column=5)
textboxwheelfunc = Text(root, height=1, width=13)
textboxwheelfunc.grid(row=4, column=6)
textboxnavfunc = Text(root, height=1, width=13)
textboxnavfunc.grid(row=4, column=7)
textboxradiofunc = Text(root, height=1, width=13)
textboxradiofunc.grid(row=4, column=8)
textboxlockfunc = Text(root, height=1, width=13)
textboxlockfunc.grid(row=4, column=9)

infovalue = Label(root, text="Value")
infovalue.grid(row=5, column=2, columnspan=9)
infovalue = Label(root, text="Value")
infovalue.grid(row=5, column=2, columnspan=9)
textboxenginevalue = Text(root, height=1, width=13)
textboxenginevalue.grid(row=6, column=2)
textboxcomfortvalue = Text(root, height=1, width=13)
textboxcomfortvalue.grid(row=6, column=3)
textboxabsvalue = Text(root, height=1, width=13)
textboxabsvalue.grid(row=6, column=4)
textboxhvacvalue = Text(root, height=1, width=13)
textboxhvacvalue.grid(row=6, column=5)
textboxwheelvalue = Text(root, height=1, width=13)
textboxwheelvalue.grid(row=6, column=6)
textboxnavvalue = Text(root, height=1, width=13)
textboxnavvalue.grid(row=6, column=7)
textboxradiovalue = Text(root, height=1, width=13)
textboxradiovalue.grid(row=6, column=8)
textboxlockvalue = Text(root, height=1, width=13)
textboxlockvalue.grid(row=6, column=9)

infoszybkosc = Label(root, text="CAN reading speed:")
infoszybkosc.grid(row=20, column=2)
szybkosc = Spinbox(root, format="%.2f", increment=0.1, from_=0.0, to=0.5, width=4)
szybkosc.grid(row=20, column=3, sticky="news")
przycisk1 = Button(root, text='Reset results', command=resetwyniki)
przycisk1.grid(row=20, column=5, sticky="news")
przycisk1 = Button(root, text='Reset logs', command=resetlog)
przycisk1.grid(row=20, column=6, sticky="news")
przycisk2 = Button(root, text='Start', command=start)
przycisk2.grid(row=20, column=7, sticky="news")
przycisk3 = Button(root, text='Stop', command=stop)
przycisk3.grid(row=20, column=8, sticky="news")
przycisk4 = Button(root, text='Exit', command=exit)
przycisk4.grid(row=20, column=9, sticky="news")

root.mainloop()
