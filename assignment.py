# assignment
# a program that prompts the user to enter 2 numbers and an operator with 4 operators and perform a calculation
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))
operator = input("Enter operator: ")
if operator == "+":
    print("Result is: ",x+y)
elif operator == "-":
    print("Result is: ",x-y)
elif operator == "*":
    print("Result is: ",x*y)
elif operator == "/":
    print("Result is: ",x/y)
else:
    print("Invalid operator")