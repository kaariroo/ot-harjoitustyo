from tkinter import Tk, ttk, constants
class UI:
    def __init__(self, root):
        self._root = root

    def start(self):
        label = ttk.Label(master=self._root, text="Get started creating some epic fantasy adventures!")
        newmap = ttk.Button(master=self._root, text="New map")
        loadmap = ttk.Button(master=self._root, text="Load map")
        

        label.grid(row=0, column=0, columnspan=10, sticky=(constants.E, constants.W, constants.N, constants.S), padx=10, pady=10)
        newmap.grid(row=1, column=0, sticky=(constants.E, constants.W, constants.N, constants.S), padx=10, pady=10)
        loadmap.grid(row=1, column=1, sticky=(constants.E, constants.W, constants.N, constants.S), padx=10, pady=10)
        
        self._root.grid_rowconfigure(1, weight=1, minsize=150)
        self._root.grid_columnconfigure(0, weight=1, minsize=200)
        self._root.grid_columnconfigure(1, weight=1, minsize=200)

        
window = Tk()
window.title("Hex-grid map-app")

ui = UI(window)
ui.start()

window.mainloop()

