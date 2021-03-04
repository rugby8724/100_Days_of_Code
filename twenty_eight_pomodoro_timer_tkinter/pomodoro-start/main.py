from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 45
SHORT_BREAK_MIN = 10
LONG_BREAK_MIN = 20
study_check = []


# ---------------------------- TIMER RESET ------------------------------- #
# def reset_tomato():
#     window.after_cancel()


# ---------------------------- TIMER MECHANISM ------------------------------- #
def work_timer():
    count_down(WORK_MIN * 60)
    study_check.append('✓')
    check_label['text'] = study_check
    timer_label.config(text='Grind', fg=RED)


def break_timer():
    if len(study_check) == 3:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text='Almost There!!', fg=GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text='Break!!', fg=PINK)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count/60)
    count_second = count % 60
    if count_second < 10:
        count_second = f'0{str(count_second)}'

    canvas.itemconfig(timer_text, text=f'{count_min}:{count_second}')
    if count > 0:
        window.after(1000, count_down, count -1)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title('Grind Timer')
window.config(padx=100, pady=50, bg=YELLOW)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(row=1, column=1)

timer_label = Label(text='Timer', fg=GREEN, bg=YELLOW, font=('Times', 50))
timer_label.grid(row=0, column=1)

start_button = Button(text='Start', command=work_timer)
start_button.grid(row=2, column=0)

break_button = Button(text='Break', command=break_timer)
break_button.grid(row=3, column=0)

reset_button = Button(text='Reset')
reset_button.grid(row=2, column=2)

check_label = Label(text=study_check, bg=YELLOW, fg=GREEN, font=(FONT_NAME, 30, 'bold'))
check_label.grid(row=3, column=1)



window.mainloop()
