class Ship:

    def __init__(self, length):

        self.__length = length
        self.bow = (0, 0)
        self.horizontal = False
        self.__hit = [False] * length

    def shoot_at(self, coordinates):

        for i in range(self.__length):
            if self.horizontal:
                if (coordinates[0], coordinates[1 + i]) == coordinates:
                    self.__hit[i] = True
                    break
            else:
                if (coordinates[0 + i], coordinates[1]) == coordinates:
                    self.__hit[i] = True
                    break
        if self.__hit == [True] * self.__length:
            return True


class Player:

    def __init__(self, name):
        self.__name = name


    def read_position(self):
        position = input('{}, enter the position:'.format(self.__name))
        while not ('A' <= position[0].upper() <= 'J' and 1 <= position[1] <= 10
                   and position[0].isalpha() and position[1:].isnumeric()):
            position = input('You enterred the incorrect position. Please, try again:')
        posit = (position[1] - 1, ord(position[0]) - ord('A'))
        return posit


def coordin(lst):
    lst1 = []
    for k in lst:
        for m in range(-1, 2):
            for n in range(-1, 2):
                lst1.append((k[0] + m, k[1] + n))
    return lst1


def generate_field():
    import random
    new_board = [[None for i in range(10)] for k in range(10)]
    for length in range(4, 0, -1):
        for ship_count in range(5 - length):
            sh = Ship(length)
            while True:
                i = random.randint(0, 9)
                j = random.randint(0, 9)
                horizontal = random.choice([True, False])
                coords = []
                if horizontal:
                    for x in range(length):
                        coords.append((i, j))
                        j += 1
                else:
                    for x in range(length):
                        coords.append((i, j))
                        i += 1
                for i in coordin(coords):
                    try:
                        if not new_board[i[0]][i[1]] is None:
                            break
                    except IndexError:
                        continue
                else:
                    try:
                        for i in coords:
                            new_board[i[0]][i[1]] = sh
                    except IndexError:
                        continue

                    break
    return new_board


class Field:

    def __init__(self):
        self.__ships = generate_field()
        self.shot = set()
    def shoot_at(self, coordinate):
        if isinstance(self.__ships[coordinate[0]][coordinate[1]], Ship):
            fire = self.__ships[coordinate[0]][coordinate[1]].shoot_at()
            shot.add(coordinate)
            if fire:
                return 'fire'
            return True
        else:
            shot.add(coordinate)
            return False

    def field_without_ships(self):
        str = ''
        for i in range(10):
            for k in range(10):
                if (i, k) in self.shot:
                    if isinstance(self.__ships[i][k], Ship):
                        str += 'X'
                    else:
                        str += 'o'
                else:
                    str += ' '
                str += '\n'
        return str


    def field_with_ships(self):
        str = ''
        for i in range(10):
            for k in range(10):
                if (i, k) in self.shot:
                    if isinstance(self.__ships[i][k], Ship):
                        str += 'X'
                    else:
                        str += 'o'
                else:
                    if isinstance(self.__ships[i][k], Ship):
                        str += '*'
                    else:
                        str += ' '
                str += '\n'
        return str


class Game:

    def __init__(self):
        player1 = input('Enter the name of the first player: ')
        player2 = input('Enter the name of the second player: ')
        self.__players = [Player(player1), Player(player2)]
        self.__fields = [Field(), Field()]
        self.__current_player = 0


    def read_position(self, index):
        return self.__players[index].read_position()


    def field_without_ships(self, index):
        return self.__fields[index].field_without_ships()


    def field_with_ships(self, index):
        return self.__fields[index].field_with_ships()


    def game(self):
        pass
