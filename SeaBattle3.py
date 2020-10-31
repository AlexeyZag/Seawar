# существует три вида доски: пустая Q, доска игрокаL и невидимая доскаQ1 с кораблями бота
# обратите внимание на 36 строку, она позволяет выводить список чкрытых кораблей ИИ (чит для отладки)
import random
from markT import MarkT
from remove_around import RemoveSq1
from desk import Desk
from place_ship import Ship
def play():
    global n, AI_count, player_count, countA
    Q = [' ' for k in range(100)]  # Доска ИИ скрытая
    Q1 = ([' ' for k1 in range(100)])  # Доска ИИ скрытая с кораблями
    L = ([' ' for i in range(100)])  # Доска игрока скрыта
    L1 = [f'|{L[i1]}' for i1 in range(100)]  # Доска игрока видимая
    Q2 = [f'|{Q[k2]}' for k2 in range(100)]  # Доска ИИ видимая
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
    player_count = 0  # если счет равен 20, то выиграл игрок
    AI_count = 0  # если счет равен 20, то выиграл бот
    place_all_ships(L, Q1, shipListAI, shipListP, allow_list_AI1, allow_list_Pl1)  # располагает все корабли
    paint(Q, L, L1, Q2)  # выводит на консоль игру
    print(allow_list_move_on_Pl_desk)
    while True:  # играем до победы
        if end_game():  # если условие победы  выполняется, то прерываем код
            return
        print(f' Компьютер сделал {countA}-ый ход')
        #print(shipListAI)   ############################## уберите решетку, чтобы видеть список кораблей ИИ перед вашим ходом (для отладки)
        if AI_count == 20:
            print('Выиграл бот')
            return
        elif player_count == 20:
            print('Ты выиграл')
            return
        if n % 2 == 1: # если номер хода нечетный, то ходит человек
            input_nump(allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, shipListAI)
            paint(Q, L, L1, Q2)
        else:  # если номер хода нечетный, то ходит бот
             input_numA(L, allow_list_move_on_Pl_desk, move_list_AI, shipListP)
             paint(Q, L, L1, Q2)
def paint(Q, L, L1, Q2):
    painter = Desk(Q=Q, L=L, L1=L1, Q2=Q2)
    painter.paint_desk()
def input_nump(allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, shipListAI):  # ввод хода за игрока
    global n, player_count
    coordinate = input('введите номер строки и номер столбца без пробелов: ')
    try:
        coordinate = int(coordinate)  # координата должна соответствовать числу из дозволенного списка
    except ValueError:
        print('Вы вводите символы, а не числа')
        input_nump(allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, shipListAI)  # снова вызываем ввод хода, если игрок ввел не числа
    else:
        if coordinate not in allow_list_move_on_AI_desk:
            print('Выберите другие координаты')
            input_nump(allow_list_move_on_AI_desk, move_list_Pl, Q1, Q, shipListAI)
        else:
            if Q1[coordinate] == " ":  # если на невидимой доске наш выстрел попадает на пустое поле, то печатаем Т на видимой
                Q[coordinate] = 'T'
                n += 1
            elif Q1[coordinate] == 'S':  # если на невидимой доске наш выстрел попадает на поле с кораблем, то печатаем Х на видимой
                Q[coordinate] = 'X'
                player_count += 1
                move_list_Pl.add(coordinate)  #когда подбиваем корабль, то потом добавляем его в список
                remove_from_shiplist(Q, shipListAI, Q1, allow_list_move_on_AI_desk, move_list_Pl)  # убираем корабль ИИ из списка доступных, маркируем вокруг него Т
            #paint(Q, L, L1, Q2)
        try:
                allow_list_move_on_AI_desk.remove(coordinate)  # удаляем координату хода из доски ИИ из списка дозволенных ходов
        except KeyError:
            pass
    return n, player_count, allow_list_move_on_AI_desk, move_list_Pl, Q1, Q
def input_numA(L, allow_list_move_on_Pl_desk, move_list_AI, shipListP):  # ввод ИИ
    global n, AI_count, countA
    shoot = random.choice(list(allow_list_move_on_Pl_desk))  # выстрел выбирается из списка дозволенных ходов на доске игрока
    if L[shoot] == " ":  # если на доске игрока выстрел бота попадает на пустое поле, то печатаем Т, если попал, то S
        L[shoot] = 'T'
        n += 1
        countA += 1
    elif L[shoot] == 'S':
        L[shoot] = 'X'
        AI_count += 1
        move_list_AI.add(shoot)
        remove_from_shiplistP(L, allow_list_move_on_Pl_desk, move_list_AI, shipListP)
        countA += 1
    try:
        allow_list_move_on_Pl_desk.remove(shoot)  # удаляем координату хода из доски игрока из списка дозволенных ходов
    except KeyError:
        pass
    print(allow_list_move_on_Pl_desk)
    print(shoot)
    return L, n, AI_count, countA, allow_list_move_on_Pl_desk

