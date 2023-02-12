def log_in(input_id, input_pw):
    real_id = ""
    ""
    file = open('log_in.txt', 'r', encoding='utf8')
    lines = file.readlines()
    for line in lines:
        key, value = line.split()
        if '\n' in value:
            value = value.replace('\n', '')
        if key[:-1] == 'ID':
            real_id = value
        else:
            real_pw = value
            if real_id == input_id and real_pw == input_pw:
                return True
    return False


def display_board(board):
    for i in range(3):
        print('-------------')
        print('|', board[i * 3 + 0], '|', board[i * 3 + 1], '|', board[i * 3 + 2], '|')
    print('-------------')


def input_pos(board):
    while True:
        pos = int(input("1부터 9까지 사이의 값을 입력하시오:"))
        if 1 <= pos <= 9:
            if board[pos - 1] == '*':
                return pos - 1
            else:
                print("이미 있는 자리입니다. 다시 입력해주세요")
        else:
            print("범위를 벗어났습니다. 다시 입력해주세요")


def victory(board, player):
    if board[0] == player and board[1] == player and board[2] == player:
        return True

    elif board[3] == player and board[4] == player and board[5] == player:
        return True
    elif board[6] == player and board[7] == player and board[8] == player:
        return True
    elif board[0] == player and board[3] == player and board[6] == player:
        return True
    elif board[1] == player and board[4] == player and board[7] == player:
        return True
    elif board[2] == player and board[5] == player and board[8] == player:
        return True
    elif board[0] == player and board[4] == player and board[8] == player:
        return True
    elif board[2] == player and board[4] == player and board[6] == player:
        return True
    else:
        return False
def random_pos(board):
    import random
    while True:
        pos = random.randint(0, 8)
        if board[pos] == '*':
            return pos


def draw(board):
    if '*' not in board:
        return True
    return False
