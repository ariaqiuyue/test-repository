def toggle_light(light_on):
    if light_on:
        light_on = False
        print("light turned off.")
    else:
        light_on = True
        print("light turned on.")
    return light_on

toggle_light(True)

def add(num1, num2):
    return num1 + num2

def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divid(num1, num2):
    return num1 + num2

def calculator():
    print("select operation:")
    print("1, add")
    print("2,subtract")
    print("3, multiply")
    print("4, divide")

    choice = input ("enter choice (1/2/3/4): ")

    num1 = float(input("enter fist number"))
    num2 = float(imput("enter second number"))

    if choice == "1":
        print("result: ", add (num1, num2))
    elif choice == "2":
        print("result:", subtract(num1, num2))
    elif choice == "3":
        print("result:", multiply(num1, num2))
    elif choice == "4":
        print("result:", divid(num1, num2))
    else:
        print("invalid input") 

    calculator()



