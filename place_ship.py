# устанавливает все корабли
import random
from remove_around import RemoveSq1

class Ship:
    def __init__(self, s, allow, listBoard, ship):
        self.allow = allow
        self.listBoard = listBoard
        self.ship = ship
        self.s = s

    def place(self):
        place1_1 = random.choice(list(self.allow))
        if self.s == 1:
            self.listBoard[place1_1] = 'S'
            self.ship.append({place1_1})
            self.allow.remove(place1_1)
            self.allow_list_Pl4_1 = RemoveSq1(place1_1, self.allow)
            self.allow.intersection_update(self.allow_list_Pl4_1.remover1)
            return

        allow_ways = [[], [], [], []]
        i = 1
        while i < self.s:
            if {place1_1 + i * 10} <= self.allow:
                allow_ways[0].append(place1_1 + i * 10)
                i += 1
            else:
                allow_ways[0] = []
                break

        i = 1
        while i < self.s:
            if {place1_1 - i * 10} <= self.allow:
                allow_ways[1].append(place1_1 - i * 10)
                i += 1
            else:
                allow_ways[1] = []
                break

        if self.s - 1 <= place1_1 % 10 <= 10 - self.s:
            i = 1
            while i < self.s:
                if {place1_1 + i} <= self.allow:
                    allow_ways[2].append(place1_1 + i)
                    i += 1
                else:
                    allow_ways[2] = []
                    break
            i = 1
            while i < self.s:
                if {place1_1 - i} <= self.allow:
                    allow_ways[3].append(place1_1 - i)
                    i += 1
                else:
                    allow_ways[3] = []
                    break
        elif self.s - 1 > place1_1 % 10:
            i = 1
            while i < self.s:
                if {place1_1 + i} <= self.allow:
                    allow_ways[2].append(place1_1 + i)
                    i += 1
                else:
                    allow_ways[2] = []
                    break
        elif 10 - self.s < place1_1 % 10:
            i = 1
            while i < self.s:
                if {place1_1 - i} <= self.allow:
                    allow_ways[3].append(place1_1 - i)
                    i += 1
                else:
                    allow_ways[3] = []
                    break
        allow_ways1 = []
        for p in allow_ways:
            if len(p) != 0:
                allow_ways1.append(p)
        if len(allow_ways1) == 0 and self.s:
            return self.place()
        else:
            way = random.choice(allow_ways1)
            self.listBoard[place1_1] = 'S'
            seter = {place1_1}
            self.allow.remove(place1_1)
            self.allow_list_Pl4_1 = RemoveSq1(place1_1, self.allow)
            self.allow.intersection_update(self.allow_list_Pl4_1.remover1)
            for o in way:
                self.listBoard[o] = 'S'
                seter.add(o)
                self.allow_list_Pl4_1 = RemoveSq1(o, self.allow)
                self.allow.intersection_update(self.allow_list_Pl4_1.remover1)
            self.ship.append(seter)
