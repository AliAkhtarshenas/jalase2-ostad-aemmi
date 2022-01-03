import math
for i in range(10):
    a = float(input("enter first number:"))
    b = float(input("enter second number:"))
    op = input("enter caracter:")
    if op == "+":
        print(a + b)
    if op == "-":
        print(a - b)
    if op == "*":
        print(a * b)
    if op == "/":
        if b == 0:
            print("eror")
        else:
            print(a / b)