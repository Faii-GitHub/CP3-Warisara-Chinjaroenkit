def AddNumber(x, y):
    print("x + y =",x + y)


def ReduceNumber(x, y):
    print("x - y =",x - y)


def MultiplyNumber(x, y):
    print("x * y =",x * y)


def DivideNumber(x, y):
    print("x / y =",int(x / y))

Num1 = int(input("Input x Number:"))
Num2 = int(input("Input y Number:"))
AddNumber(Num1, Num2)
ReduceNumber(Num1, Num2)
MultiplyNumber(Num1, Num2)
DivideNumber(Num1, Num2)