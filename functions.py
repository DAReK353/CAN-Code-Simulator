import CanNetworkSimulator
import time

startstop = 0


def start():
    global startstop
    if startstop == 0:
        startstop = 1
        print("Rozpoczęto symulowanie kodów CAN.")


def stop():
    global startstop
    if startstop == 1:
        startstop = 0
        print("Zatrzymano symulowanie kodów CAN.")


def wysylaniekodow():
    global startstop
    while True:
        while startstop == 1:
            print(CanNetworkSimulator.readCANNetwork())
            time.sleep(0.3)
