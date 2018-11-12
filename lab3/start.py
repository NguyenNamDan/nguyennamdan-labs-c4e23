a = int(input("a = "))
b = int(input("b = "))

op = input("operation(+,-,*,/): ")
if op == "+":
    print(a, "+", b, "=", a + b)
elif op == "-":
    print(a, "-", b, "=", a - b)
elif op == "*":
    print(a, "*", b, "=", a * b)
else:
    print(a, "/", b, "=", a / b)