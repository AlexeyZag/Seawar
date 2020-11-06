# существует три вида доски: пустая Q, доска игрокаL и невидимая доскаQ1 с кораблями бота
# обратите внимание на 51 строку, она позволяет выводить список чкрытых кораблей ИИ (чит для отладки)
import random
from markT import MarkT
from remove_around import RemoveSq1
from desk import Desk
from place_ship import Ship
from exception import IndexException
class Start:
    def __init__(self):
        global n, countA
        Q = [' ' for k in range(100)]  # Доска ИИ скрытая
        Q1 = [' ' for k1 in range(100)]  # Доска ИИ скрытая с кораблями
        L = [' ' for i in range(100)]  # Доска игрока скрыта
        shipListP = []  # список координат кораблей игрока
        shipListAI = []  # список координат кораблей ИИ
        move_list_AI = set()  # список сделанных ходов игроком
        move_list_Pl = set()  # список сделанных ходов ИИ
        allow_list_Pl1 = set(([w1 for w1 in range(100)]))  # список клеток, куда можно ставить корабли на доску игрока, используются для расположение кораблей на досках
        allow_list_AI1 = set(([w2 for w2 in range(100)]))  # список клеток, куда можно ставить корабли на доску ИИ
        # текущие доступные ходы на доске ИИ
        allow_list_move_on_AI_desk = set([t1 for t1 in range(100)])
        # текущие доступные ходы на доске игрока
        allow_list_move_on_Pl_desk = set([t2 for t2 in range(100)])
        n = 1  #  текущий номер хода неетный, поэтому первым ходит игрок
        countA = 0  #сколько ходов сделал ИИ
        place_all_ships(L, Q1, shipListAI, shipListP, allow_list_AI1, allow_list_Pl1)  # располагает все корабли
        paint(Q, L)  # выводит на консоль игру
        gamer = Game(shipListAI, shipListP, allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, L, allow_list_move_on_Pl_desk, move_list_AI)
        gamer.play()

