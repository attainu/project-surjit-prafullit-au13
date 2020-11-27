from army.king import King
from army.pawn import Pawn
from army.rook import Rook
from army.bishop import Bishop
from army.queen import Queen
from army.knight import Knight
from constants import *

uniDict = {WHITE: {Pawn: " ♙ ", Rook: " ♖ ", Knight: " ♘ ", Bishop: " ♗ ", King: " ♔ ", Queen: " ♕ "},
           BLACK: {Pawn: " ♟ ", Rook: " ♜ ", Knight: " ♞ ", Bishop: " ♝ ", King: " ♚ ", Queen: " ♛ "}}

initial_Order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]


def is_check(board):
    king = King
    king_dict = {}
    piece_dict = {BLACK: [], WHITE: []}
    for position, piece in board.items():
        if type(piece) == King:
            king_dict[piece.color] = position
        piece_dict[piece.color].append((piece, position))
    # white
    try:
        if can_see_king(board, king_dict[WHITE], piece_dict[BLACK]):
            return False, "White player is in check"
    except KeyError as e:
        return True, "Game End, Black Wins"
    try:
        if can_see_king(board, king_dict[BLACK], piece_dict[WHITE]):
            return False, "Black player is in check"
    except KeyError as e:
        return True, "Game End, white Wins"
    return False, ""
   


def can_see_king(board, king_pos, piece_list):
    for piece, position in piece_list:
        if piece.is_valid(position, king_pos, piece.color, board):
            return True
