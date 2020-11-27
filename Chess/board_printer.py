from color import Colors


def print_board(board):
    mat = [[" " for i in range(8)] for j in range(8)]

    for i in range(0, 8):
        for j in range(0, 8):
            try:
                mat[i][j] = str(board[(i, j)])
            except KeyError:
                mat[i][j] = "   "
    print_colored_board(mat)


def green_black(i, _):
    print(Colors.Background.green, end="")
    print(Colors.Foreground.black, end="")
    print(i[_], end=" ")


def grey_black(i, _):
    print(Colors.Background.grey, end="")
    print(Colors.Foreground.black, end="")
    print(i[_], end=" ")


def print_colored_board(board):
    num = 8
    a = [" a ", " b ", " c ", " d ", " e ", " f ", " g ", " h "]
    print("    ", end="")
    for i in a:
        print(Colors.Foreground.green, end="")
        print(i, end=" ")
    print(Colors.reset)
    j = 0
    for i in board:
        print(Colors.Foreground.cyan, num, Colors.reset, end=" ")
        if j % 2 == 0:
            for _ in range(len(i)):
                if _ % 2 == 0:
                    green_black(i, _)
                else:
                    grey_black(i, _)
            print(Colors.reset, end="")
            print(Colors.Foreground.cyan, num, Colors.reset)
        else:
            for _ in range(len(i)):
                if _ % 2 == 0:
                    grey_black(i, _)
                else:
                    green_black(i, _)
            print(Colors.reset, end="")
            print(Colors.Foreground.cyan, num, Colors.reset)
        j += 1
        num -= 1

    print("    ", end="")
    for i in a:
        print(Colors.Foreground.green, end="")
        print(i, end=" ")
    print()
    print(Colors.reset)
