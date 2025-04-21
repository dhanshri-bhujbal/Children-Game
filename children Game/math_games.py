import tkinter as tk
from PIL import Image, ImageTk
from addition_game_module import AdditionGame  # Import the addition game module
from subtraction_game_module import SubtractionGame  # Import the subtraction game module
from multiplication_game_module import MultiplicationGame  # Import the multiplication game module
import main_menu  # Import the main menu module

# Global variables for the background image and buttons
background_image = None
background_photo = None
background_label = None
addition_game_button = None
subtraction_game_button = None
multiplication_game_button = None
back_button = None
exit_button = None

# Define the button click functions
def on_addition_game_click():
    root = tk.Toplevel()  # Create a new window for the game
    app = AdditionGame(root)  # Create an instance of the addition game
    root.attributes("-fullscreen", True)  # Make the window fullscreen
    root.mainloop()

def on_subtraction_game_click():
    root = tk.Toplevel()  # Create a new window for the game
    app = SubtractionGame(root)  # Create an instance of the subtraction game
    root.attributes("-fullscreen", True)  # Make the window fullscreen
    root.mainloop()

def on_multiplication_game_click():
    root = tk.Toplevel()  # Create a new window for the game
    app = MultiplicationGame(root)  # Create an instance of the multiplication game
    root.attributes("-fullscreen", True)  # Make the window fullscreen
    root.mainloop()

def on_back_click(root):
    root.destroy()  # Close the current window
    main_menu.show_menu()  # Call the show_menu function from the main menu module

def on_exit_click(root):
    root.destroy()  # Close the application window

def on_resize(event):
    global background_image, background_photo, background_label  # Access the global variables
    if background_image:
        new_width = event.width
        new_height = event.height
        resized_image = background_image.resize((new_width, new_height))
        background_photo = ImageTk.PhotoImage(resized_image)
        background_label.config(image=background_photo)

        # Adjust the button positions and sizes
        addition_game_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)
        subtraction_game_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)
        multiplication_game_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)
        back_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)
        exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

# Main function to create the GUI
def create_math_games_screen():
    global background_image, background_photo, background_label  # Access the global variables
    global addition_game_button, subtraction_game_button, multiplication_game_button, back_button, exit_button

    root = tk.Tk()
    root.title("Math Games for Kids")

    # Load the background image
    try:
        background_image = Image.open("math_background.jpg")
        # Resize the image to fit the screen while maintaining aspect ratio
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        background_image = background_image.resize((screen_width, screen_height))
        # Create a PhotoImage object to display the resized image
        background_photo = ImageTk.PhotoImage(background_image)
        # Create a label to hold the background image with sky blue background
        background_label = tk.Label(root, image=background_photo, bg="#87CEEB")
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
    except Exception as e:
        print("Error loading background image:", e)
        root.destroy()  # Close the window if the image loading fails
        return

    # Label to display "Choose the game"
    choose_game_label = tk.Label(root, text="Choose the game", font=("Times New Roman",60, "bold"), bg="#87CEEB",width=24, height=2, fg="black")
    choose_game_label.place(relx=0.5, rely=0.1, anchor=tk.CENTER)

    # Create a button to start the addition game
    addition_game_button = tk.Button(root, text="Addition Game", command=on_addition_game_click, width=18, height=2, bg="#FF8C00", fg="white", font=("Times New Roman", 20, "bold"), bd=8, relief=tk.RAISED)
    addition_game_button.place(relx=0.5, rely=0.3, anchor=tk.CENTER)

    # Create a button to start the subtraction game
    subtraction_game_button = tk.Button(root, text="Subtraction Game", command=on_subtraction_game_click, width=18, height=2, bg="#20B2AA", fg="white", font=("Times New Roman", 20, "bold"), bd=8, relief=tk.RAISED)
    subtraction_game_button.place(relx=0.5, rely=0.45, anchor=tk.CENTER)

    # Create a button to start the multiplication game
    multiplication_game_button = tk.Button(root, text="Multiplication Game", command=on_multiplication_game_click, width=18, height=2, bg="#FF4500", fg="white", font=("Times New Roman", 20, "bold"), bd=8, relief=tk.RAISED)
    multiplication_game_button.place(relx=0.5, rely=0.6, anchor=tk.CENTER)

    # Create a "Back" button
    back_button = tk.Button(root, text="Back", command=lambda: on_back_click(root), width=12, height=2, bg="#6495ED", fg="black", font=("Times New Roman", 40, "bold"), bd=8, relief=tk.RAISED)
    back_button.place(relx=0.1, rely=0.9, anchor=tk.CENTER)

    # Create an "Exit" button
    exit_button = tk.Button(root, text="Exit", command=lambda: on_exit_click(root), width=12, height=2, bg="#DC143C", fg="black", font=("Times New Roman", 40, "bold"), bd=8, relief=tk.RAISED)
    exit_button.place(relx=0.9, rely=0.9, anchor=tk.CENTER)

    root.bind("<Configure>", on_resize)  # Bind resize event
    root.attributes("-fullscreen", True)  # Make the root window fullscreen
    root.mainloop()

# Check if the script is being run as the main program
if __name__ == "__main__":
    create_math_games_screen()