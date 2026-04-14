import random
field = [[' '] * 5 for _ in range(5)]

add_tail_one = False
add_tail_two = False
add_tail_three = False
add_tail_four = False
add_tail_five = False
add_tail_six = False
add_tail_seven = False
add_tail_eight = False
add_tail_nine = False
add_tail_ten = False
add_tail_eleven = False
add_tail_twelve = False
add_tail_thirteen = False
add_tail_fourteen = False
add_tail_fifteen = False
add_tail_sixteen = False
add_tail_seventeen = False
add_tail_eighteen = False
add_tail_nineteen = False
add_tail_twenty = False
add_tail_twenty_one = False

var_one = None
var_two = None
var_three = None
var_four = None
var_five = None
var_six = None
var_seven = None
var_eight = None
var_nine = None
var_ten = None
var_eleven = None
var_twelve = None
var_thirteen = None
var_fourteen = None
var_fifteen = None
var_sixteen = None
var_seventeen = None
var_eighteen = None
var_nineteen = None
var_twenty = None
var_twenty_one = None

score = 0


def board():
    """Выводит текущее состояние поля."""
    width = len(field[0])
    print("┌" + "───" * width + "┐")
    for row in field:
        display_row = [char if char != ' ' else '.' for char in row]
        print('│ ' + '  '.join(display_row) + ' │')
    print('└' + '───' * width + '┘')


def clear():
    """Очищает поле.
    
    Очищение поля необходимо, чтобы
    предыдущие координаты змейки не накладывались на новые.
    Также функция при очищении игнорирует яблоко.
    """
    for row in field:
        for i in range(len(row)):
            if row[i] == '@':
                continue
            else:
                row[i] = ' '


def start_snake():
    """Записывает стартовые координаты змейки для первичного вывода."""
    field[2][1] = 'X'
    field[2][2] = 'O'
    field[2][3] = 'O'


def spawn_apple():
    """Выводит яблоко на поле.
    
    Функция берет рандомные координаты и если эти координаты
    равны пробелу в кавычках, то записываем в эти координаты
    яблоко (символ @)
    """
    while True:
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        if field[row][column] != ' ':
            continue
        else:
            field[row][column] = '@'
            break


def apple_is_exists():
    """Проверяет, находится ли яблоко на поле.
    
    Если яблока на поле нет - выводит его.
    """
    apple_coordinates = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '@':
                apple_coordinates.append((i, j))
    if apple_coordinates == []:
        spawn_apple()


def head_coordinates_of_snake():
    """Возвращает координаты головы.
    
    Координаты возвращаются как список, в котором один кортеж из двух координат.
    """
    head_coordinates = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 'X':
                head_coordinates.append((i, j))
    return head_coordinates


def body_coordinates_of_snake():
    """Возвращает координаты тела и хвоста.
    
    Предисловие: изначально я не думал над игрой как над концепцией в целом, не думал
    над масштабируюемостью, поэтому я решил сначала сделать самое простое - это змейку,
    которая будет состоять из трех элементов: головы, тела и хвоста. Змейку, которая
    будет просто двигаться по карте.

    Поскольку функция ищет и добавляет координаты слева-направо и сверху-вниз, то
    может произойти путаница: где хвост, а где тело. Для этого я разработал логические
    блоки кода, которые помогают понять, где хвост, а где тело. Например: в положении
    X O O, без логических блоков, тело и хвост будут считаться правильно, а в примере
    O O X программа посчитает хвост за тело и тело за хвост.
    """
    body_coordinates = []
    head_coordinates = head_coordinates_of_snake()
    final_body_coordinates = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 'O':
                body_coordinates.append((i, j))

    if head_coordinates[0][0] == body_coordinates[0][0] and body_coordinates[0][0] != body_coordinates[1][0]:
        final_body_coordinates.append(body_coordinates[0])
        final_body_coordinates.append(body_coordinates[1])
    elif head_coordinates[0][0] == body_coordinates[1][0] and body_coordinates[0][0] != body_coordinates[1][0]:
        final_body_coordinates.append(body_coordinates[1])
        final_body_coordinates.append(body_coordinates[0])

    elif head_coordinates[0][1] == body_coordinates[0][1] and head_coordinates[0][1] != body_coordinates[1][1]:
        final_body_coordinates.append(body_coordinates[0])
        final_body_coordinates.append(body_coordinates[1])
    elif head_coordinates[0][1] == body_coordinates[1][1] and head_coordinates[0][1] != body_coordinates[0][1]:
        final_body_coordinates.append(body_coordinates[1])
        final_body_coordinates.append(body_coordinates[0])

    elif head_coordinates[0][1] == body_coordinates[0][1] == body_coordinates[1][1] and head_coordinates[0][0] < body_coordinates[0][0]:
        final_body_coordinates.append(body_coordinates[0])
        final_body_coordinates.append(body_coordinates[1])
    elif head_coordinates[0][1] == body_coordinates[0][1] == body_coordinates[1][1] and head_coordinates[0][0] > body_coordinates[0][0]:
        final_body_coordinates.append(body_coordinates[1])
        final_body_coordinates.append(body_coordinates[0])

    elif head_coordinates[0][0] == body_coordinates[0][0] == body_coordinates[1][0] and head_coordinates[0][1] < body_coordinates[1][1]:
        final_body_coordinates.append(body_coordinates[0])
        final_body_coordinates.append(body_coordinates[1])
    elif head_coordinates[0][0] == body_coordinates[0][0] == body_coordinates[1][0] and head_coordinates[0][1] > body_coordinates[1][1]:
        final_body_coordinates.append(body_coordinates[1])
        final_body_coordinates.append(body_coordinates[0])

    return final_body_coordinates


