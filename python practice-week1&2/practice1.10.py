print("hello, world")
print("good good study, day day up") #study hard work hard make money more and more
"""
Study hard work hard make money more and more
Eat well sleep well have fun day by day
"""
print("Lucky")
age=22
print(age)

greeting = "Hello"
name = "John"
Full_greeting = greeting + " " + name
print(Full_greeting)

new_greeting = Full_greeting. replace("John", "Jane")
print(new_greeting)

Laugh = "ha"
print(Laugh*3)

Data = "Apple, Banana, Orange"
fruit = Data.split(",")#这里split后面的括号是告诉用什么格式拆分
print(fruit)

sentence = ",".join(fruit)#此处“”里面的格式同样是组合后呈现的格式示范
print(sentence)

message = "Hello, {}. Your are {} years old." . format(name, age)
print(message)

Message = f"hello, {name}. You are {age} years old."
print(Message)

print(round(2.4893479, 2))

import math
square_root = math. sqrt(16)
print(square_root)


import random
random_integer = random. randint(1,10)
print(random_integer)

def roll_dice():
    return random. randrange(1,7)
print(roll_dice())

