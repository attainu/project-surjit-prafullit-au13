from army.pieces import Piece


def knight_list(x, y, step1=2, step2=1):
    return [(x + step1, y + step2), (x - step1, y + step2),
            (x + step1, y - step2), (x - step1, y - step2),
            (x + step2, y + step1), (x - step2, y + step1),
            (x + step2, y - step1), (x - step2, y - step1)]


class Knight(Piece):
    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        return [(xx, yy) for xx, yy in knight_list(x, y)
                if self.no_conflict(board, color, xx, yy)]
