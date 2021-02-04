from tkinter import *


def convert_button():
    miles = int(miles_input.get())
    km = round(miles * 1.60934, 2)
    km_output['text'] = km


window = Tk()
window.title('Miles to Km Converter')
window.minsize(width=400, height=100)
window.config(padx=20, pady=20)

miles_input = Entry(width=10)
miles_input.grid(row=0, column=1)

miles_label = Label(text='Miles')
miles_label.grid(row=0, column=2)

equal_label = Label(text='is equal to')
equal_label.grid(row=1, column=0)

km_output = Label(text='0')
km_output.grid(row=1, column=1)

km_label = Label(text='Km')
km_label.grid(row=1, column=2)

calculate_button = Button(text='Calculate', command=convert_button)
calculate_button.grid(row=2, column=1)









window.mainloop()