class RemoveSq3:
    def __init__(self, place3_1, place3_3, seq):
        self.place3_1 = place3_1
        self.place3_3 = place3_3
        self.seq = seq

    @property
    def remover3(self):
        if self.place3_1 - self.place3_3 == 2:
            try:
                self.seq.remove(self.place3_1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 7)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 3)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 12)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 13)
            except KeyError:
                pass
        elif self.place3_3 - self.place3_1 == 2:
            try:
                self.seq.remove(self.place3_3 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 7)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 3)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 12)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 13)
            except KeyError:
                pass
        elif self.place3_1 - self.place3_3 == 20:
            try:
                self.seq.remove(self.place3_1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 21)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 29)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 30)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_1 - 31)
            except KeyError:
                pass
        elif self.place3_3 - self.place3_1 == 20:
            try:
                self.seq.remove(self.place3_3 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 21)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 29)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 30)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place3_3 - 31)
            except KeyError:
                pass
        return self.seq