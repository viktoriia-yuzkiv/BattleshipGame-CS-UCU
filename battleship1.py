class Ship:

    def __init__(self, length):
        self.__length = length
        self.bow = (0, 0)
        self.horizontal = False
        self.__hit = [False] * length

    def shoot_at(self, coordinates):
        """
        Reflects that in the class Ship an opponent destroyed the
        relevant part of the ship.
        """
        for i in range(self.__length):
            if self.horizontal:
                if (self.bow[0], self.bow[1] + i) == coordinates:
                    self.__hit[i] = True
                    break
            else:
                if (self.bow[0] + i, self.bow[1]) == coordinates:
                    self.__hit[i] = True
                    break
        if self.__hit == [True] * self.__length:
            return True
        else:
            return False


class Player:

    def __init__(self, name):
        self.__name = name

    def read_position(self):
        """
        Reads coordinates of a player shot and converts them into
        the nedeed type.
        """
        position = input('{}, enter the position: '.format(self.__name))
        try:
            while not ('A' <= position[0].upper() <= 'J' and
                       1 <= int(position[1:]) <= 10 and
                       position[0].isalpha() and position[1:].isnumeric()):
                position = input('You entered the incorrect position. \
Please, try again: ')
        except:
            return self.read_position()
        posit = (int(position[1:]) - 1, ord(position[0].upper()) - ord('A'))
        return posit

    def __str__(self):
        return self.__name


def coordin(lst):
    """
    This function is used in the function generate_field.
    It creates a list of tuples with coordinates of given ship and
    cells around it. Returns this list.
    """
    lst1 = []
    for k in lst:
        for m in range(-1, 2):
            for n in range(-1, 2):
                lst1.append((k[0] + m, k[1] + n))
    return lst1


def generate_field():
    """
    Generates a random field.
    """
    import random
    new_board = [[None for _ in range(10)] for _ in range(10)]
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
        """

        """
        if isinstance(self.__ships[coordinate[0]][coordinate[1]], Ship):
            fire = self.__ships[coordinate[0]][
                                coordinate[1]].shoot_at(coordinate)
            self.shot.add(coordinate)
            return 'You have hit.'
        else:
            self.shot.add(coordinate)
            return 'You have missed.'

    def field_without_ships(self):
        """

        """
        without_ships = '  A B C D E F G H I J\n'
        for i in range(10):
            without_ships += str(i + 1)
            if i < 9:
                without_ships += ' '
            for k in range(10):
                if (i, k) in self.shot:
                    if isinstance(self.__ships[i][k], Ship):
                        without_ships += 'X '
                    else:
                        without_ships += 'o '
                else:
                    without_ships += '  '
            without_ships += '|\n'
        return without_ships

    def field_with_ships(self):
        """

        """
        with_ships = '  A B C D E F G H I J\n'
        for i in range(10):
            with_ships += str(i + 1)
            if i < 9:
                with_ships += ' '
            for k in range(10):
                if (i, k) in self.shot:
                    if isinstance(self.__ships[i][k], Ship):
                        with_ships += 'X '
                    else:
                        with_ships += 'o '
                else:
                    if isinstance(self.__ships[i][k], Ship):
                        with_ships += '* '
                    else:
                        with_ships += '  '
                    with_ships += '|\n'
        return with_ships


class Game:

    def __init__(self):
        player1 = input('Enter the name of the first player: ')
        player2 = input('Enter the name of the second player: ')
        self.__players = [Player(player1), Player(player2)]
        self.__fields = [Field(), Field()]
        self.__current_player = 0
        self.__score = [0, 0]
        self.game()

    def read_position(self, index):
        """

        """
        return self.__players[index].read_position()

    def game(self):
        """

        """
        while not self.__score[0] == 20 or self.__score[1] == 20:
            if self.__current_player == 0:
                field_index = 1
            else:
                field_index = 0
            print(self.__players[field_index], end=' field\n')
            print(self.__fields[field_index].field_without_ships())
            pos = self.read_position(self.__current_player)
            shot = self.__fields[field_index].shoot_at(pos)
            print(shot)
            print('\n')
            if shot != 'You have missed.':
                self.__score[self.__current_player] += 1
                if self.__score[self.__current_player] == 20:
                    print(self.__players[self.__current_player], end=' win\n')
                    print(self.__players[field_index], end=' lose\n')
                    break
            else:
                self.__current_player += 1
                if self.__current_player == 2:
                    self.__current_player = 0

Game()
