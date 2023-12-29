# This is a sample Python script.
import os


class Board:
    def __init__(self):
        self.number_of_singles = 0
        self.number_of_doubles = 0
        self.number_of_triples = 0
        self.number_of_quadras = 0
        self.total_ship_fragments = 20
        self.is_for_shooting = False
        self.board = [
            [' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'],
            ['1', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['2', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['3', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['4', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['5', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['6', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['7', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['8', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['9', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
            ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        ]

    def print_board(self):
        for x in self.board:
            print(x)

    def add_single(self, coords):
        row = decipher_row(coords[1])
        column = decipher_column(coords[0])
        if self.board[row][column] != '#':
            self.board[row][column] = '#'
            self.number_of_singles += 1
        else:
            print("Ship already exists in this coordinate.")
        return self.print_board()

    def add_double(self, coords):
        row1 = decipher_row(coords[1])
        column1 = decipher_column(coords[0])
        row2 = decipher_row(coords[3])
        column2 = decipher_column(coords[2])
        if self.board[row1][column1] != '#' and self.board[row2][column2] != '#':
            self.board[row1][column1] = '#'
            self.board[row2][column2] = '#'
            self.number_of_doubles += 1
        else:
            return "Ship already exists in this coordinate. Please try again."
        return self.print_board()

    def add_triple(self, coords):
        row1 = decipher_row(coords[1])
        column1 = decipher_column(coords[0])
        row2 = decipher_row(coords[3])
        column2 = decipher_column(coords[2])
        row3 = decipher_row(coords[5])
        column3 = decipher_column(coords[4])
        if self.board[row1][column1] != '#' and self.board[row2][column2] != '#' and self.board[row3][column3] != '#':
            self.board[row1][column1] = '#'
            self.board[row2][column2] = '#'
            self.board[row3][column3] = '#'
            self.number_of_triples += 1
        else:
            return "Ship already exists in this coordinate. Please try again."
        return self.print_board()

    def add_quadra(self, coords):
        row1 = decipher_row(coords[1])
        column1 = decipher_column(coords[0])
        row2 = decipher_row(coords[3])
        column2 = decipher_column(coords[2])
        row3 = decipher_row(coords[5])
        column3 = decipher_column(coords[4])
        row4 = decipher_row(coords[7])
        column4 = decipher_column(coords[6])
        if self.board[row1][column1] != '#' and self.board[row2][column2] != '#' and self.board[row3][column3] != '#' and self.board[row4][column4] != '#':
            self.board[row1][column1] = '#'
            self.board[row2][column2] = '#'
            self.board[row3][column3] = '#'
            self.board[row4][column4] = '#'
            self.number_of_quadras += 1
        else:
            return "Ship already exists in this coordinate. Please try again."
        return self.print_board()

    def shoot(self, coords, is_hit = False):
        row = decipher_row(coords[1])
        column = decipher_column(coords[0])
        if self.board[row][column] == '#' or is_hit:
            self.board[row][column] = 'h'
            self.total_ship_fragments -= 1
            if self.total_ship_fragments == 0 and self.is_for_shooting == False:
                return 2
            return 1
        else:
            self.board[row][column] = 'o'
            return 0



# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
class Game:
    is_ended = False
    player1turn = True
    player2turn = False
    player1won = False
    player2won = False
    player1name = ''
    player2name = ''


def validate_coords_single(coords):
    if len(coords) != 2 or len(coords) != 4 or len(coords) != 6 or len(coords) != 8:
        print('Incorrect length of coordinates')
    if len(coords) == 2:
        row = coords[1]
        col = coords[0]
        if (row not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                or col not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
            return False
        else:
            return True

def validate_coords_double(coords):
    if len(coords) == 4:
        row1 = coords[1]
        col1 = coords[0]
        row2 = coords[3]
        col2 = coords[2]
        dec_row1 = decipher_row(row1)
        dec_col1 = decipher_column(col1)
        dec_row2 = decipher_row(row2)
        dec_col2 = decipher_column(col2)
        if (dec_row1 == dec_row2 and (dec_col1 == dec_col2+1 or dec_col1 == dec_col2-1)
                or dec_col1 == dec_col2 and (dec_row1 == dec_row2+1 or dec_row1 == dec_row2-1)):
            if (row1 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row2 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col2 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
                return False
            else:
                return True
        else:
            print('Double Ship has to be on same row or column. Please try again.')
            return False

def validate_coords_triple(coords):
    if len(coords) == 6:
        row1 = coords[1]
        col1 = coords[0]
        row2 = coords[3]
        col2 = coords[2]
        row3 = coords[5]
        col3 = coords[4]
        dec_row1 = decipher_row(row1)
        dec_col1 = decipher_column(col1)
        dec_row2 = decipher_row(row2)
        dec_col2 = decipher_column(col2)
        dec_row3 = decipher_row(row3)
        dec_col3 = decipher_column(col3)
        if (dec_row1 == dec_row2 and (dec_col1 == dec_col2+1 or dec_col1 == dec_col2-1)
                or dec_col1 == dec_col2 and (dec_row1 == dec_row2+1 or dec_row1 == dec_row2-1)
                or dec_row2 == dec_row3 and (dec_col2 == dec_col3+1 or dec_col2 == dec_col3-1)
                or dec_col2 == dec_col3 and (dec_row2 == dec_row3+1 or dec_row2 == dec_row3-1)):
            if (row1 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row2 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col2 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row3 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col3 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
                return False
            else:
                return True
        else:
            print('Triple Ship pieces have to connect on same row or column. Please try again.')
            return False

def validate_coords_quadra(coords):
    if len(coords) == 8:
        row1 = coords[1]
        col1 = coords[0]
        row2 = coords[3]
        col2 = coords[2]
        row3 = coords[5]
        col3 = coords[4]
        row4 = coords[7]
        col4 = coords[6]
        dec_row1 = decipher_row(row1)
        dec_col1 = decipher_column(col1)
        dec_row2 = decipher_row(row2)
        dec_col2 = decipher_column(col2)
        dec_row3 = decipher_row(row3)
        dec_col3 = decipher_column(col3)
        dec_row4 = decipher_row(row4)
        dec_col4 = decipher_column(col4)
        if (dec_row1 == dec_row2 and (dec_col1 == dec_col2+1 or dec_col1 == dec_col2-1)
                or dec_col1 == dec_col2 and (dec_row1 == dec_row2+1 or dec_row1 == dec_row2-1)
                or dec_row2 == dec_row3 and (dec_col2 == dec_col3+1 or dec_col2 == dec_col3-1)
                or dec_col2 == dec_col3 and (dec_row2 == dec_row3+1 or dec_row2 == dec_row3-1)
                or dec_row3 == dec_row4 and (dec_col3 == dec_col4+1 or dec_col3 == dec_col4-1)
                or dec_col3 == dec_col4 and (dec_row3 == dec_row4+1 or dec_row3 == dec_row4-1)):
            if (row1 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col1 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row2 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col2 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row3 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col3 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
                    or row4 not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', 'X']
                    or col4 not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']):
                return False
            else:
                return True
        else:
            print('Quadra Ship pieces have to connect on same row or column. Please try again.')
            return False


def decipher_column(columnLetter):
    row = 0
    if columnLetter == 'A' : row = 1
    if columnLetter == 'B' : row = 2
    if columnLetter == 'C' : row = 3
    if columnLetter == 'D' : row = 4
    if columnLetter == 'E' : row = 5
    if columnLetter == 'F' : row = 6
    if columnLetter == 'G' : row = 7
    if columnLetter == 'H' : row = 8
    if columnLetter == 'I' : row = 9
    if columnLetter == 'J' : row = 10
    return row


def decipher_row(rowLetter):
    row = 0
    if rowLetter == '1' : row = 1
    if rowLetter == '2' : row = 2
    if rowLetter == '3' : row = 3
    if rowLetter == '4' : row = 4
    if rowLetter == '5' : row = 5
    if rowLetter == '6' : row = 6
    if rowLetter == '7' : row = 7
    if rowLetter == '8' : row = 8
    if rowLetter == '9' : row = 9
    if rowLetter == 'X' : row = 10
    return row


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    player1board = Board()
    player1boardShoots = Board()
    player1boardShoots.is_for_shooting = True
    print('=============================================')
    print("SETTING UP PLAYER 1 BOARD")
    print('Enter player 1 name: ')
    Game.player1name = input()
    while player1board.number_of_singles < 4:
        print('PLAYER {}: Please insert data for SINGLE ship (example A1):'.format(Game.player1name))
        inp = input()
        if validate_coords_single(inp):
            player1board.add_single(inp)
        else:
            print("Incorrect ship coordinates")
    while player1board.number_of_doubles < 3:
        print('PLAYER {}: Please insert data for DOUBLE ship (example A1B1):'.format(Game.player1name))
        inp = input()
        if validate_coords_double(inp):
            player1board.add_double(inp)
        else:
            print("Incorrect ship coordinates")
    while player1board.number_of_triples < 2:
        print('PLAYER {}: Please insert data for TRIPLE ship (example A1A2A3):'.format(Game.player1name))
        inp = input()
        if validate_coords_triple(inp):
            player1board.add_triple(inp)
        else:
            print("Incorrect ship coordinates")
    while player1board.number_of_quadras < 1:
        print('PLAYER {}: Please insert data for QUADRA ship (example A1A2A3A4):'.format(Game.player1name))
        inp = input()
        if validate_coords_quadra(inp):
            player1board.add_quadra(inp)
        else:
            print("Incorrect ship coordinates")

    os.system('clear')
    print('=============================================')
    player2board = Board()
    player2boardShoots = Board()
    player2boardShoots.is_for_shooting = True
    print("SETTING UP PLAYER 2 BOARD")
    print('Enter player 2 name: ')
    Game.player2name = input()
    while player2board.number_of_singles < 4:
        print('PLAYER {}: Please insert data for SINGLE ship (example A1):'.format(Game.player2name))
        inp = input()
        if validate_coords_single(inp):
            player2board.add_single(inp)
        else:
            print("Incorrect ship coordinates")
    while player2board.number_of_doubles < 3:
        print('PLAYER {}: Please insert data for DOUBLE ship (example A1B1):'.format(Game.player2name))
        inp = input()
        if validate_coords_double(inp):
            player2board.add_double(inp)
        else:
            print("Incorrect ship coordinates")
    while player2board.number_of_triples < 2:
        print('PLAYER {}: Please insert data for TRIPLE ship (example A1A2A3):'.format(Game.player2name))
        inp = input()
        if validate_coords_triple(inp):
            player2board.add_triple(inp)
        else:
            print("Incorrect ship coordinates")
    while player2board.number_of_quadras < 1:
        print('PLAYER {}: Please insert data for QUADRA ship (example A1A2A3A4):'.format(Game.player2name))
        inp = input()
        if validate_coords_quadra(inp):
            player2board.add_quadra(inp)
        else:
            print("Incorrect ship coordinates")

    os.system('cls' if os.name == 'nt' else 'clear')
    game = Game()
    print('=============================================')
    print('LET THE GAMES BEGIN')

    while game.is_ended is False:
        if game.player1turn:
            player1boardShoots.print_board()
            print('PLAYER {} turn - shoot'.format(Game.player1name))
            shot = input()
            if validate_coords_single(shot):
                game.player1turn = False
                game.player2turn = True
                effect = player2board.shoot(shot)
                if effect == 0:
                    print('missed')
                    player1boardShoots.shoot(shot)
                    player1boardShoots.print_board()
                    print('Press enter to change player.')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                if effect == 1:
                    print('HIT')
                    player1boardShoots.shoot(shot, True)
                    player1boardShoots.print_board()
                    print('Press enter to change player.')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                if effect == 2 or  player2board.total_ship_fragments == 0:
                    Game.is_ended = True
                    Game.player1won = True
            else:
                print('Incorrect shot coordinate. Please try again.')
        if game.player2turn:
            player2boardShoots.print_board()
            print('PLAYER {} turn - shoot'.format(Game.player2name))
            shot = input()
            if validate_coords_single(shot):
                game.player1turn = True
                game.player2turn = False
                effect = player1board.shoot(shot)
                if effect == 0:
                    print('missed')
                    player2boardShoots.shoot(shot)
                    player2boardShoots.print_board()
                    print('Press enter to change player.')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                if effect == 1:
                    print('HIT')
                    player2boardShoots.shoot(shot, True)
                    player2boardShoots.print_board()
                    print('Press enter to change player.')
                    input()
                    os.system('cls' if os.name == 'nt' else 'clear')
                if effect == 2 or player1board.total_ship_fragments == 0:
                    Game.is_ended = True
                    Game.player1won = True
            else:
                print('Incorrect shot coordinate. Please try again.')

    print('=============================================')
    print('END GAME')
    if Game.player1won:
        print('{} WON'.format(Game.player1name))
    else:
        print('{} WON'.format(Game.player2name))

    print('PLAYER 1 BOARD:')
    player1board.print_board()
    print('PLAYER 2 BOARD:')
    player2board.print_board()


