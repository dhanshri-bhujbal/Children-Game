import tkinter as tk
from PIL import Image, ImageTk
import random

class SubtractionGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Subtraction Adventure")
        # Get screen width and height
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()

        # Load the background image
        original_image = Image.open("addition_background.jpg")

        # Resize the image to fit the screen while maintaining aspect ratio
        image_width, image_height = original_image.size
        screen_ratio = screen_width / screen_height
        image_ratio = image_width / image_height

        if screen_ratio > image_ratio:
            # Resize based on width
            new_width = screen_width
            new_height = int(new_width / image_ratio)
        else:
            # Resize based on height
            new_height = screen_height
            new_width = int(new_height * image_ratio)

        self.background_image = original_image.resize((new_width, new_height))

        # Create a PhotoImage object to display the resized image
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a label to hold the background image
        self.background_label = tk.Label(root, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Calculate font size, button width, and button height based on screen size
        self.font_size = int(48 * screen_width / 1920)
        self.button_width = int(10 * screen_width / 1920)
        self.button_height = int(2 * screen_height / 1080)

        # Initialize score and highest score
        self.score = 0
        self.highest_score = self.load_highest_score()  # Load highest score from file

        # Create a colorful and playful title label with a fun font
        self.title_label = tk.Label(root, text="Subtraction Adventure", font=("Comic Sans MS", self.font_size, "bold"), fg="blue", bg='lightgreen')
        self.title_label.pack(pady=int(20 * screen_height / 1080))

        # Create a label to display the score
        self.score_label = tk.Label(root, text=f"Score: {self.score}\nHighest Score: {self.highest_score}", font=("Comic Sans MS", int(self.font_size*0.8), "bold"), fg="blue", bg='lightgreen')
        self.score_label.place(x=int(20 * screen_width / 1920), y=int(20 * screen_height / 1080))

        # Create heart shapes
        self.hearts = 3
        self.heart_font_size = int(self.font_size * 0.8)
        self.heart_spacing = 10  # Adjusted spacing
        self.hearts_labels = []  # Initialize hearts labels
        self.update_heart_labels()

        # Create a colorful and playful instruction label
        self.instruction_label = tk.Label(root, text="Find the correct answer!", font=("Comic Sans MS", int(36 * screen_width / 1920), "bold"), fg="purple", bg='lightgreen')
        self.instruction_label.pack(pady=int(10 * screen_height / 1080))

        # Create a colorful and playful question display with a fun font
        self.question_label = tk.Label(root, text="", font=("Comic Sans MS", self.font_size, "bold"), fg="red", bg='lightgreen')
        self.question_label.pack(pady=int(20 * screen_height / 1080))

        # Create answer buttons as a vertical frame with colorful and rounded buttons
        self.answer_frame = tk.Frame(root, bg='lightgreen')
        self.answer_frame.pack(pady=int(30 * screen_height / 1080))
        self.answer_buttons = []  # Initialize answer buttons list
        for i in range(3):
            answer_button = tk.Button(self.answer_frame, text="", command=lambda i=i: self.check_answer(i), font=("Comic Sans MS", int(self.font_size*0.8), "bold"), bg='orange', fg='white', width=self.button_width, height=self.button_height, bd=5, relief=tk.RAISED)
            answer_button.pack(side='top', pady=int(10 * screen_height / 1080))
            self.answer_buttons.append(answer_button)

        # Create a "Back" button with a playful color and font
        self.back_button = tk.Button(root, text="Back", command=self.on_back_click, font=("Comic Sans MS", int(self.font_size*0.8), "bold"), bg="lightgreen", fg="white", bd=5, relief=tk.RAISED)
        self.back_button.pack(side='left', padx=int(20 * screen_width / 1920), pady=int(20 * screen_height / 1080), anchor="se")

        # Create a "Next" button with a playful color and font
        self.next_button = tk.Button(root, text="Next", command=self.generate_question, font=("Comic Sans MS", int(self.font_size*0.8), "bold"), bg="lightgreen", fg="white", bd=5, relief=tk.RAISED)
        self.next_button.pack(side='right', padx=int(20 * screen_width / 1920), pady=int(20 * screen_height / 1080), anchor="sw")

        # Create a "Restart" button initially hidden
        self.restart_button = tk.Button(root, text="Restart", command=self.restart_game, font=("Comic Sans MS", int(self.font_size*0.8), "bold"), bg="red", fg="white", bd=5, relief=tk.RAISED)
        self.restart_button.pack_forget()  # Initially hidden

        self.game_active = True  # Flag to track game state
        self.game_over_message_id = None  # Initialize game over message ID
        self.generate_question()  # Generate the first question

    def on_back_click(self):
        self.root.destroy()

    def update_heart_labels(self):
        heart_icon = "\u2764\ufe0f"  # Unicode escape sequence for the heart symbol
        hearts_text = heart_icon * self.hearts
        hearts_width = self.heart_font_size * self.hearts + self.heart_spacing * (self.hearts - 1)
        heart_start_x = self.root.winfo_screenwidth() - hearts_width - 20  # Adjust position from the right side
        heart_start_y = 20 * self.root.winfo_screenheight() / 1080

        # Remove existing heart labels
        for label in self.hearts_labels:
            label.destroy()

        # Create individual labels for each heart shape
        self.hearts_labels = []
        for i in range(self.hearts):
            heart_label = tk.Label(self.root, text=heart_icon, font=("Arial", self.heart_font_size, "bold"), fg="red", bg='lightgreen')
            heart_label.place(x=heart_start_x + (self.heart_font_size + self.heart_spacing) * i, y=heart_start_y)
            self.hearts_labels.append(heart_label)

    def generate_question(self):
        if not self.game_active:  # Check if game is active
            return  # Exit function if game is not active

        num1 = random.randint(1, 50)
        num2 = random.randint(1, num1)  # Ensure num2 is less than num1 for valid subtraction
        self.correct_answer = num1 - num2
        self.question = f"What is {num1} - {num2}?"
        self.question_label.config(text=self.question)

        self.answer_options = [self.correct_answer]
        while len(self.answer_options) < 3:
            answer = random.randint(1, 500)
            if answer != self.correct_answer and answer not in self.answer_options:
                self.answer_options.append(answer)

        random.shuffle(self.answer_options)

        # Reset the text and background color of all answer buttons
        for i in range(3):
            self.answer_buttons[i].config(text=self.answer_options[i], bg='orange')

    def check_answer(self, selected_index):
        if not self.game_active:  # Check if game is active
            return  # Exit function if game is not active

        selected_answer = self.answer_options[selected_index]
        if selected_answer == self.correct_answer:
            self.score += 1
            self.highest_score = max(self.score, self.highest_score)  # Update highest score
            self.save_highest_score()  # Save highest score to file
            self.score_label.config(text=f"Score: {self.score}\nHighest Score: {self.highest_score}")
            self.display_temporary_message("Great job! That's the right answer.", "green", duration=2000)  # Increase duration to 3000 milliseconds
        else:
            self.hearts -= 1
            self.update_heart_labels()  # Update hearts display
            if self.hearts <= 0:
                self.game_active = False  # Set game state to inactive
                self.game_over_message_id = self.display_temporary_message("You've lost all your hearts. Game Over!", "red", duration=2000)  # Store message id for cancellation
                self.restart_button.pack()  # Display the restart button
            else:
                correct_option_index = self.answer_options.index(self.correct_answer)
                correct_option_button = self.answer_buttons[correct_option_index]
                correct_option_button.config(bg="red")
                self.display_temporary_message(f"Oops! That's not correct. The correct answer is {self.correct_answer}.", "red", duration=2000)  # Increase duration to 3000 milliseconds

        self.generate_question()  # Generate a new question regardless of hearts

    def restart_game(self):
        self.hearts = 3
        self.score = 0
        self.update_heart_labels()  # Update hearts display
        self.score_label.config(text=f"Score: {self.score}\nHighest Score: {self.highest_score}")
        self.restart_button.pack_forget()  # Hide the restart button
        self.game_active = True  # Set game state to active
        self.generate_question()
        self.display_temporary_message("Game Restarted!", "blue", duration=2000)  # Display restart message
        # Remove the "Game Over!" message if it's currently displayed
        if self.game_over_message_id:
            self.root.after_cancel(self.game_over_message_id)

    def display_temporary_message(self, message, color, duration):
        # Create a label to display the message at the center of the window
        message_label = tk.Label(self.root, text=message, font=("Comic Sans MS", int(self.font_size*0.8), "bold"), fg=color, bg='lightgreen')
        message_label.place(x=(self.root.winfo_screenwidth() - message_label.winfo_reqwidth()) / 2, y=(self.root.winfo_screenheight() - message_label.winfo_reqheight()) / 2)

        # After the specified duration, remove the message label
        return self.root.after(duration, message_label.destroy)

    def load_highest_score(self):
        try:
            with open("highest_score.txt", "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return 0

    def save_highest_score(self):
        with open("highest_score.txt", "w") as file:
            file.write(str(self.highest_score))

if __name__ == "__main__":
    root = tk.Tk()
    app = SubtractionGame(root)
    root.attributes("-fullscreen", True)  # Make the window fullscreen
    root.mainloop()
