def fibonacci_sequence(max_value):
    sequence_outcome = []
    a, b = 0, 1
    if max_value < 0:
        print("Error: enter positive number")
        return None #这里不仅要打印错误也要记得实际终止
    else:
        while b <= max_value:
            sequence_outcome.append(b)
            a, b = b, a + b
        return sequence_outcome

print(fibonacci_sequence(10))
print(fibonacci_sequence(-5))