class Game:  # класс, который включает в себя объявление переменных, ход игры, ввод чисел, и логика конца игры
    def __init__(self, shipListAI, shipListP, allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, L, allow_list_move_on_Pl_desk, move_list_AI):
        self.shipListAI = shipListAI
        self.shipListP = shipListP
        self.allow_list_move_on_AI_desk = allow_list_move_on_AI_desk
        self.move_list_Pl = move_list_Pl
        self.Q1 = Q1
        self.Q = Q
        self.L = L
        self.allow_list_move_on_Pl_desk = allow_list_move_on_Pl_desk
        self.move_list_AI = move_list_AI


    def play(self):  #
        global n
        while True:  # играем до победы
            # если условие победы  выполняется, то прерываем код
            if self.end_game():
                return
            print(f' Компьютер сделал {countA}-ый ход')
            print(self.shipListAI)   ############################## уберите решетку, чтобы видеть список кораблей ИИ перед вашим ходом (для отладки)
            if n % 2 == 1: # если номер хода нечетный, то ходит человек
                self.input_numP()
                paint(self.Q, self.L)
            else:  # если номер хода нечетный, то ходит бот
                self.input_shoot()
                paint(self.Q, self.L)


    def input_numP(self):  # ввод игрока
        global n
        coordinate = input('введите номер строки и номер столбца без пробелов: ')
        coor = IndexException(coordinate, self.allow_list_move_on_AI_desk)
        if coor.check_coor() == 1:
            print('Вы ввели неправильное значение ')
            return self.input_numP()  # снова вызываем ввод хода, если игрок ввел не числа
        else:
            coordinate = int(coordinate)
            if self.Q1[coordinate] == " ":  # если на невидимой доске наш выстрел попадает на пустое поле, то печатаем Т на видимой
                self.Q[coordinate] = 'T'
                n += 1
            elif self.Q1[coordinate] == 'S':  # если на невидимой доске наш выстрел попадает на поле с кораблем, то печатаем Х на видимой
                self.Q[coordinate] = 'X'
                self.move_list_Pl.add(coordinate)  #когда подбиваем корабль, то потом добавляем его в список
                removeA = RemoveFromShiplist(self.Q, self.allow_list_move_on_AI_desk, self.move_list_Pl, self.shipListAI)
                removeA.mark_and_remove()  # убираем корабль ИИ из списка доступных, маркируем вокруг него Т
            #paint(Q, L, L1, Q2)
            try:
                self.allow_list_move_on_AI_desk.remove(coordinate)  # удаляем координату хода из доски ИИ из списка дозволенных ходов
            except KeyError:
                pass
        return n, self.allow_list_move_on_AI_desk, self.move_list_Pl, self.Q1, self.Q

    def input_shoot(self):  # ввод ИИ
        global n, countA
        shoot = random.choice(list(self.allow_list_move_on_Pl_desk))  # выстрел выбирается из списка дозволенных ходов на доске игрока
        if self.L[shoot] == " ":  # если на доске игрока выстрел бота попадает на пустое поле, то печатаем Т, если попал, то S
            self.L[shoot] = 'T'
            n += 1
            countA += 1
        elif self.L[shoot] == 'S':
            self.L[shoot] = 'X'
            self.move_list_AI.add(shoot)
            removeP = RemoveFromShiplist(self.L, self.allow_list_move_on_Pl_desk, self.move_list_AI, self.shipListP)
            removeP.mark_and_remove()
            countA += 1
        try:
            self.allow_list_move_on_Pl_desk.remove(shoot)  # удаляем координату хода из доски игрока из списка дозволенных ходов
        except KeyError:
            pass
        print(self.allow_list_move_on_Pl_desk)
        print(shoot)
        return self.L, n, countA, self.allow_list_move_on_Pl_desk, self.move_list_AI, self.shipListP

    def end_game(self):  # конец игры
        ask = None
        if len(self.shipListP) == 0:
            print('Выиграл бот')
        elif len(self.shipListAI) == 0:
            print('Ты выиграл!')
        if len(self.shipListP) == 0 or len(self.shipListAI) == 0:
            ask = input('Сыграем еще раз? (y/n) ').lower()
            if ask == 'y':
                print('Новая игра!')
                Start()
            else:
                ask = 1
        return ask

class RemoveFromShiplist:   # убирает корабль ИИ из списка доступных, маркирует вокруг него Т

    def __init__(self, List, allow_list_move_on, move_list, shipList):
        self.List = List
        self.allow_list_move_on = allow_list_move_on
        self.move_list = move_list
        self.shipList = shipList

    def mark_and_remove(self):

        for i in range(len(self.shipList)):
            if self.shipList[i] <= self.move_list:
                w = self.shipList[i]
                marker_cell = MarkT(self.List, w)
                Q = marker_cell.marker
                for k in w:
                    remove_from_allow = RemoveSq1(k, self.allow_list_move_on)
                    self.allow_list_move_on.intersection_update(remove_from_allow.remover1)
                self.shipList.pop(i)
                return



def paint(Q, L):
    painter = Desk(Q=Q, L=L)
    painter.paint_desk()
#  Ниже представлены функциии которые устанавливают на доски корабли



def place_all_ships(L, Q1, shipListAI, shipListP, allow_list_Pl1, allow_list_AI1):  # устанавливает все корабли на доске игрока и на невидимой доске
    placer = Ship(4, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(3, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(3, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(2, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(2, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(2, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(1, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(1, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(1, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(1, allow_list_Pl1, L, shipListP)
    placer.place()
    placer = Ship(4, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(3, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(3, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(2, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(2, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(2, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(1, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(1, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(1, allow_list_AI1, Q1, shipListAI)
    placer.place()
    placer = Ship(1, allow_list_AI1, Q1, shipListAI)
    placer.place()

Start()
