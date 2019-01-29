operator = {"+", "-", "*", "/"}
pol_notation_in = (input("Введите выражение: ")).split()
assert pol_notation_in[0] in operator, "Не выбран (неправильно выбран) оператор"
# Полагаю, что лишние аргументы лучше отсечь с помощью assert, чем усложнять функцию, и все включил обработку IndexError
# assert len(pol_notation_in) == 3, "Число аргументов меньше или больше 2"
def pol_notation_calculate(pol_expression):
   if pol_expression[0] == "+" : return print(int(pol_expression[1]) + int(pol_expression[2]))
   elif pol_expression[0] == "-" : return print(int(pol_expression[1]) - int(pol_expression[2]))
   elif pol_expression[0] == "*" : return print(int(pol_expression[1]) * int(pol_expression[2]))
   elif pol_expression[0] == "/" : return print(int(pol_expression[1]) / int(pol_expression[2]))

try:
  pol_notation_calculate(pol_notation_in)
except ValueError:
  print("Один или оба аргумента не являются числами")
except ZeroDivisionError:
  print("Деление на ноль")
except IndexError:
  print("Недостаточно аргументов")

if len(pol_notation_in) > 3 : print("Лишние аргументы отброшены")