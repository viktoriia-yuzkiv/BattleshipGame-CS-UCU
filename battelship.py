def read_file(filename):
    """

    (str) -> (list)

    Reads the field from a file and converts it into a list of lists.

    """
    my_lst = []
    with open(filename, 'r') as file:
        field = file.readlines()
    for i in field:
        if '\n' in i:
            m = list(i.replace('\n', ''))
            for n in range(10-len(m)):
                m.append(' ')
            my_lst.append(m)
        else:
            m = list(i)
            for n in range(10-len(m)):
                m.append(' ')
            my_lst.append(m)
    return my_lst


def has_ship(field, coordinates):
    """

    (list, tuple) -> (bool)

    Uses a list of lists (field) and coordinates of the needed element and
    verify if there is a ship with asked coordinates in that field.
    Returns True or False.

    """
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if '*' in field[coordinates[1] - 1][letters.index(coordinates[0].upper())]:
        return True
    else:
        return False


def ship_size(field, coordinates):
    """

    (list, tuple) -> (int)

    Uses a list of lists (field) and coordinates of the needed element.
    Return the size of a ship, coordinates of a part of which are given.

    """
    len1 = 0
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    if has_ship(field, coordinates) is False:
        return len1
    else:
        len2 = 1
        i = 1
        while True:
            try:
                if '*' in field[coordinates[1] - 1][letters.index(
                        coordinates[0].upper()) + i]:
                    len2 += 1
                    i += 1
                else:
                    break
            except:
                break
        i = 1
        while True:
            try:
                if '*' in field[coordinates[1] - 1][letters.index(
                        coordinates[0].upper()) - i]:
                    len2 += 1
                    i += 1
                else:
                    break
            except:
                break
        i = 1
        while True:
            try:
                if '*' in field[coordinates[1] - 1 + i][letters.index(
                        coordinates[0].upper())]:
                    len2 += 1
                    i += 1
                else:
                    break
            except:
                break
        i = 1
        while True:
            try:
                if '*' in field[coordinates[1] - 1 - i][letters.index(
                        coordinates[0].upper())]:
                    len2 += 1
                    i += 1
                else:
                    break
            except:
                break
    return len2


def is_valid(field):
    """

    (list) -> (bool)

    Uses a list of lists. Determinates if given field is valid.
    Returns True or False.

    """
    if len(field) != 10:
        return False
    lst = [0, 0, 0, 0]
    for i in field:
        if len(i) != 10:
            return False
    for k in range(len(field)):
        for m in range(len(field[k])):
            if has_ship(field, (chr(m + 65), k + 1)):
                length = ship_size(field, (chr(m + 65), k + 1))
                if length > 4:
                    return False
                lst[length - 1] += 1
    for i in range(len(lst)):
        lst[i] /= i + 1
    if lst != [4, 3, 2, 1]:
        return False
    return True


def field_to_str(field):
    """

    (list) -> (str)

    Converts a list of lists into a string. Returns a string.

    """
    a = ''
    for i in range(10):
        for k in range(10):
            a += field[i][k]
        a += '\n'
    return a


