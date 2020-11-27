from army.pieces import Piece


def knight_list(x, y, int1, int2):
    return [(x + int1, y + int2), (x - int1, y + int2), (x + int1, y - int2), (x - int1, y - int2),
            (x + int2, y + int1), (x - int2, y + int1), (x + int2, y - int1), (x - int2, y - int1)]


class Knight(Piece):
    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        return [(xx, yy) for xx, yy in knight_list(x, y, 2, 1) if self.no_conflict(board, color, xx, yy)]
