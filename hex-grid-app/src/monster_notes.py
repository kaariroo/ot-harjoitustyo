import os

class MonsterNote:

    """Hexoissa olevien monstereiden tiedon tallentamisesta vastaava luokka"""

    def __init__(self, hexa, monster):

        """Luokan konstruktori, joka luo uuden muistiinpanon
        Args:
        hexa = muistiinpanoon liittyvän kuusikulmion numero
        monster = muistiinpanoon lisättävä monsteri"""

        self.hexa = hexa
        self.monster = monster

    def write(self, hex_number):

        """Vastaa csv tiedoston kirjoittamisesta."""

        dirname = os.path.dirname(__file__)
        notes_file_path = os.path.join(dirname, "monster_notes", f"{hex_number}.csv")
        if not os.path.isfile(notes_file_path):
            with open(notes_file_path, "w") as document:
                document.write(f"{self.monster};")
        else:
            with open(notes_file_path, "a") as document:
                document.write(f"{self.monster};")
    