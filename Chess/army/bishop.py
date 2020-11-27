from army.pieces import Piece
from constants import *


class Bishop(Piece):
    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        return self.generate_continuous_moves(x, y, board, color, chess_diagonals)
