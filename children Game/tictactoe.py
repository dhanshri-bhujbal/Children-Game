import tkinter as tk
from PIL import Image, ImageTk
import random
import main_menu  # Import the main_menu module

class TicTacToe:
    BOARD_SIZE = 3

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Single Player Tic Tac Toe")
        self.root.attributes("-fullscreen", True)

        self.bg_photo = None  # Initialize bg_photo attribute to None

        self.initialize_board()

    def initialize_board(self):
        self.load_background_image()

        self.frame = tk.Frame(self.root, bg="#2c3e50")
        self.frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

        self.buttons = [[None] * TicTacToe.BOARD_SIZE for _ in range(TicTacToe.BOARD_SIZE)]
        self.user_turn = True
        self.xState = [0] * (TicTacToe.BOARD_SIZE ** 2)
        self.oState = [0] * (TicTacToe.BOARD_SIZE ** 2)
        self.moves_made = 0

        for row in range(TicTacToe.BOARD_SIZE):
            for col in range(TicTacToe.BOARD_SIZE):
                button_config = {
                    "text": "",
                    "width": 10,
                    "height": 3,
                    "font": ("Comic Sans MS", 24, "bold"),
                    "command": lambda row=row, col=col: self.button_click(row, col),
                    "bg": "#3498db",
                    "fg": "#ffffff",
                    "highlightbackground": "#2c3e50",
                    "highlightthickness": 5,
                    "bd": 0
                }
                self.buttons[row][col] = tk.Button(self.frame, **button_config)
                self.buttons[row][col].grid(row=row, column=col, padx=5, pady=5)

        self.x_color = "#e74c3c"
        self.o_color = "#f1c40f"

        self.status_label = tk.Label(self.root, text="", font=("Comic Sans MS", 36, "bold"), fg="#ffffff", bg="#3498db", padx=20, pady=10)
        self.restart_button = tk.Button(self.root, text="Restart", width=8, height=2,
                                        font=("Comic Sans MS", 12, "bold"), command=self.reset_game, bg="#2ecc71", fg="#ffffff")
        self.restart_button.place(relx=0.95, rely=0.95, anchor=tk.SE)

        self.back_button = tk.Button(self.root, text="Back", width=8, height=2,
                                     font=("Comic Sans MS", 12, "bold"), command=self.back_to_menu, bg="#e74c3c", fg="#ffffff")
        self.back_button.place(relx=0.05, rely=0.95, anchor=tk.SW)

        self.frame.update_idletasks()
        width = self.frame.winfo_width()
        height = self.frame.winfo_height()
        x_offset = (self.root.winfo_screenwidth() - width) // 2
        y_offset = (self.root.winfo_screenheight() - height) // 2
        self.root.geometry(f'{width}x{height}+{x_offset}+{y_offset}')

    def load_background_image(self):
        try:
            bg_image = Image.open("tictactoe.jpg")
            bg_image = bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.BICUBIC)
            self.bg_photo = ImageTk.PhotoImage(bg_image)
            bg_label = tk.Label(self.root, image=self.bg_photo)
            bg_label.image = self.bg_photo  # Keep a reference to prevent garbage collection
            bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        except FileNotFoundError:
            print("Error: Couldn't find background image. Make sure the file path is correct and the image file exists.")

    def button_click(self, row, col):
        if self.user_turn and self.xState[row * TicTacToe.BOARD_SIZE + col] == 0 and self.oState[row * TicTacToe.BOARD_SIZE + col] == 0:
            self.update_button(row, col, self.x_color, 'X')
            self.xState[row * TicTacToe.BOARD_SIZE + col] = 1
            self.user_turn = False
            self.moves_made += 1

            winner = self.check_win()
            if winner:
                self.display_status(f"{winner} Won the match!")
                self.show_restart_button()
            elif self.moves_made == TicTacToe.BOARD_SIZE ** 2:
                self.display_status("It's a draw!")
                self.show_restart_button()
            else:
                self.computer_move()

    def computer_move(self):
        empty_cells = [(row, col) for row in range(TicTacToe.BOARD_SIZE) for col in range(TicTacToe.BOARD_SIZE)
                       if self.xState[row * TicTacToe.BOARD_SIZE + col] == 0 and self.oState[row * TicTacToe.BOARD_SIZE + col] == 0]

        if empty_cells:
            row, col = random.choice(empty_cells)
            self.update_button(row, col, self.o_color, 'O')
            self.oState[row * TicTacToe.BOARD_SIZE + col] = 1
            self.user_turn = True
            self.moves_made += 1

            winner = self.check_win()
            if winner:
                self.display_status(f"{winner} Won the match!")
                self.show_restart_button()
            elif self.moves_made == TicTacToe.BOARD_SIZE ** 2:
                self.display_status("It's a draw!")
                self.show_restart_button()

    def update_button(self, row, col, bg_color, text):
        self.buttons[row][col].config(text=text, state="disabled", font=("Comic Sans MS", 24, "bold"),
                                      bg=bg_color, fg="#ffffff")

    def check_win(self):
        wins = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8],
                [0, 4, 8], [2, 4, 6]]
        for win in wins:
            if self.xState[win[0]] == self.xState[win[1]] == self.xState[win[2]] == 1:
                return 'X'
            if self.oState[win[0]] == self.oState[win[1]] == self.oState[win[2]] == 1:
                return 'O'
        return None

    def display_status(self, message):
        if message:
            self.status_label.config(text=message)
            self.status_label.pack(side=tk.TOP, fill=tk.X)
        else:
            self.status_label.pack_forget()

    def show_restart_button(self):
        self.restart_button.place(relx=0.95, rely=0.95, anchor=tk.SE)
    
    def reset_game(self):
        self.display_status("")
        self.user_turn = True
        self.xState = [0] * (TicTacToe.BOARD_SIZE ** 2)
        self.oState = [0] * (TicTacToe.BOARD_SIZE ** 2)
        self.moves_made = 0

        for row in range(TicTacToe.BOARD_SIZE):
            for col in range(TicTacToe.BOARD_SIZE):
                self.buttons[row][col].config(text="", state="active", font=("Comic Sans MS", 24, "bold"),
                                              bg="#3498db")

    def back_to_menu(self):
        self.root.destroy()  # Destroy the game window
        main_menu.show_menu()  # Show the main menu

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
