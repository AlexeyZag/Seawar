class RemoveSq1:   # удаляет числа из множества доступных клеток, куда можно поставить корабль
    def __init__(self, place1, seq):
        self.place1 = place1
        self.seq = seq
    @property
    def remover1(self):
        if self.place1 % 10 != 0 and self.place1 % 10 != 9:
            self.exception(1)
            self.exception(9)
            self.exception(10)
            self.exception(11)
            self.exception(-1)
            self.exception(-9)
            self.exception(-10)
            self.exception(-11)
        elif self.place1 % 10 == 0:
            self.exception(1)
            self.exception(10)
            self.exception(11)
            self.exception(-9)
            self.exception(-10)
        elif self.place1 % 10 == 9:
            self.exception(-1)
            self.exception(-10)
            self.exception(-11)
            self.exception(9)
            self.exception(10)

        return self.seq

    def exception(self, n):
        try:
            self.seq.remove(self.place1 + n)
        except KeyError:
            pass
        return self.seq
