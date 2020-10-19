class RemoveSq1:   # удаляет числа из множества доступных клеток, куда можно поставить корабль
    def __init__(self, place1, seq):
        self.place1 = place1
        self.seq = seq
    @property
    def remover1(self):
        if self.place1 % 10 != 0 and self.place1 % 10 != 9:
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
                self.seq.remove(self.place1 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 11)
            except KeyError:
                pass
        elif self.place1 % 10 == 0:
            try:
                self.seq.remove(self.place1 + 1)
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
                self.seq.remove(self.place1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 - 10)
            except KeyError:
                pass
        elif self.place1 % 10 == 9:
            try:
                self.seq.remove(self.place1 - 1)
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
                self.seq.remove(self.place1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place1 + 10)
            except KeyError:
                pass

        return self.seq
