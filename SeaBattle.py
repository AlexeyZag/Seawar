# существует три вида доски: пустая Q, доска игрокаL и невидимая доскаQ1 с кораблями бота
import random
from remove_around import RemoveSq1
def play():
    global n, Q, L, Q1, allow_list_AI, allow_list_Pl, AI_count, player_count, allow_list_Pl1, allow_list_AI1
    Q = ([' ' for k in range(100)])  # Доска ИИ
    L = ([' ' for i in range(100)])  # Доска игрока пустая
    Q1 = ([' ' for j in range(100)])  # Доска ИИ скрытая с кораблями
    allow_list_Pl1 = set(([k for k in range(100)]))  # список клеток, куда можно ставить корабли на доску игрока
    allow_list_AI1 = set(([k for k in range(100)]))  # список клеток, куда можно ставить корабли на доску ИИ
    # текущие доступные ходы на доске ИИ
    allow_list_AI = set(([k for k in range(100)]))
    # текущие доступные ходы на доске игрока
    allow_list_Pl = set(([k for k in range(100)]))
    n = 1
    player_count = 0  # если счет равен 20, то выиграл игрок
    AI_count = 0  # если счет равен 20, то выиграл бот
    place_all_ships()
    paint()  # выводит на консоль игру
    while True:  # играем до победы
        if end_game():  # если условие победы  выполняется, то прерываем код
            return
        elif n % 2 == 1: # если номер хода нечетный, то ходит человек
            input_nump()
        else:  # если номер хода нечетный, то ходит бот
             input_numA()
             paint()
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

def paint():  # выводит тело игры
    global Q, L
    print(f""" |0|1|2|3|4|5|6|7|8|9|          |0|1|2|3|4|5|6|7|8|9|
0|{Q[0]}|{Q[1]}|{Q[2]}|{Q[3]}|{Q[4]}|{Q[5]}|{Q[6]}|{Q[7]}|{Q[8]}|{Q[9]}|         0|{L[0]}|{L[1]}|{L[2]}|{L[3]}|{L[4]}|{L[5]}|{L[6]}|{L[7]}|{L[8]}|{L[9]}|
1|{Q[10]}|{Q[11]}|{Q[12]}|{Q[13]}|{Q[14]}|{Q[15]}|{Q[16]}|{Q[17]}|{Q[18]}|{Q[19]}|         1|{L[10]}|{L[11]}|{L[12]}|{L[13]}|{L[14]}|{L[15]}|{L[16]}|{L[17]}|{L[18]}|{L[19]}|
2|{Q[20]}|{Q[21]}|{Q[22]}|{Q[23]}|{Q[24]}|{Q[25]}|{Q[26]}|{Q[27]}|{Q[28]}|{Q[29]}|         2|{L[20]}|{L[21]}|{L[22]}|{L[23]}|{L[24]}|{L[25]}|{L[26]}|{L[27]}|{L[28]}|{L[29]}|
3|{Q[30]}|{Q[31]}|{Q[32]}|{Q[33]}|{Q[34]}|{Q[35]}|{Q[36]}|{Q[37]}|{Q[38]}|{Q[39]}|         3|{L[30]}|{L[31]}|{L[32]}|{L[33]}|{L[34]}|{L[35]}|{L[36]}|{L[37]}|{L[38]}|{L[39]}|
4|{Q[40]}|{Q[41]}|{Q[42]}|{Q[43]}|{Q[44]}|{Q[45]}|{Q[46]}|{Q[47]}|{Q[48]}|{Q[49]}|         4|{L[40]}|{L[41]}|{L[42]}|{L[43]}|{L[44]}|{L[45]}|{L[46]}|{L[47]}|{L[48]}|{L[49]}|
5|{Q[50]}|{Q[51]}|{Q[52]}|{Q[53]}|{Q[54]}|{Q[55]}|{Q[56]}|{Q[57]}|{Q[58]}|{Q[59]}|         5|{L[50]}|{L[51]}|{L[52]}|{L[53]}|{L[54]}|{L[55]}|{L[56]}|{L[57]}|{L[58]}|{L[59]}|
6|{Q[60]}|{Q[61]}|{Q[62]}|{Q[63]}|{Q[64]}|{Q[65]}|{Q[66]}|{Q[67]}|{Q[68]}|{Q[69]}|         6|{L[60]}|{L[61]}|{L[62]}|{L[63]}|{L[64]}|{L[65]}|{L[66]}|{L[67]}|{L[68]}|{L[69]}|
7|{Q[70]}|{Q[71]}|{Q[72]}|{Q[73]}|{Q[74]}|{Q[75]}|{Q[76]}|{Q[77]}|{Q[78]}|{Q[79]}|         7|{L[70]}|{L[71]}|{L[72]}|{L[73]}|{L[74]}|{L[75]}|{L[76]}|{L[77]}|{L[78]}|{L[79]}|
8|{Q[80]}|{Q[81]}|{Q[82]}|{Q[83]}|{Q[84]}|{Q[85]}|{Q[86]}|{Q[87]}|{Q[88]}|{Q[89]}|         8|{L[80]}|{L[81]}|{L[82]}|{L[83]}|{L[84]}|{L[85]}|{L[86]}|{L[87]}|{L[88]}|{L[89]}|
9|{Q[90]}|{Q[91]}|{Q[92]}|{Q[93]}|{Q[94]}|{Q[95]}|{Q[96]}|{Q[97]}|{Q[98]}|{Q[99]}|         9|{L[90]}|{L[91]}|{L[92]}|{L[93]}|{L[94]}|{L[95]}|{L[96]}|{L[97]}|{L[98]}|{L[99]}|
""")
def input_nump():  # ввод хода за игрока
    global n, player_count, allow_list_AI, allow_list_Pl, move_list_Pl
    a = input('введите номер строки ')
    b = input('введите номер столбца ')
    try:
        coordinate = 10 * int(a) + int(b)  # координата должна соответствовать числу из дозволенного списка
    except ValueError:
        print('Вы вводите символы, а не числа')
        input_nump()  # снова вызываем ввод хода, если игрок введ не числа
    else:
        if coordinate not in allow_list_AI:
            print('Выберите другие координаты')
            input_nump()
        else:
            if Q1[coordinate] == " ":  # если на невидимой доске наш выстрел попадает на пустое поле, то печатаем Т на пустой
                Q[coordinate] = 'T'
                n += 1
            elif Q1[coordinate] == 'S':  # если на невидимой доске наш выстрел попадает на поле с кораблем, то печатаем Х на пустой
                Q[coordinate] = 'X'
                player_count += 1
                paint()
            allow_list_AI.remove(coordinate)  # удаляем координату хода из доски ИИ из списка дозволенных ходов

