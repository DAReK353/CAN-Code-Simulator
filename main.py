import functions
import threading
from tkinter import *

watek = threading.Thread(target=functions.wysylaniekodow, daemon=True)
watek.start()

root = Tk()

przycisk1 = Button(root, text='Start', command=functions.start)
przycisk1.grid(row=10, column=1)
przycisk2 = Button(root, text='Stop', command=functions.stop)
przycisk2.grid(row=10, column=2)

root.mainloop()
