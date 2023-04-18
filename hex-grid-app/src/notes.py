import os

class Note:
    def __init__(self, hexa):
        self.hexa = hexa
    def write(self, hex_number):
        if not os.path.isfile(f"{hex_number}.txt"):
            with open(f"{hex_number}.txt", "w") as document:
                document.write("Notes about hex.")
        os.system(f"gedit {hex_number}.txt")
           