# 简易五子棋

import os

player_chess = {}  # chess of play, dictionary, like {'18', '12'}
computer_chess = {} # chess of computer, dictionary, like {'17', '11'}

chess_board = []

player_play = '0' 
quit_sign = 'bye'  # quit game

def init_board():
    chess_board.append(['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    for i in range (1, 10):
        chess_board.append([str(i), '·', '·', '·', '·', '·', '·', '·', '·', '·'])
def print_board():
    os.system('clear')
    for idx1 in range(len(chess_board)):
        for idx2, v in enumerate(chess_board[idx1]):
            print(v, end=' ')
        print()

def set_player_chess(spot: str):
    x = int(spot[0])
    y = int(spot[1])
    chess_board[x][y] = '◉'
    player_chess[spot] = '1'

def set_computer_chess(spot: str):
    x = int(spot[0])
    y = int(spot[1])
    chess_board[x][y] = '○'
    computer_chess[spot] = '1'

def evaluate_position(x, y, chess_set):
    # 评估某个位置在x或y方向上是否形成四子连珠或更多
    def count_consecutive(dx, dy):
        count = 0
        for i in range(1, 5):
            nx, ny = x + i * dx, y + i * dy
            if 1 <= nx <= 9 and 1 <= ny <= 9 and f"{nx}{ny}" in chess_set:
                count += 1
            else:
                break
        return count

    # 检查四个方向：水平、垂直和两个对角线
    return max(
        count_consecutive(1, 0) + count_consecutive(-1, 0),  # 水平
        count_consecutive(0, 1) + count_consecutive(0, -1),  # 垂直
        count_consecutive(1, 1) + count_consecutive(-1, -1), # 对角线1
        count_consecutive(1, -1) + count_consecutive(-1, 1)  # 对角线2
    )

def find_best_move():
    best_score = -1
    best_move = None
    for x in range(1, 10):
        for y in range(1, 10):
            spot = f"{x}{y}"
            if spot not in player_chess and spot not in computer_chess:
                # 计算当前点对玩家和电脑的影响
                player_score = evaluate_position(x, y, player_chess)
                computer_score = evaluate_position(x, y, computer_chess)
                
                # 优先考虑防守
                if player_score >= 4:
                    return spot
                
                # 再考虑进攻
                if computer_score > best_score:
                    best_score = computer_score
                    best_move = spot
                
    return best_move if best_move else '11'  # 如果无法找到最优位置，默认为'11'

def computer_turn():
    best_move = find_best_move()
    set_computer_chess(best_move)
    
def check_win(spots: dict) -> bool:
    x_s = {} # x轴数相同的棋子: like {'1': [12, 13, 14, 15], '2': [21, 22, 23, 24]}
    y_s = {} # y轴数相同的棋子: like {'1': [11, 21, 31, 41], '2': [12, 22, 32, 42]}
    for k in spots.keys():
        x = int(k[0])
        if x not in x_s:
            x_s[x] = [int(k)]
        else:
            x_s[x].append(int(k))
        # 判断是否有连续的 5 个数字
        if len(x_s[x]) == 5 and x_s[x][4] - x_s[x][0] == 4:
            return True

        y = int(k[1])
        if y not in y_s:
            y_s[y] = [int(k)]
        else:
            y_s[y].append(int(k))
        # 判断是否有连续的 5 个数字
        if len(y_s[y]) == 5 and y_s[y][4] - y_s[y][0] == 40:
            return True


########## run ##########
init_board()
print_board()

while player_play != quit_sign:
    pp = int(player_play)
    if pp < 11 or pp > 99:
        print('请输入合法的下棋的位置：[11 ~ 99]')
    else:
        set_player_chess(player_play)
        if check_win(player_chess):
            print('玩家赢了')
            break
        computer_turn()
        if check_win(computer_chess):
            print('电脑赢了')
            break
        print_board()

    player_play = input('请输入下棋的位置：')
