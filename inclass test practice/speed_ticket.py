def speeding_ticket(speed, is_birthday):
    if is_birthday: #这里不能直接加上True，因为输入是文字，将永远转为False
        if speed <= 65:
            return "No Ticket"
        elif 66 <= speed <= 85:
            return "Small Ticket"
        else:
            return "Big Ticket"
    else:
        if speed <= 60:
            return "No Ticket"
        elif 61 <= speed <= 80:
            return "Small Ticket"
        else:
            return "Big Ticket"  

driving_speed = int(input("Please enter driving speed")) #补充需要是整数的要求
Birthday = input("Is the driver's birthday today? (True/False)")  
is_birthday = bool(Birthday)  #将用户输入的字符串转化为True or False

Ticket_rule = speeding_ticket(driving_speed, Birthday)
print(Ticket_rule)