def input_numA():  # ввод ИИ
    global L, n, AI_count
    shoot = random.choice(list(allow_list_Pl))  # выстрел выбирается из списка дозволенных ходов на доске игрока
    if L[shoot] == " ":  # если на доске игрока выстрел бота попадает на пустое поле, то печатаем Т, если попал, то S
        L[shoot] = 'T'
        n += 1
    elif L[shoot] == 'S':
        L[shoot] = 'X'
        AI_count += 1
    allow_list_Pl.remove(shoot)  # удаляем координату хода из доски игрока из списка дозволенных ходов


#  Ниже представлены функциии которые устанавливают на доски корабли

def place1s(allow, listBoard):  # функция, устанавливающая 1-палубные корабли, в качестве аргументов принимает:
    # список клеток игрока или ИИ, доску игрока или ИИ, дополнять список кораблей игрока или ИИ
    global allow_list_Pl1, allow_list_AI1, shoot
    shoot = random.choice(list(allow))  # выбираем рандомный ход из списка дозволенных клеток
    listBoard[shoot] = 'S'  # добавляем маркер корабля на доску
    # после установки корабля мы выделяем вокуруг него клетки, которые нужно убрать из списка дозволенных, так как другие корабли не должны стоять рядом
    allow_list_Pl1_5 = RemoveSq1(shoot, allow)
    allow.intersection_update(allow_list_Pl1_5.remover1)
    allow.remove(shoot)  # убираем координату из списка дозволенных клеток

