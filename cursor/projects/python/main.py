import tkinter as tk
from tkinter import messagebox

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    # 行のチェック
    for row in board:
        if all([cell == player for cell in row]):
            return True
    # 列のチェック
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    # 対角線のチェック
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all([cell != " " for row in board for cell in row])

def tic_tac_toe_gui():
    def on_button_click(row, col):
        nonlocal current_player
        if board[row][col] == " ":
            board[row][col] = current_player
            buttons[row][col].config(text=current_player)
            if check_winner(board, current_player):
                messagebox.showinfo("ゲーム終了", f"プレイヤー {current_player} の勝ちです！")
                root.quit()
            elif is_full(board):
                messagebox.showinfo("ゲーム終了", "引き分けです！")
                root.quit()
            else:
                current_player = "O" if current_player == "X" else "X"
    
    root = tk.Tk()
    root.title("三目並べゲーム")
    
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    buttons = [[None for _ in range(3)] for _ in range(3)]
    
    for row in range(3):
        for col in range(3):
            button = tk.Button(root, text=" ", width=10, height=3,
                               command=lambda r=row, c=col: on_button_click(r, c))
            button.grid(row=row, column=col)
            buttons[row][col] = button
    
    root.mainloop()

if __name__ == "__main__":
    tic_tac_toe_gui()