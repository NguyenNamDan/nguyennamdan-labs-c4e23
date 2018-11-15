# a = int(input("a = "))
# b = int(input("b = "))

# op = input("operation(+,-,*,/): ")
# if op == "+":
#     print(a, "+", b, "=", a + b)
# elif op == "-":
#     print(a, "-", b, "=", a - b)
# elif op == "*":
#     print(a, "*", b, "=", a * b)
# elif op == "/":
#     print(a, "/", b, "=", a / b) 
# else:
#     print("unsupport") 

from random import randint, choice
from namdan import eval
while True:
    def quiz():
        x = randint(0, 10)
        y = randint(0, 10)
        ero = randint(-2, 2)
        o = choice(["+", "-", "*", "/"])
        r = eval(x, y, o) + ero

        return x, y, o, r, ero

    a, b, op, r, eror = quiz() 
    print(a, op, b, "= ", r)  
    ans = input("Y/N?").lower() 
    if eror == 0:
        if ans == "y":
            print("ok")
        else:
            print("not ok")
    else:
        if ans == "y":
            print(" not ok")
        else:
            print("ok")
        

# from random import randint, choice
# op_list = ["+", "-", "*", "/"]
# def math(x, y, op):
#     if op == "+":
#         return a + b
#     elif op == "-":
#         return a - b
#     elif op == "*":
#         return a * b
#     else:
#         return a / b
# while True:
#     x = randint(0, 10)
#     y = randint(0, 10)
#     op = choice(op_list)
#     eror = randint(-2, 2)
#     if op == "+":
#         print(a, "+", b, "=", a + b)
#     elif op == "-":
#         print(a, "-", b, "=", a - b)
#     elif op == "*":
#         print(a, "*", b, "=", a * b)
#     else:
#         print(a, "/", b, "=", a / b) 
    # if op == "+":
        # kq = x + y + eror
        # print(x, "+", y, "=",kq)
        # ans = input("Y/N? ").upper()
        # if ans == "Y":
        #     if eror == 0:
        #         print("ok")
        #     else:
        #         print("not ok")
        # else:
        #     if eror == 0:
        #         print("not ok")
        #     else:
        #         print("ok")

# def add(a, b): 
#     r = a + b
#     return r 

# # call function
# s = add(1, 2) 
# print(s)      

def eval(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    else:
        return a / b
kq = eval(1, 2, "-")
print(kq)  

    

    