def place2s(allow, listBoard):  # функция, устанавливающая 1-палубные корабли
    #  allow_place_2 - список клеток, куда можно будет поставить вторую палубу
    global allow_place_2, place2, place1
    place1 = random.choice(list(allow))  # выбираем пустую клетку
    if place1 % 10 != 9 and place1 % 10 != 0:  # если номер столбца не равен 0 или 9, делается для того, чтобы корабль не вылезал по краям
        allow_place_2 = {place1 + 1, place1 - 1, place1 + 10, place1 - 10}  # показываем, на какие места можно поставить второе место корабля
    elif(place1 % 10 == 9):  # если номер столбца все же равен 9, то выбираем не 4 дозволенные клетки, а три, вправо идти нельзя
        allow_place_2 = {place1 - 1, place1 + 10, place1 - 10}
    elif (place1 % 10 == 0): # если номер столбца все же равен 0, то выбираем не 4 дозволенные клетки, а три, влево идти нельзя
        allow_place_2 = {place1 + 1, place1 + 10, place1 - 10}
    allow_place_2.intersection_update(allow)  # согласовываем, что такие клетки есть в дозволенном списке
    if len(allow_place_2) != 0:  # если существуют пустые клетки возле первого вхождения, то выбираем рандомно второе поле
        place2 = random.choice(list(allow_place_2))
        listBoard[place1] = 'S'
        listBoard[place2] = 'S'
        allow.remove(place1)  # убираем из списка дозволенных клеток
        allow.remove(place2)
    else:  # если же вокруг первого вхождения все клетки заняты, то снова вызываем функцию, пока корабль не установится
        place2s(allow, listBoard)
    allow_list_Pl2_1 = RemoveSq1(place1, allow)  # создаем переменную вызова класса
    allow.intersection_update(allow_list_Pl2_1.remover1)  # обращаемся к классу, который убирает рядом стоящие клетки из списка дозволенных
    allow_list_Pl2_2 = RemoveSq1(place2, allow)  # создаем переменную вызова класса
    allow.intersection_update(allow_list_Pl2_2.remover1)
def place3s(allow, listBoard):
    global place3_3, place3_1, allow_list_Pl1, allow_list_Pl1_2, place3_2
    place3_1 = random.choice(list(allow))  # выбираем пустую клетку
    allow_place3_2 = set()
    if place3_1 % 10 != 0 and place3_1 % 10 != 1 and place3_1 % 10 != 8 and place3_1 % 10 != 9:
        if {place3_1 + 1, place3_1 + 2} <= allow:
            allow_place3_2.add(place3_1 + 1)
        if {place3_1 - 1, place3_1 - 2} <= allow:
            allow_place3_2.add(place3_1 - 1)
        if {place3_1 - 10, place3_1 - 20} <= allow:
            allow_place3_2.add(place3_1 - 10)
        if {place3_1 + 10, place3_1 + 20} <= allow:
            allow_place3_2.add(place3_1 + 10)
    elif place3_1 % 10 == 0 or place3_1 % 10 == 1:
        if {place3_1 + 1, place3_1 + 2} <= allow:
            allow_place3_2.add(place3_1 + 1)
        if {place3_1 - 10, place3_1 - 20} <= allow:
            allow_place3_2.add(place3_1 - 10)
        if {place3_1 + 10, place3_1 + 20} <= allow:
            allow_place3_2.add(place3_1 + 10)
    elif place3_1 % 10 == 8 or place3_1 % 10 == 9:
        if {place3_1 - 1, place3_1 - 2} <= allow:
            allow_place3_2.add(place3_1 - 1)
        if {place3_1 - 10, place3_1 - 20} <= allow:
            allow_place3_2.add(place3_1 - 10)
        if {place3_1 + 10, place3_1 + 20} <= allow:
            allow_place3_2.add(place3_1 + 10)
    if len(allow_place3_2) != 0:
        place3_2 = random.choice(list(allow_place3_2))
        if place3_2 == place3_1 + 1:
            listBoard[place3_1], listBoard[place3_2], listBoard[place3_2 + 1] = 'S', 'S', 'S'
            place3_3 = place3_2 + 1
        elif place3_2 == place3_1 - 1:
            listBoard[place3_1], listBoard[place3_2], listBoard[place3_2 - 1] = 'S', 'S', 'S'
            place3_3 = place3_2 - 1
        elif place3_2 == place3_1 - 10:
            listBoard[place3_1], listBoard[place3_2], listBoard[place3_2 - 10] = 'S', 'S', 'S'
            place3_3 = place3_2 - 10
        elif place3_2 == place3_1 + 10:
            listBoard[place3_1], listBoard[place3_2], listBoard[place3_2 + 10] = 'S', 'S', 'S'
            place3_3 = place3_2 + 10
        allow.remove(place3_1)
        allow.remove(place3_2)
        allow.remove(place3_3)
    else:
        place3s(allow, listBoard)
    allow_list_Pl3_1 = RemoveSq1(place3_1, allow)
    allow.intersection_update(allow_list_Pl3_1.remover1)
    allow_list_Pl3_2 = RemoveSq1(place3_2, allow)
    allow.intersection_update(allow_list_Pl3_2.remover1)
    allow_list_Pl3_3 = RemoveSq1(place3_3, allow)
    allow.intersection_update(allow_list_Pl3_3.remover1)
