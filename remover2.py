class RemoveSq2:
    def __init__(self, place1, place2,seq):
        self.place1 = place1
        self.place2 = place2
        self.seq = seq
    @property
    def remover(self):
        if self.place1 - self.place2 == 1:
            try:
                self.seq.remove(self.place1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 2)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 12)
            except KeyError:
                pass
        elif self.place2 - self.place1 == 1:
            try:
                self.seq.remove(self.place2 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 2)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 12)
            except KeyError:
                pass
        elif self.place1 - self.place2 == 10:
            try:
                self.seq.remove(self.place1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 20)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 21)
            except KeyError:
                pass
        elif self.place2 - self.place1 == 10:
            try:
                self.seq.remove(self.place2 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 20)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place2 - 21)
            except KeyError:
                pass
        return self.seq


