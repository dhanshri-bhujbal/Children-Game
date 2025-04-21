import tkinter as tk
from PIL import Image, ImageTk

def display_help():
    # Create the main window
    root = tk.Toplevel()
    root.title("VIVIDH GAMES Help")
    root.attributes('-fullscreen', True)

    # Load the background image and get screen dimensions
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    background_image = Image.open("help.jpg")
    background_image = background_image.resize((screen_width, screen_height))

    # Convert the image to a PhotoImage for displaying in Tkinter
    background_photo = ImageTk.PhotoImage(background_image)

    # Display the background image
    background_label = tk.Label(root, image=background_photo)
    background_label.image = background_photo
    background_label.pack(fill=tk.BOTH, expand=True)

    # Text content
    text_content = """
    Welcome to VIVIDH GAMES! 

    1. TYPING:
    The objective is to correctly type the falling letters before they reach the bottom of the screen. 
    Use your keyboard to type the letters displayed on the falling bricks and press "Enter" after each word. 
    You earn points for each correct word, but typing a wrong word decreases your lives by 1 (starting with 3 lives).
    If you lose all your lives, the game will ask if you want to restart. Stay focused, type quickly and accurately, 
    and enjoy improving your typing skills!

    2. MATHEMATICS:
    Get ready to have fun while improving your math skills! In these games, 
    you'll be challenged with addition, subtraction, and multiplication problems. 
    For each correct answer, you'll earn points, but be careful! 
    If you provide an incorrect answer, you'll lose a life. You start with 3 lives, and if you lose them all, 
    the game will be over, but don't worry – you can always restart and try again! 
    So, get ready to solve some math problems and enjoy the excitement of learning math in a playful way!

    3. FUN AND MORE:
    Tic Tac Toe is a classic game played on a 3x3 grid where players take turns placing Xs or Os. 
    The objective is to be the first to form a horizontal, vertical, or diagonal line of three of your marks. 
    To win, strategically control the center, block your opponent's moves, and look for patterns to anticipate 
    and create winning combinations. The game ends in a draw if the grid is full without a winner. 
    Enjoy the challenge and have fun playing
    """

    # Create a label for text content
    text_label = tk.Label(root, text=text_content, font=("Arial", 16), bg="white", fg="#FF00FF", justify=tk.LEFT)
    text_label.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

    # Function to handle the back button click event
    def back_to_main_menu():
        root.destroy()

    # Create a back button
    back_button = tk.Button(root, text="Back to Main Menu", font=("Comic Sans MS", 14), bg="#00FFFF", fg="white",
                            activebackground="#00CED1", activeforeground="white", width=20, height=2, command=back_to_main_menu)
    back_button.place(relx=0.5, rely=1.0, anchor=tk.S)  # Position the back button at the bottom center

    root.mainloop()

if __name__ == "__main__":
    display_help()