def apple_coordinates_on_board():
    """Возвращает коордианты яблока."""
    apple_coordinates = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == '@':
                apple_coordinates.append((i, j))
    return apple_coordinates


def define_form(head, body):
    """Определяет, в каком положении сейчас находится змейка на поле и возвращает название положения (строковый литерал first, second и т.д)."""
    form = None

    if head[0][0] == body[0][0] == body[1][0] and head[0][1] < body[1][1]: # X O O
        form = 'first'
        return form
    elif head[0][0] == body[0][0] == body[1][0] and head[0][1] > body[1][1]: # O O X
        form = 'second'
        return form
    elif head[0][1] == body[0][1] == body[1][1] and head[0][0] < body[1][0]: # X
        form = 'third'                                                       # O
        return form                                                          # O
    elif head[0][1] == body[0][1] == body[1][1] and head[0][0] > body[1][0]: # O
        form = 'fourth'                                                      # O               
        return form                                                          # X           
    elif body[0][0] == body[1][0] and body[0][1] > body[1][1] and head[0][0] > body[0][0] and head[0][0] > body[1][0]: # O O
        form = 'eleventh'                                                                                              #   X
        return form
    elif body[0][0] == body[1][0] and body[0][1] < body[1][1] and head[0][0] > body[0][0] and head[0][0] > body[1][0]: # O O
        form = 'twelfth'                                                                                               # X
        return form
    elif body[0][0] == body[1][0] and body[0][1] > body[1][1] and head[0][0] < body[0][0] and head[0][0] < body[1][0]: #   X
        form = 'ninth'                                                                                                 # O O
        return form
    elif body[0][0] == body[1][0] and body[0][1] < body[1][1] and head[0][0] < body[0][0] and head[0][0] < body[1][0]: # X
        form = 'tenth'                                                                                                 # O O
        return form
    elif head[0][0] == body[0][0] and body[0][0] < body[1][0] and body[0][1] == body[1][1] and head[0][1] > body[0][1] and head[0][1] > body[1][1]: # O X
        form = 'fifth'                                                                                                                              # O
        return form
    elif head[0][0] == body[0][0] and body[0][0] > body[1][0] and body[0][1] == body[1][1] and head[0][1] > body[0][1] and head[0][1] > body[1][1]: # O
        form = 'sixth'                                                                                                                              # O X
        return form
    elif head[0][0] == body[0][0] and body[0][0] < body[1][0] and body[0][1] == body[1][1] and head[0][1] < body[0][1] and head[0][1] < body[1][1]: # X O
        form = 'seventh'                                                                                                                            #   O
        return form
    elif head[0][0] == body[0][0] and body[0][0] > body[1][0] and body[0][1] == body[1][1] and head[0][1] < body[0][1] and head[0][1] < body[1][1]: #   O
        form = 'eighth'                                                                                                                             # X O
        return form


