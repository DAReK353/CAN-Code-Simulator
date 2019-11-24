import CanNetworkSimulator
import time

#for i in range(0, 50):
#    print(CanNetworkSimulator.readCANNetwork())

while True:
    print(CanNetworkSimulator.readCANNetwork())
    time.sleep(0.3)