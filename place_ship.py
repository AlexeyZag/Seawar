# устанавливает все корабли
import random
from remove_around import RemoveSq1
class Ship:
    def __init__(self, allow, listBoard, ship):
        self.allow = allow
        self.listBoard = listBoard
        self.ship = ship

    def get_place4s(self):
        place4_2, place4_3, place4_4 = None, None, None
        place4_1 = random.choice(list(self.allow))  # выбираем пустую клетку
        allow_place4_2 = set()  # множество, показывающее направление 4палубника
        if {place4_1 - 30} <= self.allow:  # если сверху нет ограничений добавляем направление вверх
            allow_place4_2.add(place4_1 - 10)
        if {place4_1 + 30} <= self.allow:  # если снизу нет ограничений добавляем направление вниз
            allow_place4_2.add(place4_1 + 10)
        if place4_1 % 10 != 0 and place4_1 % 10 != 1 and place4_1 % 10 != 2 and place4_1 % 10 != 7 and place4_1 % 10 != 8 and place4_1 % 10 != 9:
            allow_place4_2.add(place4_1 + 1)  # влево и вправо нет ограничений, так как первое вхождение находится далеко от краев доски
            allow_place4_2.add(place4_1 - 1)
        elif place4_1 % 10 == 0 or place4_1 % 10 == 1 or place4_1 % 10 == 2:  # если первое вхождение близко к левому краю
            allow_place4_2.add(place4_1 + 1)
        elif place4_1 % 10 == 8 or place4_1 % 10 == 9 or place4_1 % 10 == 7:  # если первое вхождение близко к правому краю
            allow_place4_2.add(place4_1 - 1)
        if len(allow_place4_2) != 0:  # если allow_place4_2 не пустое, значит напрвление есть, можно продолжать
            place4_2 = random.choice(list(allow_place4_2))  # выбираем направление из allow_place4_2
            if place4_2 == place4_1 + 1:
                self.listBoard[place4_1], self.listBoard[place4_2], self.listBoard[place4_2 + 1], self.listBoard[place4_2 + 2] = 'S', 'S', 'S', 'S'
                place4_3 = place4_2 + 1
                place4_4 = place4_2 + 2
            elif place4_2 == place4_1 - 1:
                self.listBoard[place4_1], self.listBoard[place4_2], self.listBoard[place4_2 - 1], self.listBoard[
                    place4_2 - 2] = 'S', 'S', 'S', 'S'
                place4_3 = place4_2 - 1
                place4_4 = place4_2 - 2
            elif place4_2 == place4_1 - 10:
                self.listBoard[place4_1], self.listBoard[place4_2], self.listBoard[place4_2 - 10], self.listBoard[
                    place4_2 - 20] = 'S', 'S', 'S', 'S'
                place4_3 = place4_2 - 10
                place4_4 = place4_2 - 20
            elif place4_2 == place4_1 + 10:
                self.listBoard[place4_1], self.listBoard[place4_2], self.listBoard[place4_2 + 10], self.listBoard[
                    place4_2 + 20] = 'S', 'S', 'S', 'S'
                place4_3 = place4_2 + 10
                place4_4 = place4_2 + 20
            self.ship.append({place4_1, place4_2, place4_3, place4_4})
            self.allow.remove(place4_1)
            self.allow.remove(place4_2)
            self.allow.remove(place4_3)
            self.allow.remove(place4_4)
        else:
            self.get_place4s()
        allow_list_Pl4_1 = RemoveSq1(place4_1, self.allow)
        self.allow.intersection_update(allow_list_Pl4_1.remover1)  # убираем клетки из списка дозволенных вокруг каждой палубы, чтобы нельзя было в след раз ставить рядом другой корабль
        allow_list_Pl4_2 = RemoveSq1(place4_2, self.allow)
        self.allow.intersection_update(allow_list_Pl4_2.remover1)
        allow_list_Pl4_3 = RemoveSq1(place4_3, self.allow)
        self.allow.intersection_update(allow_list_Pl4_3.remover1)
        allow_list_Pl4_4 = RemoveSq1(place4_4, self.allow)
        self.allow.intersection_update(allow_list_Pl4_4.remover1)

    def get_place3s(self):
        place3_1, place3_2, place3_3 = None, None, None
        place3_1 = random.choice(list(self.allow))  # выбираем пустую клетку
        allow_place3_2 = set()
        if place3_1 % 10 != 0 and place3_1 % 10 != 1 and place3_1 % 10 != 8 and place3_1 % 10 != 9:
            if {place3_1 + 1, place3_1 + 2} <= self.allow:
                allow_place3_2.add(place3_1 + 1)
            if {place3_1 - 1, place3_1 - 2} <= self.allow:
                allow_place3_2.add(place3_1 - 1)
            if {place3_1 - 10, place3_1 - 20} <= self.allow:
                allow_place3_2.add(place3_1 - 10)
            if {place3_1 + 10, place3_1 + 20} <= self.allow:
                allow_place3_2.add(place3_1 + 10)
        elif place3_1 % 10 == 0 or place3_1 % 10 == 1:
            if {place3_1 + 1, place3_1 + 2} <= self.allow:
                allow_place3_2.add(place3_1 + 1)
            if {place3_1 - 10, place3_1 - 20} <= self.allow:
                allow_place3_2.add(place3_1 - 10)
            if {place3_1 + 10, place3_1 + 20} <= self.allow:
                allow_place3_2.add(place3_1 + 10)
        elif place3_1 % 10 == 8 or place3_1 % 10 == 9:
            if {place3_1 - 1, place3_1 - 2} <= self.allow:
                allow_place3_2.add(place3_1 - 1)
            if {place3_1 - 10, place3_1 - 20} <= self.allow:
                allow_place3_2.add(place3_1 - 10)
            if {place3_1 + 10, place3_1 + 20} <= self.allow:
                allow_place3_2.add(place3_1 + 10)
        if len(allow_place3_2) != 0:
            place3_2 = random.choice(list(allow_place3_2))
            if place3_2 == place3_1 + 1:
                self.listBoard[place3_1], self.listBoard[place3_2], self.listBoard[place3_2 + 1] = 'S', 'S', 'S'
                place3_3 = place3_2 + 1
            elif place3_2 == place3_1 - 1:
                self.listBoard[place3_1], self.listBoard[place3_2], self.listBoard[place3_2 - 1] = 'S', 'S', 'S'
                place3_3 = place3_2 - 1
            elif place3_2 == place3_1 - 10:
                self.listBoard[place3_1], self.listBoard[place3_2], self.listBoard[place3_2 - 10] = 'S', 'S', 'S'
                place3_3 = place3_2 - 10
            elif place3_2 == place3_1 + 10:
                self.listBoard[place3_1], self.listBoard[place3_2], self.listBoard[place3_2 + 10] = 'S', 'S', 'S'
                place3_3 = place3_2 + 10
            self.allow.remove(place3_1)
            self.allow.remove(place3_2)
            self.allow.remove(place3_3)
        else:
            self.get_place3s()
        self.ship.append({place3_1, place3_2, place3_3})
        allow_list_Pl3_1 = RemoveSq1(place3_1, self.allow)
        self.allow.intersection_update(allow_list_Pl3_1.remover1)
        allow_list_Pl3_2 = RemoveSq1(place3_2, self.allow)
        self.allow.intersection_update(allow_list_Pl3_2.remover1)
        allow_list_Pl3_3 = RemoveSq1(place3_3, self.allow)
        self.allow.intersection_update(allow_list_Pl3_3.remover1)

    def get_place2s(self):
        place1, place2 = None, None
        place1 = random.choice(list(self.allow))  # выбираем пустую клетку
        allow_place_2 = None  #  allow_place_2 - список клеток, куда можно будет поставить вторую палубу
        if place1 % 10 != 9 and place1 % 10 != 0:  # если номер столбца не равен 0 или 9, делается для того, чтобы корабль не вылезал по краям
            allow_place_2 = {place1 + 1, place1 - 1, place1 + 10,
                             place1 - 10}  # показываем, на какие места можно поставить второе место корабля
        elif (
                place1 % 10 == 9):  # если номер столбца все же равен 9, то выбираем не 4 дозволенные клетки, а три, вправо идти нельзя
            allow_place_2 = {place1 - 1, place1 + 10, place1 - 10}
        elif (
                place1 % 10 == 0):  # если номер столбца все же равен 0, то выбираем не 4 дозволенные клетки, а три, влево идти нельзя
            allow_place_2 = {place1 + 1, place1 + 10, place1 - 10}
        allow_place_2.intersection_update(self.allow)  # согласовываем, что такие клетки есть в дозволенном списке
        if len(
                allow_place_2) != 0:  # если существуют пустые клетки возле первого вхождения, то выбираем рандомно второе поле
            place2 = random.choice(list(allow_place_2))
            self.listBoard[place1] = 'S'
            self.listBoard[place2] = 'S'
            self.ship.append({place1, place2})  # добавляем корабль в список кораблей
            self.allow.remove(place1)  # убираем из списка дозволенных клеток
            self.allow.remove(place2)
        else:  # если же вокруг первого вхождения все клетки заняты, то снова вызываем функцию, пока корабль не установится
            self.get_place2s()
        allow_list_Pl2_1 = RemoveSq1(place1, self.allow)  # создаем переменную вызова класса
        self.allow.intersection_update(
            allow_list_Pl2_1.remover1)  # обращаемся к классу, который убирает рядом стоящие клетки из списка дозволенных
        allow_list_Pl2_2 = RemoveSq1(place2, self.allow)  # создаем переменную вызова класса
        self.allow.intersection_update(allow_list_Pl2_2.remover1)

    def get_place1s(self):
        shoot = random.choice(list(self.allow))  # выбираем рандомный ход из списка дозволенных клеток
        self.ship.append({shoot})  # добавляем корабль в список игрока или ИИ
        self.listBoard[shoot] = 'S'  # добавляем маркер корабля на доску
        # после установки корабля мы выделяем вокуруг него клетки, которые нужно убрать из списка дозволенных, так как другие корабли не должны стоять рядом
        allow_list_Pl1_5 = RemoveSq1(shoot, self.allow)
        self.allow.intersection_update(allow_list_Pl1_5.remover1)
        self.allow.remove(shoot)  # убираем координату из списка дозволенных клеток