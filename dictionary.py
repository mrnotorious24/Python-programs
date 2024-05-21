dict1 = {
    "+": [100, 200],
    "-": [50, 40],
    "*": [30, 10],
    "/": [10, 2]
}

x = input("Enter an operator: ")
print("Operation entered:", x)

def add():
    a = dict1["+"]
    print("Numbers to add:", a)
    b = a[0] + a[1]
    print("Result of addition:", b)

def sub():
    a = dict1["-"]
    print("Numbers to subtract:", a)
    b = a[0] - a[1]
    print("Result of subtraction:", b)

def mul():
    a = dict1["*"]
    print("Numbers to multiply:", a)
    b = a[0] * a[1]
    print("Result of multiplication:", b)

def div():
    a = dict1["/"]
    print("Numbers to divide:", a)
    b = a[0] / a[1]
    print("Result of division:", b)

if x == "+":
    add()
elif x == "-":
    sub()
elif x == "*":
    mul()
elif x == "/":
    div()
else:
    print("Invalid operator entered!")
