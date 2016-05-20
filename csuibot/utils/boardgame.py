# This file is modified from the code off the book Python in Practice by
# Mark Summerfield. Copyright © 2012-13 Qtrac Ltd. All rights reserved.
# This program or module is free software: you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version. It is provided for
# educational purposes and is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.

import itertools


DRAUGHT, PAWN, ROOK, KNIGHT, BISHOP, KING, QUEEN = (
    "DRAUGHT", "PAWN", "ROOK", "KNIGHT", "BISHOP", "KING", "QUEEN")
BLACK, WHITE = ("BLACK", "WHITE")


def console(char, background):
    if char is None:
        return chr(0x2B1B) if background == BLACK else chr(0x2B1C)
    else:
        return char


class AbstractBoard:

    def __init__(self, rows=8, columns=8):
        self.board = [[None for _ in range(columns)] for _ in range(rows)]

    def populate_board(self):
        raise NotImplementedError()

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, BLACK if (y + x) % 2 else WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)


class CheckersBoard(AbstractBoard):

    def __init__(self):
        super().__init__(10, 10)
        self.name = "checkers"
        self.populate_board()

    def populate_board(self):
        def black():
            return create_piece(DRAUGHT, BLACK)

        def white():
            return create_piece(DRAUGHT, WHITE)
        rows = ((None, black()), (black(), None), (None, black()),
                (black(), None),
                (None, None), (None, None),
                (None, white()), (white(), None), (None, white()),
                (white(), None))            # 4 white rows
        self.board = [list(itertools.islice(
            itertools.cycle(squares), 0, len(rows))) for squares in rows]


class ChessBoard(AbstractBoard):

    def __init__(self):
        super().__init__(8, 8)
        self.name = "chess"
        self.populate_board()

    def populate_board(self):
        for row, color in ((0, BLACK), (7, WHITE)):
            for columns, kind in (((0, 7), ROOK), ((1, 6), KNIGHT),
                                  ((2, 5), BISHOP), ((3,), QUEEN),
                                  ((4,), KING)):
                for column in columns:
                    self.board[row][column] = create_piece(kind, color)
        for column in range(8):
            for row, color in ((1, BLACK), (6, WHITE)):
                self.board[row][column] = create_piece(PAWN, color)


class ReversiBoard(AbstractBoard):

    def __init__(self):
        super().__init__(8, 8)
        self.name = "reversi"
        self.populate_board()

    def populate_board(self):
        start_squares = ((3, 3, WHITE), (3, 4, BLACK),
                         (4, 3, BLACK), (4, 4, WHITE))
        for i in range(len(start_squares)):
            row, column, color = start_squares[i]
            self.board[row][column] = create_piece(DRAUGHT, color)

    def __str__(self):
        squares = []
        for y, row in enumerate(self.board):
            for x, piece in enumerate(row):
                square = console(piece, WHITE)
                squares.append(square)
            squares.append("\n")
        return "".join(squares)


def create_piece(kind, color):
    color = "White" if color == WHITE else "Black"
    name = {DRAUGHT: "Draught", PAWN: "ChessPawn", ROOK: "ChessRook",
            KNIGHT: "ChessKnight", BISHOP: "ChessBishop",
            KING: "ChessKing", QUEEN: "ChessQueen"}[kind]
    return globals()[color + name]()


class Piece(str):

    __slots__ = ()

emoji_code = {
    "WhiteDraught": 0x26AA,
    "WhiteChessPawn": 0x1F467,
    "WhiteChessRook": 0x26EA,
    "WhiteChessKnight": 0x1F417,
    "WhiteChessBishop": 0x1F472,
    "WhiteChessKing": 0x1F474,
    "WhiteChessQueen": 0x1F478,

    "BlackDraught": 0x26AB,
    "BlackChessPawn": 0x1F466,
    "BlackChessRook": 0x1F3E4,
    "BlackChessKnight": 0x1F40E,
    "BlackChessBishop": 0x1F473,
    "BlackChessKing": 0x1F468,
    "BlackChessQueen": 0x1F470
}

for name, code in emoji_code.items():
    char = chr(code)
    new = (lambda char: lambda Class: Piece.__new__(Class, char))(char)
    new.__name__ = "__new__"
    Class = type(name, (Piece,), dict(__slots__=(), __new__=new))
    globals()[name] = Class
