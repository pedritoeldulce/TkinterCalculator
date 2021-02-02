from tkinter import *
import parser

root = Tk()
root.title("Calculator")


root.geometry("260x180")
root.iconbitmap("envase.ico")
root.config(bg="blue")
root.resizable(0,0)

display = Entry(root)
display.grid(row=1, columnspan=6, sticky=W+E) # sticky: indica que lo que que av a abarcar

i = 0

def get_numbers(n):
    global i
    display.insert(i, n)
    i+=1

def get_operations(operator):
    global i
    len_operator = len(operator)
    display.insert(i, operator)
    i+=len_operator

def clear_display():
    display.delete(0, END)


def undo():
    display_state = display.get() #display.get=arroja el valor actualde la pantalla
    if len(display_state):
        display_new_state = display_state[:-1]
        clear_display()
        display.insert(0, display_new_state)
    else:
        clear_display()
        display.insert(0, "Error")

def calculate():
    display_state = display.get()
    try:
        math_expression = parser.expr(display_state).compile()
        result = eval(math_expression)
        clear_display()
        display.insert(0, result)
    except:
        clear_display()
        display.insert(0,  "Error")

# Font
# font =tkFont.Font(family="Helvetica", size=16)

# Numeric Buttons
Button(root, text="1", fg='green', width=6, height=2, command=lambda:get_numbers(1)).grid(row=2, column=0,sticky=W+E)
Button(root, text="2", fg='green', width=6, height=2, command=lambda:get_numbers(2)).grid(row=2, column=1,sticky=W+E)
Button(root, text="3", fg='green', width=6, height=2, command=lambda:get_numbers(3)).grid(row=2, column=2,sticky=W+E)

Button(root, text="4", fg='green', height=2, command=lambda:get_numbers(4)).grid(row=3, column=0,sticky=W+E)
Button(root, text="5", fg='green', height=2, command=lambda:get_numbers(5)).grid(row=3, column=1,sticky=W+E)
Button(root, text="6", fg='green', height=2, command=lambda:get_numbers(6)).grid(row=3, column=2,sticky=W+E)

Button(root, text="7", fg='green', height=2, command=lambda:get_numbers(7)).grid(row=4, column=0,sticky=W+E)
Button(root, text="8", fg='green', height=2, command=lambda:get_numbers(8)).grid(row=4, column=1,sticky=W+E)
Button(root, text="9", fg='green', height=2, command=lambda:get_numbers(9)).grid(row=4, column=2,sticky=W+E)

# Operation Buttons

Button(root, text="AC", height=2, command=lambda:clear_display()).grid(row=5,  column=0,sticky=W+E)
Button(root, text="0", height=2, command=lambda:get_numbers(0)).grid(row=5,  column=1,sticky=W+E)
Button(root, text="%", height=2, command=lambda:get_operations("%")).grid(row=5, column=2,sticky=W+E)


Button(root, text="+", height=2, width=6, command=lambda:get_operations("+")).grid(row=2,  column=3, sticky=W+E)
Button(root, text="-", height=2, command=lambda:get_operations("-")).grid(row=3,  column=3, sticky=W+E)
Button(root, text="*", height=2, command=lambda:get_operations("*")).grid(row=4,  column=3, sticky=W+E)
Button(root, text="/", height=2, command=lambda:get_operations("/")).grid(row=5,  column=3, sticky=W+E)

Button(root, text="←", height=2, width=6,command=lambda:undo()).grid(row=2,  column=4, sticky=W+E, columnspan=2)
Button(root, text="exp", height=2, command=lambda:get_operations("**")).grid(row=3,  column=4, sticky=W+E)
Button(root, text="^2", height=2, command=lambda:get_operations("**2")).grid(row=3,  column=5, sticky=W+E)
Button(root, text="(", height=2, command=lambda:get_operations("(")).grid(row=4,  column=4, sticky=W+E)
Button(root, text=")", height=2, command=lambda:get_operations(")")).grid(row=4,  column=5, sticky=W+E)
Button(root, text="=", height=2, command=lambda:calculate()).grid(row=5,  column=4, sticky=W+E, columnspan = 2)

root.mainloop()