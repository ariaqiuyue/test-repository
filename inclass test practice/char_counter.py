def case_counter(text):
    
    upper_count = 0
    lower_count = 0
    
    
    for char in text:
        if char.isalpha():
          
            if char.isupper():
                upper_count += 1
            
            elif char.islower():
                lower_count += 1
        else:
            upper_count += 0
            lower_count += 0
    
    
    return upper_count, lower_count


input_text = input("please enter words：")
uppercase_count, lowercase_count = case_counter(input_text)

print("Uppercase letters：", uppercase_count)
print("lowercase letters：", lowercase_count)