def make_move(board, row, col, player, ROWS, COLS):
    """
    在游戏棋盘上执行玩家的移动。

    参数:
        board (list): 二维列表，表示游戏棋盘。
        row (int): 玩家选择的行索引。
        col (int): 玩家选择的列索引。
        player (int): 玩家标识符，1 代表黑子，2 代表白子。
        ROWS (int): 棋盘的行数。
        COLS (int): 棋盘的列数。

    返回:
        bool: 移动是否成功。成功返回 True，否则返回 False。
    """
    if 0 <= row < ROWS and 0 <= col < COLS and board[row][col] == 0:
        board[row][col] = player
        return True
    return False

def check_win(board, player, ROWS, COLS):
    """
    检查玩家是否获胜。

    参数:
        board (list): 二维列表，表示游戏棋盘。
        player (int): 玩家标识符，1 代表黑子，2 代表白子。
        ROWS (int): 棋盘的行数。
        COLS (int): 棋盘的列数。

    返回:
        bool: 如果玩家获胜，则返回 True，否则返回 False。
    """
    # 检查水平方向
    for i in range(ROWS):
        for j in range(COLS - 4):
            if board[i][j] == player and board[i][j + 1] == player and board[i][j + 2] == player and board[i][j + 3] == player and board[i][j + 4] == player:
                return True

    # 检查垂直方向
    for i in range(ROWS - 4):
        for j in range(COLS):
            if board[i][j] == player and board[i + 1][j] == player and board[i + 2][j] == player and board[i + 3][j] == player and board[i + 4][j] == player:
                return True

    # 检查主对角线方向
    for i in range(ROWS - 4):
        for j in range(COLS - 4):
            if board[i][j] == player and board[i + 1][j + 1] == player and board[i + 2][j + 2] == player and board[i + 3][j + 3] == player and board[i + 4][j + 4] == player:
                return True

    # 检查副对角线方向
    for i in range(ROWS - 4):
        for j in range(4, COLS):
            if board[i][j] == player and board[i + 1][j - 1] == player and board[i + 2][j - 2] == player and board[i + 3][j - 3] == player and board[i + 4][j - 4] == player:
                return True

    return False
