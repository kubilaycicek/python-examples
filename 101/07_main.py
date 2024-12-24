number1 = int(input("Number 1 = "))
number2 = int(input("Number 2 = "))
operation = input("Select a operation = ")

result = 0

if operation == "+":
    result = number1 + number2
elif operation== "-":
    result = number1 - number2
elif operation== "*":
    result = number1 * number2  
elif operation== "/":
    result = number1 / number2            

print("Result = {}".format(result))    