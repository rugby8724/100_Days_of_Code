from tkinter import *


def button_click():
    new_text = user_input .get()
    my_label['text'] = new_text


window = Tk()
window.title('My first GUI')
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

my_label = Label(text='I am a label', font=('Arial', 24, 'bold'))
#pack will place component into the screen and center the component
# my_label.pack()
my_label.grid(column=0, row=0)

# my_label['text'] = 'New Text'
# my_label.config(text='New Text')

#Button


button = Button(text='Click Me', command=button_click)
button.grid(column=1, row=1)

new_button = Button(text='Hello World',)
new_button.grid(column=2, row=0)

#Entry

user_input = Entry(width=10)
user_input.grid(column=3, row=2)


#keeps window open has to be at the end of the program
window.mainloop()