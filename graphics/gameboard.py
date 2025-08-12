from common.darken_hex_color import darken_hex_color
import tkinter as tk
import tkinter.font as tk_font
import os

def create_chessboard(root, rows=8, cols=8, square_size=60):
    heading = tk.Label(
        root,
        bg=os.getenv("LIGHTER_COLOR"),
        fg=os.getenv("DARKER_COLOR"),
        text="TEST",
        font=(tk_font.Font(
            family="Helvetica",
            size=22
        ))
    )
    heading.pack()

    dark_color = darken_hex_color(os.getenv("DARKER_COLOR"))
    board_border = tk.Frame(
        root,
        bg=dark_color,
        highlightbackground=dark_color,
        highlightcolor=dark_color,
        bd=0,
        padx=10, pady=10
    )
    board_border.pack(padx=50, pady=50)
    board_frame = tk.Frame(board_border, bg=dark_color)
    board_frame.pack()

    light_color = os.getenv("LIGHTER_COLOR")
    dark_color = os.getenv("DARKER_COLOR")
    for r in range(rows):
        for c in range(cols):
            color = light_color if (r + c) % 2 == 0 else dark_color
            frame = tk.Frame(
                board_frame,
                width=square_size,
                height=square_size,
                bg=color,
                highlightthickness=0
            )
            frame.grid(row=r, column=c)
            frame.grid_propagate(False)