from random import *
from namdan import eval
def generate_quiz():
    x = randint(0, 10)
    y = randint(0, 10)
    ero = randint(-2, 2)
    o = choice(["+", "-", "*", "/"])
    result = eval(x, y, o) + ero
    return x, y, o, result, ero
def check_answer(x, y, o, result, user_choice):
    a, b, op, result, eror = generate_quiz() 
    print(a, op, b, "= ", r)  
    user_choice = input("Y/N?").lower() 
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
    pass
