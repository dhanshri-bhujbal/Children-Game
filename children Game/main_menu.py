import tkinter as tk
from PIL import Image, ImageTk
import typing_game
import math_games
from tictactoe import TicTacToe
import help_module

class MainMenu:
    def __init__(self, root):
        self.root = root
        self.root.title("Fun Learning Menu")
        self.root.attributes('-fullscreen', True)
        
        self.canvas = tk.Canvas(self.root, width=self.root.winfo_screenwidth(), height=self.root.winfo_screenheight())
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.background_photo_resized = None
        self.background_label = None
        
        self.load_background_image()

    def load_background_image(self):
        try:
            self.background_image = Image.open("typing_menu_background.jpg")
            self.background_photo_resized = ImageTk.PhotoImage(self.background_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight())))
            print("Background image loaded successfully.")
            self.create_widgets()  # Call create_widgets after loading the background image
        except FileNotFoundError as e:
            print("Background image not found:", e)
        except Exception as e:
            print("Error loading background image:", e)

    def create_widgets(self):
        self.background_label = tk.Label(self.root, image=self.background_photo_resized)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        print("Background label created.")

        center_x = self.root.winfo_screenwidth() // 2
        center_y = self.root.winfo_screenheight() // 2

        # Title Label
        title_label = tk.Label(self.root, text="Welcome to Fun Learning!", font=("Times New Roman", 100, "bold"), fg="#4CAF50", bg="white")
        title_label.place(x=center_x, y=center_y - 300,width=500, height=100, anchor=tk.CENTER)
        print("Title label created.")

        # Typing Game Button
        typing_button = tk.Button(self.root, text="Typing Game", font=("Times New Roman", 40,"bold"), bg="#FF4081", fg="white",
                                  activebackground="#FF80AB", activeforeground="white", width=12, height=2, command=self.start_typing_game)
        typing_button.place(x=center_x, y=center_y - 50, anchor=tk.CENTER)
        print("Typing game button created.")

        # Math Games Button
        math_button = tk.Button(self.root, text="Math Games", font=("Times New Roman", 40,"bold"), bg="#2196F3", fg="white",
                                activebackground="#64B5F6", activeforeground="white",width=12, height=2, command=self.start_math_games)
        math_button.place(x=center_x, y=center_y + 100, anchor=tk.CENTER)
        print("Math games button created.")

        # Tic Tac Toe Button
        tic_tac_toe_button = tk.Button(self.root, text="Tic Tac Toe", font=("Times New Roman",40,"bold"), bg="#FF5722", fg="white",
                                        activebackground="#FF8A65", activeforeground="white",width=12, height=2, command=self.start_tic_tac_toe)
        tic_tac_toe_button.place(x=center_x, y=center_y + 250, anchor=tk.CENTER)
        print("Tic Tac Toe button created.")

        # Help Button
        help_button = tk.Button(self.root, text="Help", font=("Times New Roman", 40,"bold"), bg="#FFEB3B", fg="black",
                                activebackground="#FFD600", activeforeground="black", width=12, height=2, command=help_module.display_help)
        help_button.place(x=50, y=self.root.winfo_screenheight() - 50, anchor=tk.SW)
        print("Help button created.")

        # Exit Button
        exit_button = tk.Button(self.root, text="Exit", font=("Times New Roman", 40,"bold"), bg="#F44336", fg="black",
                                activebackground="#EF5350", activeforeground="black", width=12, height=2, command=self.exit_application)
        exit_button.place(x=self.root.winfo_screenwidth() - 50, y=self.root.winfo_screenheight() - 50, anchor=tk.SE)
        print("Exit button created.")

    def start_typing_game(self):
        self.root.destroy()
        typing_game.start_typing_game()

    def start_math_games(self):
        self.root.destroy()
        math_games.create_math_games_screen()

    def start_tic_tac_toe(self):
        self.root.destroy()
        tic_tac_toe_game = TicTacToe()
        tic_tac_toe_game.run()

    def exit_application(self):
        self.root.destroy()

def show_menu():
    root = tk.Tk()
    MainMenu(root)
    root.mainloop()

if __name__ == "__main__":
    show_menu()