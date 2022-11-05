import tkinter

from operations import *
from history import *
from tkinter import *

root = Tk()
root.mainloop()
button1 = tkinter.Button(text='Start', command=calk())
button1.bind()


while True:
    def calk():
        choice = input('\nДоступные операции: \n 1 = + \n 2 = - \n 3 = / \n 4 = * \n exit \n Что будем делать?: ')

        if choice.upper() == 'EXIT':
            exit()
        elif choice != '1' and choice != '2' and choice != '3' and choice != '4':
            print('Нет такой операции!')
            calk()
        try:
            num1 = float(input('Число 1: '))
            num2 = float(input('Число 2: '))
        except ValueError:
            print('Ошибка, нужно ввести число!')
            calk()

        if choice == '1':
            result1 = (f'{num1} + {num2} = {Sum(num1, num2)}')
            print(result1)
            save(result1 + '\n')
        elif choice == '2':
            result2 = (f'{num1} - {num2} = {Substruction(num1, num2)}')
            print(result2)
            save(result2 + '\n')
        elif choice == '3':
            try:
                result3 = (f'{num1} / {num2} = {Division(num1, num2)}')
                print(result3)
                save(result3 + '\n')
            except ZeroDivisionError:
                print('Ошибка деления на ноль!')
        elif choice == '4':
            result4 = (f'{num1} * {num2} = {Multiplication(num1, num2)}')
            print(result4)
            save(result4 + '\n')


    calk()

