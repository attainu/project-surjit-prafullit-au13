from army.pieces import Piece


class Pawn(Piece):
    def __init__(self, color, name, direction):
        super().__init__(color, name)
        self.direction = direction

    def available_moves(self, x, y, board, color=None):
        if color is None:
            color = self.color
        answers = []
        if (x + self.direction, y + 1) in board and \
                self.no_conflict(board, color, x + self.direction, y + 1):
            answers.append((x + self.direction, y + 1))

        if (x - self.direction, y - 1) in board and \
                self.no_conflict(board, color, x + self.direction, y - 1):
            answers.append((x - self.direction, y - 1))

        if (x + self.direction, y) not in board and color == self.color:
            answers.append((x + self.direction, y))

        if x == 1 or x == 6:
            if (x + self.direction + self.direction, y) not in board and \
                    self.is_in_bound(
                        x + self.direction + self.direction, y) and \
                    color == self.color:
                answers.append((x + self.direction + self.direction, y))
        return answers
