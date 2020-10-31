class Desk:

    def __init__(self, L, L1, Q, Q2):
        self.L = L
        self.L1 = L1
        self.Q = Q
        self.Q2 = Q2

    def paint_desk(self):
        self.L1 = [f'|{self.L[i]}' for i in range(100)]  # Доска игрока видимая
        self.Q2 = [f'|{self.Q[i]}' for i in range(100)]  # Доска ИИ видимая
        for w in range(10):
            self.Q2[w * 10 - 1] = f'|{self.Q[w * 10 - 1]}|'
            self.L1[w * 10 - 1] = f'|{self.L[w * 10 - 1]}|'
        print(' |0|1|2|3|4|5|6|7|8|9|', end='')
        print('        |0|1|2|3|4|5|6|7|8|9|')
        for q in range(10):
            print(q, end='')
            for e1 in range(10):
                print(self.Q2[e1 + q * 10], end="")
            print('       ', end='')
            print(q, end='')
            for e2 in range(10):
                print(self.L1[e2 + q * 10], end="")
            print()
        return


