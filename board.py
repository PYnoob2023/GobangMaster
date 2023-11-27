# board.py

ROWS = 15
COLS = 15

def create_board():
    """
    创建一个初始为空的游戏棋盘。

    返回:
        list: 二维列表，表示游戏棋盘。
    """
    board = [[0 for _ in range(COLS)] for _ in range(ROWS)]
    return board
