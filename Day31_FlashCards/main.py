from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("Day31_FlashCards/words_to_learn.csv")

except FileNotFoundError:
    original_data = pandas.read_csv("Day31_FlashCards/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


# -------------- BUTTON -------------------

def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas_wind.itemconfigure(card_title, text="French", fill="black")
    canvas_wind.itemconfig(card_word, text=current_card["French"], fill="black")
    canvas_wind.itemconfig(card_background, image= card_front_img)
    
    flip_timer = window.after(3000, func=flip_card)


# ------------ CHANGE PROCESS FUNCTION -----------

def flip_card():
    canvas_wind.itemconfig(card_title, text="English", fill="white")
    canvas_wind.itemconfig(card_word, text=current_card["English"])
    canvas_wind.itemconfig(card_background, image=card_back_img)

def is_known():
    to_learn.remove(current_card)
    data_list = pandas.DataFrame(to_learn)
    data_list.to_csv("Day31_FlashCards/words_to_learn.csv", index=False)
    next_card()




# ------------------ GUI -----------------
window = Tk()
window.title("Learning Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)


canvas_wind = Canvas(width= 800, height=526)
card_front_img = PhotoImage(file= "images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_background = canvas_wind.create_image(400, 263, image=card_front_img)
card_title = canvas_wind.create_text(400, 150, font= ("Arial", 40, "italic"))
card_word = canvas_wind.create_text(400, 263, font=("Arial", 60, "bold"))
canvas_wind.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_wind.grid(row=0, column=0, columnspan=2)


cross_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image= cross_image, command=next_card)
wrong_button.grid(row=1, column=0)


check_image = PhotoImage(file="images/right.png")
right_button = Button(image=check_image, command=is_known)
right_button.grid(row=1, column=1)



next_card()

window.mainloop()
