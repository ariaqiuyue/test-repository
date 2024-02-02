def calculate_factorial(number):
    # 处理边界情况
    if number < 0:
        print("Error message")
        return None
    elif number == 0:
        return 1

    # 初始化阶乘结果为 1
    factorial_result = 1

    # 使用循环计算阶乘
    for i in range(1, number + 1):
        factorial_result *= i

    return factorial_result

# 测试函数
print(calculate_factorial(5))  # 应该返回 120
print(calculate_factorial(0))  # 应该返回 1
print(calculate_factorial(3))  # 应该返回 6
print(calculate_factorial(-1))  # 应该打印错误信息并返回 None
