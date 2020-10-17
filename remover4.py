class RemoveSq4:
    def __init__(self, place4_1, place4_4, seq):
        self.place4_1 = place4_1
        self.place4_4 = place4_4
        self.seq = seq
    @property
    def remover4(self):
        if self.place4_1 - self.place4_4 == 3:
            try:
                self.seq.remove(self.place4_1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 6)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 7)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 4)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 12)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 13)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 14)
            except KeyError:
                pass
        elif self.place4_4 - self.place4_1 == 3:
            try:
                self.seq.remove(self.place4_4 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 6)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 7)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 8)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 4)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 12)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 13)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 14)
            except KeyError:
                pass
        elif self.place4_1 - self.place4_4 == 30:
            try:
                self.seq.remove(self.place4_1 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 21)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 29)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 31)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 39)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 40)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_1 - 41)
            except KeyError:
                pass
        elif self.place4_4 - self.place4_1 == 30:
            try:
                self.seq.remove(self.place4_4 + 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 10)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 + 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 1)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 9)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 11)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 19)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 21)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 29)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 31)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 39)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 40)
            except KeyError:
                pass
            try:
                self.seq.remove(self.place4_4 - 41)
            except KeyError:
                pass
        return self.seq
