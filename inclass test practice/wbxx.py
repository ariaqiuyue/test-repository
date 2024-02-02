def fibonacci_sequence(max_value):

    sequence_outcome = []

    a, b = 0, 1

    if max_value <= 0:
        print("error message")
        return None

    else:    

        while b < max_value:

            sequence_outcome.append(b)

            a,b = b, a+b

        return sequence_outcome    
    
print(fibonacci_sequence(10)) 

       