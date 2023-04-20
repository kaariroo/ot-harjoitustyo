import os

class Note:
    def __init__(self, hexa):
        self.hexa = hexa
    def write(self, hex_number):
        dirname = os.path.dirname(__file__)
        print(dirname)
        notes_file_path = os.path.join(dirname, "hex_notes", f"{hex_number}.txt")
        print(notes_file_path)
        if not os.path.isfile(notes_file_path):
            with open(notes_file_path, "w") as document:
                document.write("Notes about hex.")
        os.system(f"gedit {notes_file_path}")
           