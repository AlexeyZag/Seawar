class Desk:

    def __init__(self, L, Q):
        self.L = L
        self.Q = Q

    def paint_desk(self):
        L1 = [f'|{self.L[i1]}' for i1 in range(100)]  # Доска игрока видимая
        Q2 = [f'|{self.Q[k2]}' for k2 in range(100)]  # Доска ИИ видимая

        for w in range(10):
            Q2[w * 10 - 1] = f'|{self.Q[w * 10 - 1]}|'
            L1[w * 10 - 1] = f'|{self.L[w * 10 - 1]}|'
        print(' |0|1|2|3|4|5|6|7|8|9|', end='')
        print('        |0|1|2|3|4|5|6|7|8|9|')
        for q in range(10):
            print(q, end='')
            for e1 in range(10):
                print(Q2[e1 + q * 10], end="")
            print('       ', end='')
            print(q, end='')
            for e2 in range(10):
                print(L1[e2 + q * 10], end="")
            print()
        return


