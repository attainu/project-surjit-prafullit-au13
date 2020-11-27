

def parse_input():
    try:
        a, b = input().split()
        a = (8 - int(a[1]), (ord(a[0]) - 97))
        b = (8 - int(b[1]), ord(b[0]) - 97)
        return a, b
    except Exception:
        print("error decoding input. please try again")
        return (-1, -1), (-1, -1)
