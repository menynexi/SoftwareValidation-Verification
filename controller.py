from addition import addition
from subtraction import subtraction
from multiplication import multiplication
from divide import divide
from square import square
from tkinter import *
import re

expression = ""

def press(num):
    global expression
    print(expression)
    expression = expression + str(num)
    print("new expression", expression)
    equation.set(expression)

def getNumber(input_string):
  expression = input_string
  pattern = r"(\d+)"
  match = re.match(pattern, expression)

  if match:
      first_number = int(match.group())
      print("First number:", first_number)
      return first_number
  else:
      print("No number found")
      return 0

def equalpress():
    global expression

    #gets the first number
    input_string = expression
    result = getNumber(input_string)
    input_string = input_string[len(str(result))::]
    print(input_string)
    try:
        while input_string != '':
            if input_string[0] == '+':
                input_string = input_string[1::]
                result = addition(result, getNumber(input_string))
                input_string = input_string[len(str(getNumber(input_string)))::]
                print(input_string)
            elif input_string[0] == '-':
                input_string = input_string[1::]
                result = subtraction(result, getNumber(input_string))
                input_string = input_string[len(str(getNumber(input_string)))::]
                print(input_string)
            elif input_string[0] == '*':
                input_string = input_string[1::]
                result = multiplication(result, getNumber(input_string))
                input_string = input_string[len(str(getNumber(input_string)))::]
                print(input_string)
            elif input_string[0] == '/':
                input_string = input_string[1::]
                result = divide(result, getNumber(input_string))
                input_string = input_string[len(str(getNumber(input_string)))::]
                print(input_string)
            elif input_string[0] == '^':
                input_string = input_string[1::]
                result = square(result, getNumber(input_string))
                input_string = input_string[len(str(getNumber(input_string)))::]
                print(input_string)

        equation.set(str(result))
    except:
        equation.set("ERROR")
 
def clear():
    global expression
    expression = ""
    equation.set("")
 

if __name__ == "__main__":
    gui = Tk()
    gui.configure(background="light green")
    gui.title("MATH++")
    gui.geometry("270x150")

    equation = StringVar()
    expression_field = Entry(gui, textvariable=equation)
    expression_field.grid(columnspan=4, ipadx=70)

    #button press
    button1 = Button(gui, text=' 1 ', fg='black', bg='red',
                    command=lambda: press(1), height=1, width=7)
    button1.grid(row=2, column=0)
 
    button2 = Button(gui, text=' 2 ', fg='black', bg='red',
                    command=lambda: press(2), height=1, width=7)
    button2.grid(row=2, column=1)
 
    button3 = Button(gui, text=' 3 ', fg='black', bg='red',
                    command=lambda: press(3), height=1, width=7)
    button3.grid(row=2, column=2)
 
    button4 = Button(gui, text=' 4 ', fg='black', bg='red',
                    command=lambda: press(4), height=1, width=7)
    button4.grid(row=3, column=0)
 
    button5 = Button(gui, text=' 5 ', fg='black', bg='red',
                    command=lambda: press(5), height=1, width=7)
    button5.grid(row=3, column=1)
 
    button6 = Button(gui, text=' 6 ', fg='black', bg='red',
                    command=lambda: press(6), height=1, width=7)
    button6.grid(row=3, column=2)
 
    button7 = Button(gui, text=' 7 ', fg='black', bg='red',
                    command=lambda: press(7), height=1, width=7)
    button7.grid(row=4, column=0)
 
    button8 = Button(gui, text=' 8 ', fg='black', bg='red',
                    command=lambda: press(8), height=1, width=7)
    button8.grid(row=4, column=1)
 
    button9 = Button(gui, text=' 9 ', fg='black', bg='red',
                    command=lambda: press(9), height=1, width=7)
    button9.grid(row=4, column=2)
 
    button0 = Button(gui, text=' 0 ', fg='black', bg='red',
                    command=lambda: press(0), height=1, width=7)
    button0.grid(row=5, column=0)
 
    plus = Button(gui, text=' + ', fg='black', bg='red',
                command=lambda: press("+"), height=1, width=7)
    plus.grid(row=2, column=3)
 
    minus = Button(gui, text=' - ', fg='black', bg='red',
                command=lambda: press("-"), height=1, width=7)
    minus.grid(row=3, column=3)
 
    multiply = Button(gui, text=' * ', fg='black', bg='red',
                    command=lambda: press("*"), height=1, width=7)
    multiply.grid(row=4, column=3)
 
    divide = Button(gui, text=' / ', fg='black', bg='red',
                    command=lambda: press("/"), height=1, width=7)
    divide.grid(row=5, column=3)
 
    equal = Button(gui, text=' = ', fg='black', bg='red',
                command=equalpress, height=1, width=7)
    equal.grid(row=5, column=2)
 
    clear = Button(gui, text='Clear', fg='black', bg='red',
                command=clear, height=1, width=7)
    clear.grid(row=5, column='1')
 
    Decimal= Button(gui, text='.', fg='black', bg='red',
                    command=lambda: press('.'), height=1, width=7)
    Decimal.grid(row=6, column=0)

    Squared = Button(gui, text=' ^ ', fg='black', bg='red',
                    command=lambda: press('^'), height=1, width=7)
    Squared.grid(row=6, column=3)

    # start the GUI
    gui.mainloop()