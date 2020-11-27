
class Piece:

    def __init__(self, color, name):
        self.name = name
        self.position = None
        self.color = color

    def is_valid(self, start_pos, end_pos, color, board):
        if end_pos in self.available_moves(
                start_pos[0], start_pos[1], board, color):
            return True
        return False

    def __repr__(self):
        return self.name

    def __str__(self):
        return self.name

    def generate_continuous_moves(self, x, y, board, color, intervals):
        answers = []
        for x_int, y_int in intervals:
            x_temp, y_temp = x + x_int, y + y_int
            while self.is_in_bound(x_temp, y_temp):
                target = board.get((x_temp, y_temp), None)
                if target is None:
                    answers.append((x_temp, y_temp))
                elif target.color != color:
                    answers.append((x_temp, y_temp))
                    break
                else:
                    break

                x_temp, y_temp = x_temp + x_int, y_temp + y_int
        return answers

    @staticmethod
    def is_in_bound(x, y):
        if 0 <= x < 8 and 0 <= y < 8:
            return True
        return False

    def no_conflict(self, board, initial_color, x, y):
        if self.is_in_bound(x, y) and (((x, y) not in board) or
                                       board[(x, y)].color != initial_color):
            return True
        return False

    def available_moves(self, x, y, board, color=None):
        pass
