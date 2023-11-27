import tkinter as tk
from tkinter import ttk, messagebox
from board import create_board
from game import check_win, make_move
from player import get_player_move

ROWS = 15
COLS = 15
CELL_SIZE = 30

def draw_board(canvas):
    """
    在画布上绘制游戏棋盘。

    参数:
        canvas (tk.Canvas): 游戏棋盘绘制的 Tkinter 画布。
    """
    for i in range(ROWS):
        for j in range(COLS):
            canvas.create_rectangle(j * CELL_SIZE, i * CELL_SIZE, (j + 1) * CELL_SIZE, (i + 1) * CELL_SIZE, fill="#f0d9b5", outline="black")

def draw_stone(canvas, row, col, color):
    """
    在画布上绘制一个棋子。

    参数:
        canvas (tk.Canvas): 棋子绘制的 Tkinter 画布。
        row (int): 棋子的行索引。
        col (int): 棋子的列索引。
        color (str): 棋子的颜色 ("black" 或 "white")。
    """
    canvas.create_oval(col * CELL_SIZE, row * CELL_SIZE, (col + 1) * CELL_SIZE, (row + 1) * CELL_SIZE, fill=color)

def play_game():
    board = create_board()
    current_player = 1
    game_over = False

    def on_click(event):
        """
        鼠标点击画布的事件处理程序。

        参数:
            event (tk.Event): 鼠标点击事件。
        """
        nonlocal current_player, game_over
        if game_over:
            return

        col = event.x // CELL_SIZE
        row = event.y // CELL_SIZE

        if make_move(board, row, col, current_player, ROWS, COLS):
            draw_stone(canvas, row, col, "#000000" if current_player == 1 else "#ffffff")
            if check_win(board, current_player, ROWS, COLS):
                winner = f"玩家{current_player}({('黑' if current_player == 1 else '白')})"
                show_winner(winner)
                return

            current_player = 3 - current_player

    def restart_game():
        """
        通过重置棋盘和 UI 来重新开始游戏。
        """
        nonlocal board, game_over
        canvas.delete("all")
        draw_board(canvas)
        board = create_board()
        game_over = False

    def show_winner(winner):
        """
        显示获胜者并禁用进一步的移动。

        参数:
            winner (str): 指示获胜者的消息。
        """
        nonlocal game_over
        game_over = True
        result = f"{winner}获胜！"
        messagebox.showinfo("游戏结果", result)

    style = ttk.Style()
    style.configure("TButton", padding=10, font=('Helvetica', 12))

    root = tk.Tk()
    root.title("五子棋")
    root.configure(bg='#ececec')

    canvas = tk.Canvas(root, width=COLS * CELL_SIZE, height=ROWS * CELL_SIZE, bg="#f0d9b5", highlightthickness=0)
    canvas.pack()

    restart_button = ttk.Button(root, text="重新开始", command=restart_game, style="TButton")
    restart_button.pack(pady=10)

    canvas.bind("<Button-1>", on_click)
    draw_board(canvas)

    root.mainloop()

if __name__ == "__main__":
    play_game()
