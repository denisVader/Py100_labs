RAZMER = 9   # количество ячеек
X = 'x'      # символ первого игрока
O = 'o'      # символ второго игрока
VIN = ((0, 1, 2),    # Выигрышные комбинации
       (3, 4, 5),
       (6, 7, 8),
       (0, 3, 6),
       (1, 4, 7),
       (2, 5, 8),
       (0, 4, 8),
       (6, 4, 2))


def main():
    p1, p2 = perviy_hod()
    current_player = p1
    field = game_field()
    show_field(field)
    for i in range(RAZMER):
        idx = kuda_hodit(field, current_player)
        field[idx] = current_player
        show_field(field)
        if result(field):
            print(f'Игрок {current_player} выиграл')
            return current_player
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1
    print('Ничья')


def perviy_hod():
    perviy = input('Первые ходят крестики, Вы хотите играть крестиками?: ')
    if perviy.lower() == 'да':    # ответ 'да' с любым регистром
        player1 = 'X'
        player2 = 'O'
    else:
        player1 = 'O'             # если другой символ, то игрок ходит "0"
        player2 = 'X'
    return player1, player2


'''Создать  игральное поле'''
def game_field():
    field = list(range(RAZMER))
    return field
field = game_field()


def show_field(field):
    print('----------')
    print(field[0], '|', field[1], '|', field[2])
    print('----------')
    print(field[3], '|', field[4], '|', field[5])
    print('----------')
    print(field[6], '|', field[7], '|', field[8])
    print('----------')
    # print(pokazat_pole(pole))
show_field(field)

def kuda_hodit(field, current_player):
    while True:
        idx = input(f'Куда хотите сходить? Игрок {current_player}:')
        if not idx.isdigit():
            print("Введи цифру")
            continue
        else:
            idx = int(idx)
        if not 0 <= idx < RAZMER:
            print(f"Нет такой ячейки, выбери от 0 до {RAZMER - 1}")
            continue
        if field[idx] in ("X", "O"):
            print("Ячейка занята, сходи еще раз:")
            continue
        return idx


def result(field):
    for i in VIN:
        if field[i[0]] == field[i[1]] == field[i[2]]:
            return True
    return False

main()
