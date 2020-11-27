from army.pieces import Piece


def king_list(x, y):
    return [(x + 1, y), (x + 1, y + 1), (x + 1, y - 1), (x, y + 1), (x, y - 1), (x - 1, y), (x - 1, y + 1),
            (x - 1, y - 1)]


class King(Piece):
    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        return [(xx, yy) for xx, yy in king_list(x, y) if self.no_conflict(board, color, xx, yy)]