def generate_field():
    """

    () -> (list)

    Generates new field. Returns a list of lists.

    """
    import random
    new_board = [[' ' for i in range(10)] for k in range(10)]
    num = random.randint(1, 2)
    position1_4 = random.randint(0, 9)
    position2_4 = random.randint(0, 9)
    if num == 1:
        if position1_4 < 5:
            for i in range(4):
                new_board[position2_4][position1_4 + i] = '*'
        elif position1_4 >= 5:
            for i in range(4):
                new_board[position2_4][position1_4 - i] = '*'
    elif num == 2:
        if position2_4 < 5:
            for i in range(4):
                new_board[position2_4 + i][position1_4] = '*'
        elif position2_4 >= 5:
            for i in range(4):
                new_board[position2_4 - i][position1_4] = '*'
    my_board = paint_out_ship(new_board)
    for numm in range(2):
        while True:
            posit1_3 = random.randint(0, 9)
            position2_3 = random.randint(0, 9)
            if my_board[position2_3][posit1_3] == ' ':
                my_board[position2_3][posit1_3] = '*'
                num1 = random.randint(1, 2)
                if num1 == 1:
                    if posit1_3 < 6 and posit1_3 > 4:
                        if my_board[position2_3][posit1_3 + 1] == ' '\
                                and my_board[position2_3][
                                            posit1_3 + 2] == ' ':
                            my_board[position2_3][posit1_3 + 1] = '*'
                            my_board[position2_3][posit1_3 + 2] = '*'
                        elif my_board[position2_3][posit1_3 + 1] == ' '\
                                and my_board[position2_3][
                                            posit1_3 - 1] == ' ':
                            my_board[position2_3][posit1_3 + 1] = '*'
                            my_board[position2_3][posit1_3 - 1] = '*'
                        elif my_board[position2_3][posit1_3 - 1] == ' '\
                                and my_board[position2_3][
                                            posit1_3 - 2] == ' ':
                            my_board[position2_3][posit1_3 - 1] = '*'
                            my_board[position2_3][posit1_3 - 2] = '*'
                        else:
                            pass
                    elif posit1_3 <= 4:
                        if my_board[position2_3][posit1_3 + 1] == ' '\
                               and my_board[position2_3][
                                           posit1_3 + 2] == ' ':
                            my_board[position2_3][posit1_3 + 1] = '*'
                            my_board[position2_3][posit1_3 + 2] = '*'
                        else:
                            pass
                    elif posit1_3 >= 6:
                        if my_board[position2_3][posit1_3 - 1] == ' '\
                               and my_board[position2_3][
                                           posit1_3 - 2] == ' ':
                            my_board[position2_3][posit1_3 - 1] = '*'
                            my_board[position2_3][posit1_3 - 2] = '*'
                        else:
                            pass
                else:
                    if position2_3 < 6 and position2_3 > 4:
                        if my_board[position2_3 + 1][posit1_3] == ' '\
                                and my_board[position2_3 + 2][
                                            posit1_3] == ' ':
                            my_board[position2_3 + 1][posit1_3] = '*'
                            my_board[position2_3 + 2][posit1_3] = '*'
                        elif my_board[position2_3 + 1][posit1_3] == ' '\
                                and my_board[position2_3 - 1][
                                            posit1_3] == ' ':
                            my_board[position2_3 + 1][posit1_3] = '*'
                            my_board[position2_3 - 1][posit1_3] = '*'
                        elif my_board[position2_3 - 1][posit1_3] == ' '\
                                and my_board[position2_3 - 2][
                                            posit1_3] == ' ':
                            my_board[position2_3 - 1][posit1_3] = '*'
                            my_board[position2_3 - 2][posit1_3] = '*'
                        else:
                            pass
                    elif position2_3 <= 4:
                        if my_board[position2_3 + 1][posit1_3] == ' '\
                               and my_board[position2_3 + 2][
                                    posit1_3] == ' ':
                            my_board[position2_3 + 1][posit1_3] = '*'
                            my_board[position2_3 + 2][posit1_3] = '*'
                        else:
                            pass
                    elif position2_3 >= 6:
                        if my_board[position2_3 - 1][posit1_3] == ' '\
                               and my_board[position2_3 - 2][
                                    posit1_3] == ' ':
                            my_board[position2_3 - 1][posit1_3] = '*'
                            my_board[position2_3 - 2][posit1_3] = '*'
                my_board = paint_out_ship(my_board)
                break
            else:
                continue
    for numm in range(3):
        while True:
            position1_2 = random.randint(0, 9)
            position2_2 = random.randint(0, 9)
            if my_board[position2_2][position1_2] == ' ':
                my_board[position2_2][position1_2] = '*'
                num1 = random.randint(1, 2)
                if num1 == 1:
                    if position1_2 < 8 and position1_2 > 1:
                        if my_board[position2_2][position1_2 + 1] == ' ':
                            my_board[position2_2][position1_2 + 1] = '*'
                        elif my_board[position2_2][position1_2 - 1] == ' ':
                            my_board[position2_2][position1_2 - 1] = '*'
                        else:
                            pass
                    elif position1_2 <= 1:
                        if my_board[position2_2][position1_2 + 1] == ' ':
                            my_board[position2_2][position1_2 + 1] = '*'
                        else:
                            pass
                    elif position1_2 >= 8:
                        if my_board[position2_2][position1_2 - 1] == ' ':
                            my_board[position2_2][position1_2 - 1] = '*'
                        else:
                            pass
                else:
                    if position2_2 < 8 and position2_2 > 1:
                        if my_board[position2_2 + 1][position1_2] == ' ':
                            my_board[position2_2 + 1][position1_2] = '*'
                        elif my_board[position2_2 - 1][position1_2] == ' ':
                            my_board[position2_2 - 1][position1_2] = '*'
                        else:
                            pass
                    elif position2_2 <= 1:
                        if my_board[position2_2 + 1][position1_2] == ' ':
                            my_board[position2_2 + 1][position1_2] = '*'
                        else:
                            pass
                    elif position2_2 >= 8:
                        if my_board[position2_2 - 1][position1_2] == ' ':
                            my_board[position2_2 - 1][position1_2] = '*'
                        else:
                            pass
                my_board = paint_out_ship(my_board)
                break
            else:
                continue
    for numm in range(4):
        while True:
            position1_1 = random.randint(0, 9)
            position2_1 = random.randint(0, 9)
            if my_board[position2_1][position1_1] == ' ':
                my_board[position2_1][position1_1] = '*'
                my_board = paint_out_ship(my_board)
                break
            else:
                continue
    for i in range(len(my_board)):
        for k in range(len(my_board[i])):
            my_board[i][k] = my_board[i][k].replace('-', ' ')
    if not is_valid(my_board):
        return generate_field()
    return my_board


def paint_out_ship(board):
    """
    (list) -> (list)

    Paints cellules around ships.

    """
    for i in range(len(board)):
        for k in range(len(board[i])):
            if board[i][k] == '*':
                if i + 1 < 10 and board[i + 1][k] == ' ':
                    board[i + 1][k] = '-'
                if i - 1 >= 0 and board[i - 1][k] == ' ':
                    board[i - 1][k] = '-'
                if k + 1 < 10 and board[i][k + 1] == ' ':
                    board[i][k + 1] = '-'
                if k - 1 >= 0 and board[i][k - 1] == ' ':
                    board[i][k - 1] = '-'
                if i + 1 < 10 and k + 1 < 10 and board[i + 1][k] == '-'\
                        and board[i][k + 1] == '-':
                    board[i + 1][k + 1] = '-'
                if i - 1 >= 0 and k - 1 >= 0 and board[i - 1][k] == '-'\
                        and board[i][k - 1] == '-':
                    board[i - 1][k - 1] = '-'
                if k - 1 >= 0 and i + 1 < 10 and board[i][k - 1] == '-'\
                        and board[i + 1][k] == '-':
                    board[i + 1][k - 1] = '-'
                if i - 1 >= 0 and k + 1 < 10 and board[i - 1][k] == '-'\
                        and board[i][k + 1] == '-':
                    board[i - 1][k + 1] = '-'
    return board
