# player.py

def get_player_move():
    """
    获取玩家的移动输入。

    返回:
        tuple: 包含玩家输入的行和列索引。
    """
    row = int(input("请输入行号: ")) - 1
    col = int(input("请输入列号: ")) - 1
    return row, col
