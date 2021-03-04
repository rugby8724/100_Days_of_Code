from tkinter import *
import random
import pandas



BACKGROUND_COLOR = "#B1DDC6"

try :
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')
words = df.to_dict(orient='records')
word = {}

# ---------------------------- Get Word ------------------------------- #


def get_word():

    def flip():
        canvas.itemconfig(lang_text, text='English', fill='white')
        canvas.itemconfig(word_text, text=word['English'], fill='white')
        canvas.itemconfig(card, image=back_image)
        x_button.grid(row=1, column=0)
        y_button.grid(row=1, column=1)
    global word
    word = random.choice(words)
    canvas.itemconfig(lang_text, text='French', fill='black')
    canvas.itemconfig(word_text, text=word['French'], fill='black')
    canvas.itemconfig(card, image=front_image)
    x_button.grid_forget()
    y_button.grid_forget()
    window.after(3000, flip)


def is_known():
    words.remove(word)
    data = pandas.DataFrame(words)
    data.to_csv('data/words_to_learn.csv', index=False)
    get_word()






# ---------------------------- UI SETU)P ------------------------------- #
window = Tk()
window.title('Flashy')
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)



canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file='./images/card_front.png')
back_image = PhotoImage(file='./images/card_back.png')
card = canvas.create_image(400, 263, image=front_image)
lang_text = canvas.create_text(400, 150, text='Language', font=('Ariel', 40, 'italic'))
word_text = canvas.create_text(400, 263, text='New Word', font=('Ariel', 60, 'bold'))


canvas.grid(row=0, column=0, columnspan=2)
x_image = PhotoImage(file='./images/wrong.png')
x_button = Button(image=x_image, highlightthickness=0, command=get_word)
x_button.grid(row=1, column=0)

y_image = PhotoImage(file='./images/right.png')
y_button = Button(image=y_image, highlightthickness=0, command=is_known)
y_button.grid(row=1, column=1)


get_word()

window.mainloop()