def remove_from_shiplist(Q, shipListAI, Q1, allow_list_move_on_AI_desk, move_list_Pl):   # убирает корабль ИИ из списка доступных, маркирует вокруг него Т
    for i in range(len(shipListAI)):
        if shipListAI[i] <= move_list_Pl:
            w = shipListAI[i]
            marker_cell = MarkT(Q1, Q, w)
            Q = marker_cell.marker
            for k in w:
                remove_from_allowP = RemoveSq1(k, allow_list_move_on_AI_desk)
                allow_list_move_on_AI_desk.intersection_update(remove_from_allowP.remover1)
            shipListAI.pop(i)
            return
def remove_from_shiplistP(L, allow_list_move_on_Pl_desk, move_list_AI, shipListP):  # убирает корабль игрока из списка доступных, маркирует вокруг него Т
    for i in range(len(shipListP)):
        if shipListP[i] <= move_list_AI:
            w = shipListP[i]
            marker_cell = MarkT(L, L, w)
            L = marker_cell.marker
            for k in w:
                remove_from_allowAI = RemoveSq1(k, allow_list_move_on_Pl_desk)
                allow_list_move_on_Pl_desk.intersection_update(remove_from_allowAI.remover1)
            shipListP.pop(i)
            return
def end_game():  # условие победы
    ask = None
    if AI_count == 20:
        print('Выиграл бот')
        ask = input('Сыграем еще раз? (y/n) ').lower()
        if ask == 'y':
            print('Новая игра!')
            play()
        else:
            ask = 1
    elif player_count == 20:
        print('Ты выиграл!')
        ask = input('Сыграем еще раз? (y/n) ').lower()
        if ask == 'y':
            print('Новая игра!')
            play()
        else:
            ask = 1
    return ask


#  Ниже представлены функциии которые устанавливают на доски корабли

def place1s(allow, listBoard, ship):  # функция, устанавливающая 1-палубные корабли, в качестве аргументов принимает:
    # список клеток игрока или ИИ, доску игрока или ИИ, дополнять список кораблей игрока или ИИ
    placer = Ship(allow, listBoard, ship)
    placer.get_place1s()

def place2s(allow, listBoard, ship):  # функция, устанавливающая 1-палубные корабли
    placer = Ship(allow, listBoard, ship)
    placer.get_place2s()
def place3s(allow, listBoard, ship):
    placer = Ship(allow, listBoard, ship)
    placer.get_place3s()
def place4s(allow, listBoard, ship):
    placer = Ship(allow, listBoard, ship)
    placer.get_place4s()

def place_all_ships(L, Q1, shipListAI, shipListP, allow_list_Pl1, allow_list_AI1):  # устанавливает все корабли на доске игрока и на невидимой доске
    place4s(allow_list_Pl1, L, shipListP)
    place3s(allow_list_Pl1, L, shipListP)
    place3s(allow_list_Pl1, L, shipListP)
    place2s(allow_list_Pl1, L, shipListP)
    place2s(allow_list_Pl1, L, shipListP)
    place2s(allow_list_Pl1, L, shipListP)
    place1s(allow_list_Pl1, L, shipListP)
    place1s(allow_list_Pl1, L, shipListP)
    place1s(allow_list_Pl1, L, shipListP)
    place1s(allow_list_Pl1, L, shipListP)
    place4s(allow_list_AI1, Q1, shipListAI)
    place3s(allow_list_AI1, Q1, shipListAI)
    place3s(allow_list_AI1, Q1, shipListAI)
    place2s(allow_list_AI1, Q1, shipListAI)
    place2s(allow_list_AI1, Q1, shipListAI)
    place2s(allow_list_AI1, Q1, shipListAI)
    place1s(allow_list_AI1, Q1, shipListAI)
    place1s(allow_list_AI1, Q1, shipListAI)
    place1s(allow_list_AI1, Q1, shipListAI)
    place1s(allow_list_AI1, Q1, shipListAI)
play()