def current_position_of_snake_and_moveing(head, body, mhc = 0, mhr = 0, phc = 0, phr = 0,
                              mb1c = 0, mb1r = 0, pb1c = 0, pb1r = 0,
                              mb2c = 0, mb2r = 0, pb2c = 0, pb2r = 0):
    """Двигает змейку по полю, определяет момент столкновения, увеличивает змейку от стандартной(X O O), считает полученные очки,
    проверяет, чтобы яблоко всегда было на поле.
    
    В аргументах функции, после head и body, идут аббревиатуры, они были добавлены для того,
    чтобы я мог легко ореинтироваться при написании основного кода: куда двигается змейка при том или ином шаге.
    Расшифровка каждой использованной буквы: p - plus, m - minus, h - head, b1 - body1, b2 - body2, r - row, c - column.

    Если змейка сталкивается со стеной или с самой собой, то возращается строковый литерал crash.
    """
    global var_one
    global var_two
    global var_three
    global var_four
    global var_five
    global var_six
    global var_seven
    global var_eight
    global var_nine
    global var_ten
    global var_eleven
    global var_twelve
    global var_thirteen
    global var_fourteen
    global var_fifteen
    global var_sixteen
    global var_seventeen
    global var_eighteen
    global var_nineteen
    global var_twenty

    global score

    clear()

    if add_tail_twenty_one == True:
        field[var_twenty[1][0]][var_twenty[1][1]] = 'О'
        if score < 21:
            score += 1

    if add_tail_twenty == True:
        field[var_nineteen[1][0]][var_nineteen[1][1]] = 'О'
        var_twenty = var_nineteen
        if score < 20:
            score += 1

    if add_tail_nineteen == True:
        field[var_eighteen[1][0]][var_eighteen[1][1]] = 'О'
        var_nineteen = var_eighteen
        if score < 19:
            score += 1

    if add_tail_eighteen == True:
        field[var_seventeen[1][0]][var_seventeen[1][1]] = 'О'
        var_eighteen = var_seventeen
        if score < 18:
            score += 1

    if add_tail_seventeen == True:
        field[var_sixteen[1][0]][var_sixteen[1][1]] = 'О'
        var_seventeen = var_sixteen
        if score < 17:
            score += 1

    if add_tail_sixteen == True:
        field[var_fifteen[1][0]][var_fifteen[1][1]] = 'О'
        var_sixteen = var_fifteen
        if score < 16:
            score += 1

    if add_tail_fifteen == True:
        field[var_fourteen[1][0]][var_fourteen[1][1]] = 'О'
        var_fifteen = var_fourteen
        if score < 15:
            score += 1

    if add_tail_fourteen == True:
        field[var_thirteen[1][0]][var_thirteen[1][1]] = 'О'
        var_fourteen = var_thirteen
        if score < 14:
            score += 1

    if add_tail_thirteen == True:
        field[var_twelve[1][0]][var_twelve[1][1]] = 'О'
        var_thirteen = var_twelve
        if score < 13:
            score += 1

    if add_tail_twelve == True:
        field[var_eleven[1][0]][var_eleven[1][1]] = 'О'
        var_twelve = var_eleven
        if score < 12:
            score += 1

    if add_tail_eleven == True:
        field[var_ten[1][0]][var_ten[1][1]] = 'О'
        var_eleven = var_ten
        if score < 11:
            score += 1

    if add_tail_ten == True:
        field[var_nine[1][0]][var_nine[1][1]] = 'О'
        var_ten = var_nine
        if score < 10:
            score += 1

    if add_tail_nine == True:
        field[var_eight[1][0]][var_eight[1][1]] = 'О'
        var_nine = var_eight
        if score < 9:
            score += 1

    if add_tail_eight == True:
        field[var_seven[1][0]][var_seven[1][1]] = 'О'
        var_eight = var_seven
        if score < 8:
            score += 1

    if add_tail_seven == True:
        field[var_six[1][0]][var_six[1][1]] = 'О'
        var_seven = var_six
        if score < 7:
            score += 1

    if add_tail_six == True:
        field[var_five[1][0]][var_five[1][1]] = 'О'
        var_six = var_five
        if score < 6:
            score += 1

    if add_tail_five == True:
        field[var_four[1][0]][var_four[1][1]] = 'О'
        var_five = var_four
        if score < 5:
            score += 1

    if add_tail_four == True:
        field[var_three[1][0]][var_three[1][1]] = 'О'
        var_four = var_three
        if score < 4:
            score += 1

    if add_tail_three == True:
        field[var_two[1][0]][var_two[1][1]] = 'О'
        var_three = var_two
        if score < 3:
            score += 1

    if add_tail_two == True:
        field[var_one[1][0]][var_one[1][1]] = 'О'
        var_two = var_one
        if score < 2:
            score += 1

    if (head[0][1] - mhr + phr) < 0:
        return 'crash'
    elif (head[0][1] - mhr + phr) > 4:
        return 'crash'
    elif (head[0][0] - mhc + phc) < 0:
        return 'crash'
    elif (head[0][0] - mhc + phc) > 4:
        return 'crash'
    elif field[head[0][0] - mhc + phc][head[0][1] - mhr + phr] != ' ' and field[head[0][0] - mhc + phc][head[0][1] - mhr + phr] != '@':
        return 'crash'
    else:
        field[head[0][0] - mhc + phc][head[0][1] - mhr + phr] = 'X'
        field[body[0][0] - mb1c + pb1c][body[0][1] - mb1r + pb1r] = 'O'
        field[body[1][0] - mb2c + pb2c][body[1][1] - mb2r + pb2r] = 'O'
        if add_tail_one == True:
            field[body[1][0]][body[1][1]] = 'О'
            var_one = body
            if score < 1:
                score += 1
        apple_is_exists()


