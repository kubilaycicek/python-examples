def helloWorld():
    print("Hello World!")
    
def hello(name):
    print("Hello ",name)

def sayHello(name = "kubilay"):
    print("Hello ",name)    
    

def addition(number1,number2):
    return number1 + number2

def division(number1,number2):
    return number1 / number2

hello("kubilay")
helloWorld()
sayHello()
sayHello("Sevilay")

result1 = addition(3,4)
print(result1)

result2 = division(8,4)
print(result2)


