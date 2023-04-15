from tkinter import *

def button_pressed(num):
    global equation_text
    equation_text = equation_text + str(num)
    equation_label.set(equation_text)

def equals_button_pressed():
    global equation_text
    try:
            total = str(eval(equation_text))
            equation_label.set(total)
            equation_text = total

    except SyntaxError:
            equation_label.set("syntax error")
            equation_text = ""

    except ZeroDivisionError:
            equation_label.set("arithmetic error")
    equation_text = ''

def clear(): 
    global equation_text

    equation_label.set("")
    equation_text = ''


window = Tk()

window.title("Calculator")
window.geometry("500x500")

equation_text = ''

equation_label = StringVar()
#set up the label (top)
label= Label(window, textvariable=equation_label, font=("Arial", 20), bg= "grey", width= 23 , height= 2)
label.pack()
#set up the frame
frame = Frame(window,)
frame.pack()
#set up the buttons
button1 = Button(frame, text="1", width= 9, height= 4, font= 30, command=lambda: button_pressed(1))
button1.grid(row=0, column=0)

button2 = Button(frame, text="2", width= 9, height= 4, font= 30, command=lambda: button_pressed(2))
button2.grid(row=0, column=1)

button3 = Button(frame, text="3", width= 9, height= 4, font= 30, command=lambda: button_pressed(3))
button3.grid(row=0, column=2)

button4 = Button(frame, text="4", width= 9, height= 4, font= 30, command=lambda: button_pressed(4))
button4.grid(row=1, column=0)

button5 = Button(frame, text="5", width= 9, height= 4, font= 30, command=lambda: button_pressed(5))
button5.grid(row=1, column=1)

button6 = Button(frame, text="6", width= 9, height= 4, font= 30, command=lambda: button_pressed(5))
button6.grid(row=1, column=2)

button7 = Button(frame, text="7", width= 9, height= 4, font= 30, command=lambda: button_pressed(7))
button7.grid(row=2, column=0)

button8 = Button(frame, text="8", width= 9, height= 4, font= 30, command=lambda: button_pressed(8))
button8.grid(row=2, column=1)

button9 = Button(frame, text="9", width= 9, height= 4, font= 30, command=lambda: button_pressed(9))
button9.grid(row=2, column=2)

buttonPL = Button(frame, text="+", width= 9, height= 4, font= 30, command=lambda: button_pressed('+'))
buttonPL.grid(row=3, column=3)

button0 = Button(frame, text="0", width= 9, height= 4, font= 30, command=lambda: button_pressed(0))
button0.grid(row=3, column=1)

buttonmin = Button(frame, text="-", width= 9, height= 4, font= 30, command=lambda: button_pressed('-'))
buttonmin.grid(row=0, column=3)

buttondiv = Button(frame, text="/", width= 9, height= 4, font= 30, command=lambda: button_pressed('/'))
buttondiv.grid(row=1, column=3)

buttonx = Button(frame, text="x", width= 9, height= 4, font= 30, command=lambda: button_pressed('*'))
buttonx.grid(row=2, column=3)

buttondes = Button(frame, text=".", width= 9, height= 4, font= 30, command=lambda: button_pressed('.'))
buttondes.grid(row=3, column=2)

button_equal = Button(frame, text="=", width= 9, height= 4, font= 30, command=equals_button_pressed)
button_equal.grid(row=3 , column=0)

clear = Button(window, text='clear', height=4, width=12, font=35,command=clear)
clear.pack()

window.mainloop()
