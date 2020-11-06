class MarkT:  # маркерует поля вокруг подбитого корабля символом Т
    def __init__(self, seqVis, subseq):
        self.seqVis = seqVis
        self.subseq = subseq
    @property
    def marker(self):
        for i in self.subseq:
            if i % 10 != 0 and i % 10 != 9:
                self.exception(i, 1)
                self.exception(i, 9)
                self.exception(i, 10)
                self.exception(i, 11)
                self.exception(i, -1)
                if i // 10 != 0:
                    self.exception(i, -9)
                    self.exception(i, -10)
                    self.exception(i, -11)
            elif i % 10 == 0:
                self.exception(i, 1)
                self.exception(i, 10)
                self.exception(i, 11)
                if i // 10 != 0:
                    self.exception(i, -9)
                    self.exception(i, -10)
            elif i % 10 == 9:
                self.exception(i, -1)
                if i // 10 != 0:
                    self.exception(i, -10)
                    self.exception(i, -11)
                self.exception(i, 9)
                self.exception(i, 10)
        return self.seqVis

    def exception(self, i, n):
        try:
            if self.seqVis[i + n] != 'X':
                self.seqVis[i + n] = 'T'
        except IndexError:
            pass
        return self.seqVis
