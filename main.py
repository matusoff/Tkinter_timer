from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_mark.config(text="")
    global reps
    reps = 0    

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
       
    #if after 8 rounds the number of reps has no remainder, it is time for long break 
    if reps% 8 ==0:
        count_down(long_break_sec)
        timer_label.config(text="Long Break", fg=RED)  
    elif reps %2 ==0:
        count_down(short_break_sec)
        timer_label.config(text="Break", fg=PINK)   
    else:
        count_down(work_sec)
        timer_label.config(text="Work", fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    #to count how many minutes left, we use math module with floor method that return largest whole number that less or = to x
    #e.g 4.8 min, the largest whole number less than 4.8 is 4, so we get 4 min
    count_min = math.floor(count / 60)
    #to count how many seconds left we use %, to have a remainder of seconds, e.g 100 sec / 60 = 1, then 100-60 = 40 as a remainder
    count_sec = count % 60

    #to display the second zero in the timer, so when count_sec == 0, instead of integer 0 let's create a string "00" 
    #this is possible because of concept known as Dynamic typing or dynamically change of data type 
    # just by assigning a different type of value
    if count_sec < 10:
        count_sec = f"0{count_sec}"
     
    #to change text or label in canvas, use itemconfig() with variable which has to be changed
    #to visualize the timer use f string with defined variables
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
        mark = ""
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            mark += "✔"
        check_mark.config(text=mark)
             

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


#bg and highlightthicknes are keyword(kw) agruguments to fully change the background
canvas = Canvas(width=200, heigh=224, bg=YELLOW, highlightthickness=0)
#to be able to see the image
tomato_image = PhotoImage(file=r"PROJECTS\100days_of_code\TKinter\Pomodoro_timer\tomato.png")

#to place image in the center
canvas.create_image(100,112, image=tomato_image)
#to create a timer text we need to provide x,y values(*args), and key word arguments(text=..)
timer_text = canvas.create_text(100,130,text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))

#to specify a layout of image on screen
canvas.grid(column=1, row=1)


button_start = Button(text="Start", command=start_timer)
button_start.grid(column=0, row=2)

button_reset = Button(text="Reset", command=reset_timer)
button_reset.grid(column=2, row=2)


check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 24, "bold"))
check_mark.grid(column=1, row=3)

timer_label=Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)


window.mainloop()