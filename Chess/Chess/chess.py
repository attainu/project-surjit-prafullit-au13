from utils import uniDict, initial_Order, is_check
from constants import WHITE, BLACK
from board_printer import print_board
from input_parser import parse_input
from army.pawn import Pawn


class Game:
    def __init__(self):
        self.players_turn = BLACK
        self.board = {}
        self.setup_board()
        print("Black will start first.")
        self.start_game()

    def setup_board(self):
        # Arranging first Pawn.
        for i in range(0, 8):
            self.board[(1, i)] = Pawn(WHITE, uniDict[WHITE][Pawn], 1)
            self.board[(6, i)] = Pawn(BLACK, uniDict[BLACK][Pawn], -1)

        for i in range(0, 8):
            self.board[(7, i)] = initial_Order[i](
                BLACK, uniDict[BLACK][initial_Order[i]])
            self.board[(0, (7 - i))] = initial_Order[i](
                WHITE, uniDict[WHITE][initial_Order[i]])

    def start_game(self):
        game_end = False
        while game_end is False:
            print_board(self.board)
            if self.players_turn == BLACK:
                print("Black's turn")
            if self.players_turn == WHITE:
                print("White's turn")
            start_pos, end_pos = parse_input()
            try:
                target = self.board[start_pos]
            except KeyError:
                print("Could not find piece; "
                      "index probably out of range")
                target = None

            if target:
                if target.color != self.players_turn:
                    print("Wait for your turn")
                    continue
                if target.is_valid(start_pos, end_pos, target.color,
                                   self.board):
                    game_end = self.process_valid_move(end_pos, start_pos)
                else:
                    print("Invalid move")
            else:
                print("There is no piece in that space")
        print_board(self.board)

    def process_valid_move(self, end_pos, start_pos):
        self.board[end_pos] = self.board[start_pos]
        del self.board[start_pos]
        game_end = False
        game_end, message = is_check(self.board)
        print(message)
        if self.players_turn == BLACK:
            self.players_turn = WHITE
        else:
            self.players_turn = BLACK
        return game_end


if __name__ == "__main__":
    Game()