def place4s(allow, listBoard):
    global place4_3, place4_4, place4_1, place4_2
    place4_1 = random.choice(list(allow))  # выбираем пустую клетку
    allow_place4_2 = set()  # множество, показывающее направление 4палубника
    if {place4_1 - 30} <= allow:  # если сверху нет ограничений добавляем направление вверх
        allow_place4_2.add(place4_1 - 10)
    if {place4_1 + 30} <= allow:  # если снизу нет ограничений добавляем направление вниз
        allow_place4_2.add(place4_1 + 10)
    if place4_1 % 10 != 0 and place4_1 % 10 != 1 and place4_1 % 10 != 2 and place4_1 % 10 != 7 and place4_1 % 10 != 8 and place4_1 % 10 != 9:
        allow_place4_2.add(place4_1 + 1)  # влево и вправо нет ограничений
        allow_place4_2.add(place4_1 - 1)
    elif place4_1 % 10 == 0 or place4_1 % 10 == 1 or place4_1 % 10 == 2:
        allow_place4_2.add(place4_1 + 1)
    elif place4_1 % 10 == 8 or place4_1 % 10 == 9 or place4_1 % 10 == 7:
        allow_place4_2.add(place4_1 - 1)
    if len(allow_place4_2) != 0:
        place4_2 = random.choice(list(allow_place4_2))
        if place4_2 == place4_1 + 1:
            listBoard[place4_1], listBoard[place4_2], listBoard[place4_2 + 1], listBoard[place4_2 + 2] = 'S', 'S', 'S', 'S'
            place4_3 = place4_2 + 1
            place4_4 = place4_2 + 2
        elif place4_2 == place4_1 - 1:
            listBoard[place4_1], listBoard[place4_2], listBoard[place4_2 - 1], listBoard[place4_2 - 2] = 'S', 'S', 'S', 'S'
            place4_3 = place4_2 - 1
            place4_4 = place4_2 - 2
        elif place4_2 == place4_1 - 10:
            listBoard[place4_1], listBoard[place4_2], listBoard[place4_2 - 10], listBoard[place4_2 - 20] = 'S', 'S', 'S', 'S'
            place4_3 = place4_2 - 10
            place4_4 = place4_2 - 20
        elif place4_2 == place4_1 + 10:
            listBoard[place4_1], listBoard[place4_2], listBoard[place4_2 + 10], listBoard[place4_2 + 20] = 'S', 'S', 'S', 'S'
            place4_3 = place4_2 + 10
            place4_4 = place4_2 + 20
        allow.remove(place4_1)
        allow.remove(place4_2)
        allow.remove(place4_3)
        allow.remove(place4_4)
    else:
        place4s(allow, listBoard)
    allow_list_Pl4_1 = RemoveSq1(place4_1, allow)
    allow.intersection_update(allow_list_Pl4_1.remover1)
    allow_list_Pl4_2 = RemoveSq1(place4_2, allow)
    allow.intersection_update(allow_list_Pl4_2.remover1)
    allow_list_Pl4_3 = RemoveSq1(place4_3, allow)
    allow.intersection_update(allow_list_Pl4_3.remover1)
    allow_list_Pl4_4 = RemoveSq1(place4_4, allow)
    allow.intersection_update(allow_list_Pl4_4.remover1)
def place_all_ships():  # устанавливает все корабли на доске игрока и на невидимой доске
    global L, Q1
    place4s(allow_list_Pl1, L)
    place3s(allow_list_Pl1, L)
    place3s(allow_list_Pl1, L)
    place2s(allow_list_Pl1, L)
    place2s(allow_list_Pl1, L)
    place2s(allow_list_Pl1, L)
    place1s(allow_list_Pl1, L)
    place1s(allow_list_Pl1, L)
    place1s(allow_list_Pl1, L)
    place1s(allow_list_Pl1, L)
    place4s(allow_list_AI1, Q1)
    place3s(allow_list_AI1, Q1)
    place3s(allow_list_AI1, Q1)
    place2s(allow_list_AI1, Q1)
    place2s(allow_list_AI1, Q1)
    place2s(allow_list_AI1, Q1)
    place1s(allow_list_AI1, Q1)
    place1s(allow_list_AI1, Q1)
    place1s(allow_list_AI1, Q1)
    place1s(allow_list_AI1, Q1)
play()
