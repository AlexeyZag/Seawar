class MarkT:  # маркерует поля вокруг подбитого корабля символом Т
    def __init__(self, seqVis, subseq):
        self.seqVis = seqVis
        self.subseq = subseq
    @property
    def marker(self):
        for i in self.subseq:
            if i % 10 != 0 and i % 10 != 9:
                try:
                    if self.seqVis[i + 1] != 'X':
                        self.seqVis[i + 1] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 9] != 'X':
                        self.seqVis[i + 9] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 10] != 'X':
                        self.seqVis[i + 10] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 11] != 'X':
                        self.seqVis[i + 11] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i - 1] != 'X':
                        self.seqVis[i - 1] = 'T'
                except IndexError:
                    pass
                if i // 10 != 0:
                    try:
                        if self.seqVis[i - 9] != 'X':
                            self.seqVis[i - 9] = 'T'
                    except IndexError:
                        pass
                    try:
                        if self.seqVis[i - 10] != 'X':
                            self.seqVis[i - 10] = 'T'
                    except IndexError:
                        pass
                    try:
                        if self.seqVis[i - 11] != 'X':
                            self.seqVis[i - 11] = 'T'
                    except IndexError:
                        pass
            elif i % 10 == 0:
                try:
                    if self.seqVis[i + 1] != 'X':
                        self.seqVis[i + 1] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 10] != 'X':
                        self.seqVis[i + 10] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 11] != 'X':
                        self.seqVis[i + 11] = 'T'
                except IndexError:
                    pass
                if i // 10 != 0:
                    try:
                        if self.seqVis[i - 9] != 'X':
                            self.seqVis[i - 9] = 'T'
                    except IndexError:
                        pass
                    try:
                        if self.seqVis[i - 10] != 'X':
                            self.seqVis[i - 10] = 'T'
                    except IndexError:
                        pass
            elif i % 10 == 9:
                try:
                    if self.seqVis[i - 1] != 'X':
                        self.seqVis[i - 1] = 'T'
                except IndexError:
                    pass
                if i // 10 != 0:
                    try:
                        if self.seqVis[i - 10] != 'X':
                            self.seqVis[i - 10] = 'T'
                    except IndexError:
                        pass
                    try:
                        if self.seqVis[i - 11] != 'X':
                            self.seqVis[i - 11] = 'T'
                    except IndexError:
                        pass
                try:
                    if self.seqVis[i + 9] != 'X':
                        self.seqVis[i + 9] = 'T'
                except IndexError:
                    pass
                try:
                    if self.seqVis[i + 10] != 'X':
                        self.seqVis[i + 10] = 'T'
                except IndexError:
                    pass
        return self.seqVis
