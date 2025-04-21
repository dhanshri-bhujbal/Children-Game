import tkinter as tk
from PIL import Image, ImageTk
import random
import main_menu  # Importing the main_menu module

def load_highest_score():
    try:
        with open("highest_score.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 0

def save_highest_score(score):
    with open("highest_score.txt", "w") as file:
        file.write(str(score))

def start_typing_game():
    def restart_game():
        root.destroy()
        start_typing_game()

    def update_highest_score():
        nonlocal score, highest_score
        if score > highest_score:
            highest_score = score
            highest_score_label.config(text="Highest Score: " + str(highest_score))
            save_highest_score(highest_score)

    def generate_brick():
        nonlocal brick, brick_text, brick_falling
        x_pos = random.randint(0, root.winfo_screenwidth() - brick_width)
        brick = canvas.create_rectangle(x_pos, 0, x_pos + brick_width, brick_height, fill=random_color(), outline="#FFFFFF")
        falling_letter = random.choice("abcdefghijklmnopqrstuvwxyz")
        brick_text = canvas.create_text(x_pos + brick_width / 2, brick_height / 2, text=falling_letter, font=("Arial", brick_width // 4, "bold"), fill="#FFFFFF")
        brick_falling = True
        move_brick()

    def random_color():
        return random.choice(["#4F4F4F", "#2F4F4F", "#708090", "#2E8B57", "#4B0082", "#800000"])

    def check_word(event):
        nonlocal score, lives, brick_falling
        typed_word = word_entry.get().lower()
        if brick_falling:
            if typed_word == canvas.itemcget(brick_text, 'text'):
                score += 1
                score_label.config(text="Score: " + str(score))
                update_highest_score()
                canvas.delete(brick)
                canvas.delete(brick_text)
                brick_falling = False
                generate_brick()
            else:
                lives -= 1
                if lives >= 0:
                    canvas.delete(heart_icons[lives])
                if lives == 0:
                    restart_screen()
        word_entry.delete(0, tk.END)

    def move_brick():
        nonlocal brick, brick_text, brick_falling, brick_speed, lives, heart_icons, speed_increase_amount, speed_change_interval
        if brick_falling:
            canvas.move(brick, 0, brick_speed)
            canvas.move(brick_text, 0, brick_speed)
            if canvas.coords(brick)[3] > root.winfo_screenheight():
                lives -= 1
                if lives >= 0:
                    canvas.delete(heart_icons[lives])
                if lives == 0:
                    restart_screen()
                canvas.delete(brick)
                canvas.delete(brick_text)
                brick_falling = False
                generate_brick()
        root.after(50, move_brick)

    def generate_brick_with_delay():
        nonlocal speed_change_interval
        root.after(1000, generate_brick)
        root.after(speed_change_interval, change_brick_speed)

    def change_brick_speed():
        nonlocal brick_speed, speed_increase_amount, max_brick_speed
        if brick_speed < max_brick_speed:
            brick_speed += speed_increase_amount
        root.after(speed_change_interval, change_brick_speed)

    def go_back_to_menu():
        root.destroy()
        main_menu.show_menu()  # Call the show_menu function from the main_menu module

    def restart_screen():
        game_over_label = tk.Label(root, text="Game Over", font=("Arial", root.winfo_screenwidth() // 40, "bold"), bg="red", fg="white")
        game_over_label.place(relx=0.5, rely=0.4, anchor="center")

        restart_button = tk.Button(root, text="Restart", font=("Arial", root.winfo_screenwidth() // 80, "bold"), bg="#FF6347", fg="#FFFFFF", bd=0, padx=root.winfo_screenwidth() // 50, pady=root.winfo_screenheight() // 90, command=restart_game)
        restart_button.place(relx=0.5, rely=0.5, anchor="center")

    root = tk.Tk()
    root.title("Typing Game")
    root.attributes('-fullscreen', True)

    background_image = Image.open("typing_background.jpg")
    background_image = background_image.resize((root.winfo_screenwidth(), root.winfo_screenheight()))
    background_photo = ImageTk.PhotoImage(background_image)

    canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
    canvas.pack(fill=tk.BOTH, expand=True)
    canvas.background = background_photo  # Keep a reference to the image object
    canvas.create_image(0, 0, image=background_photo, anchor=tk.NW)

    score = 0
    highest_score = load_highest_score()
    lives = 3
    heart_text = "♥"
    heart_font_size = root.winfo_screenwidth() // 20
    brick_width = root.winfo_screenwidth() // 14
    brick_height = brick_width // 2
    initial_brick_speed = 1
    brick_speed = initial_brick_speed
    brick_falling = False
    brick = None
    brick_text = None
    speed_increase_amount = 0.00005
    speed_change_interval = 15000
    max_brick_speed = 10

    box_width = root.winfo_screenwidth() // 8
    box_height = root.winfo_screenheight() // 15
    box_x = root.winfo_screenwidth() - (root.winfo_screenwidth() // 10)
    box_y = root.winfo_screenheight() // 20
    heart_spacing = (box_width - heart_font_size * lives) // (lives + 1)

    heart_icons = []
    for i in range(lives):
        heart_x = box_x + (heart_spacing * (i + 1)) + (heart_font_size * i) - 20
        heart_y = box_y + box_height // 2 - heart_font_size // 2
        heart_icon = canvas.create_text(heart_x + 10, heart_y, text=heart_text, font=("Arial", heart_font_size), fill="#FF6347")
        heart_icons.append(heart_icon)

    highest_score_label = tk.Label(root, text="Highest Score: " + str(highest_score), font=("Arial", root.winfo_screenwidth() // 60, "bold"), bg="#87CEEB", fg="#000000")
    highest_score_label.place(x=root.winfo_screenwidth() // 2, y=root.winfo_screenheight() // 50, anchor="n")

    back_to_menu_button = tk.Button(root, text="Back to Menu", font=("Arial", root.winfo_screenwidth() // 80, "bold"), bg="#FF6347", fg="#FFFFFF", bd=0, padx=root.winfo_screenwidth() // 50, pady=root.winfo_screenheight() // 90, command=go_back_to_menu)
    back_to_menu_button.place(relx=0.05, rely=0.95, anchor='sw')

    score_label = tk.Label(root, text="Score: 0", font=("Arial", root.winfo_screenwidth() // 60, "bold"), bg="#87CEEB", fg="#000000")
    score_label.place(x=root.winfo_screenwidth() // 100, y=root.winfo_screenheight() // 50, anchor="nw")

    entry_bg_color = "#FF6347"
    word_entry = tk.Entry(root, font=("Arial", root.winfo_screenwidth() // 60), bg=entry_bg_color)
    word_entry.place(x=root.winfo_screenwidth() // 2, y=root.winfo_screenheight() - (root.winfo_screenheight() // 18), anchor="center")

    word_entry.bind("<Return>", check_word)
    word_entry.focus()

    generate_brick_with_delay()

    root.mainloop()

if __name__ == "__main__":
    start_typing_game()
