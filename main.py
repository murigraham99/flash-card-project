from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
LANGUAGE1 = "Magyar"
LANGUAGE2 = "English"
words_dict = {}

try:
    data = pandas.read_csv("/Users/robertmuresan/Downloads/flash-card-project-start/data/words_to_learn.csv")
except FileNotFoundError:
    initial_data = pandas.read_csv("/Users/robertmuresan/Downloads/flash-card-project-start/data/HU-EN - "
                                   "coduri-judete.csv")
    words_dict = initial_data.to_dict(orient="records")
else:
    words_dict = data.to_dict(orient="records")


# ---------------------------- REMOVE WORDS THAT YOU KNOW ------------------------------- #
def remove():
    words_dict.remove(new_words)
    data = pandas.DataFrame(words_dict)
    data.to_csv("data/words_to_learn.csv", index=False)


# ---------------------------- GENERATE NEW WORD ------------------------------- #
def generate():
    global new_words, timer
    screen.after_cancel(timer)  # after 5 s it cancels the timer
    new_words = random.choice(list(words_dict))
    title.config(text=LANGUAGE1, foreground="black", bg="white")
    word.config(text=new_words["Hungarian"], foreground="black", bg="white")
    canvas.itemconfig(image_bg, image=card_f)
    timer = screen.after(5000, func=flip)


# ---------------------------- FLIP THE CARD AFTER 5s------------------------------- #

def flip():
    title.config(text=LANGUAGE2, bg=BACKGROUND_COLOR)
    word.config(text=new_words["English"], bg=BACKGROUND_COLOR)
    canvas.itemconfig(image_bg, image=card_b)


# ---------------------------- UI SETUP -------------------------------

# screen + start timer
screen = Tk()
screen.title("Flash Cards")
screen.config(bg=BACKGROUND_COLOR, padx=50)
screen.minsize(width=800, height=526)
timer = screen.after(5000, func=flip)

# card images
card_f = PhotoImage(file="/Users/robertmuresan/Downloads/flash-card-project-start/images/card_front.png")
card_b = PhotoImage(file="/Users/robertmuresan/Downloads/flash-card-project-start/images/card_back.png")

canvas = Canvas(bg=BACKGROUND_COLOR, width=800, height=526, borderwidth=0, highlightthickness=0)
image_bg = canvas.create_image(400, 263, image=card_f)
canvas.grid(row=0, column=0, columnspan=2, pady=50)

# title and word
title = Label(text=LANGUAGE1, font=("Ariel", 40, "italic"), foreground="black", bg="white")
title.place(x=320, y=150)

word = Label(font=("Ariel", 60, "bold"), bg="white", foreground="black")
word.place(x=310, y=263)

# start by generating title and word
generate()

# buttons
right = PhotoImage(file="/Users/robertmuresan/Downloads/flash-card-project-start/images/right.png", )
wrong = PhotoImage(file="/Users/robertmuresan/Downloads/flash-card-project-start/images/wrong.png")

button_x = Button(image=right, bg=BACKGROUND_COLOR, padx=50, highlightthickness=0, bd=0,
                  command=lambda: [generate(), remove()])
button_x.grid(row=1, column=0, pady=50)

button_ok = Button(image=wrong, bg=BACKGROUND_COLOR, padx=50, highlightthickness=0, bd=0,
                   command=generate)
button_ok.grid(row=1, column=1, pady=50)


screen.mainloop()
