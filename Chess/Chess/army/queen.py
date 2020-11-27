from army.pieces import Piece
from constants import chess_cardinals, chess_diagonals


class Queen(Piece):
    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        return self.generate_continuous_moves(
            x, y, board, color, chess_cardinals + chess_diagonals)
