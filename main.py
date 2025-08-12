from graphics.gameboard import create_chessboard
from dotenv import load_dotenv
import tkinter as tk

load_dotenv(".env")

def main():
    root = tk.Tk()
    root.title("ChessApp")

    create_chessboard(root)
    root.mainloop()

if __name__ == "__main__":
    main()