def eating(head, apple, mhc = 0, mhr = 0, phc = 0, phr = 0):
    """Функция возвращает стороковый литерал, если при то или ином движении змейки координаты головы
    будут равны координатам яблока."""
    if apple != []:
        if apple[0][0] == (head[0][0] - mhc + phc) and apple[0][1] == (head[0][1] - mhr + phr):
            return 'eated'


start_snake()
spawn_apple()
board()
moveing = None

while moveing != 'Quit':
    current_form = define_form(head = head_coordinates_of_snake(), body = body_coordinates_of_snake())
    moveing = input('Use w, a, s or d to move: ')

    if current_form == 'first':
        if moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1r = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1r = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, mb1r = 1, mb2r = 1) == 'crash':
                print(f'Your score is {score}')
                print('Crash!')
                break
            board()

    elif current_form == 'second':
        if moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1r = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1r = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, pb1r = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'third':
        if moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1c = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, mb1c = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1c = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'fourth':
        if moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1c = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1c = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, pb1c = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'eleventh':
        if moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, pb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'twelfth':
        if moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, pb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'ninth':
        if moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, mb1c = 1, pb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'tenth':
        if moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, mb1c = 1, mb2r = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'fifth':
        if moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, pb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'sixth':
        if moveing == 'd':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phr = 1, pb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, pb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, pb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'seventh':
        if moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, mb1r = 1, mb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()

    elif current_form == 'eighth':
        if moveing == 'a':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhr = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhr = 1, mb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 'w':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      mhc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  mhc = 1, mb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()
        elif moveing == 's':
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twenty == True:
                add_tail_twenty_one = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nineteen == True:
                add_tail_twenty = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eighteen == True:
                add_tail_nineteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seventeen == True:
                add_tail_eighteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_sixteen == True:
                add_tail_seventeen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fifteen == True:
                add_tail_sixteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_fourteen == True:
                add_tail_fifteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_thirteen == True:
                add_tail_fourteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_twelve == True:
                add_tail_thirteen = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eleven == True:
                add_tail_twelve = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_ten == True:
                add_tail_eleven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_nine == True:
                add_tail_ten = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_eight == True:
                add_tail_nine = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_seven == True:
                add_tail_eight = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_six == True:
                add_tail_seven = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_five == True:
                add_tail_six = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_four == True:
                add_tail_five = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_three == True:
                add_tail_four = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_two == True:
                add_tail_three = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated' and add_tail_one == True:
                add_tail_two = True
            if eating(head = head_coordinates_of_snake(), apple = apple_coordinates_on_board(),
                      phc = 1) == 'eated':
                add_tail_one = True
            if current_position_of_snake_and_moveing(head = head_coordinates_of_snake(), body = body_coordinates_of_snake(),
                                                  phc = 1, mb1r = 1, pb2c = 1) == 'crash':
                print('Crash!')
                print(f'Your score is {score}')
                break
            board()