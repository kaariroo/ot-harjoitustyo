import os

class Note:

    """Hexojen tietojen kirjoittamisesta vastaava luokka"""

    def __init__(self, hexa):

        """Luokan konstruktori
        Args:
        hexa = kuusikulmio, johon muistiinpanot liittyvät"""

        self.hexa = hexa
    def write(self, hex_number):

        """Muistiinpanojen kirjoittamisesta vastaava metodi. Luo tarvittaessa 
        tekstitiedoston ja avaa editorin"""

        dirname = os.path.dirname(__file__)
        notes_file_path = os.path.join(dirname, "hex_notes", f"{hex_number}.txt")
        if not os.path.isfile(notes_file_path):
            with open(notes_file_path, "w") as document:
                document.write("Notes about hex.")
        os.system(f"gedit {notes_file_path}")
        