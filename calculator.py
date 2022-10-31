#Калькулятор v2
from colorama import init
from colorama import Fore, Back, Style

# use Colorama to make Termcolor work on Windows too
init()

print( Fore.BLACK)
print( Back.MAGENTA)

what = input("Что делаем? (+, -): " )

print( Back.GREEN)

a = float(input("Введи первое число: "))
b = float(input("Введи второе число: "))

print( Back.CYAN)

if what == "+":
    с = a + b
    print("Результат: " + str(с))
elif what == "-":
    с = a - b
    print("Результат: " + str(с))
else:
    print("Выбрана неверная операция!")

input()
