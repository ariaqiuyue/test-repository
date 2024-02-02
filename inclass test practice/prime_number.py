import math #要用数学类指令之前要放一个这个，需要顶格

def is_prime(number):
    # Step 1: Check if it's a counting number greater than 1 and not a perfect square
    if number <= 1 or not has_no_integer_square_root(number):
        return False
    
    # Step 2: Find the largest number whose square is less than the given number
    largest_square_root = math.isqrt(number) #.isqrt是求平方根
    
    # Step 3: List the prime numbers up to the largest square root
    for divisor in range(2, largest_square_root + 1): #range(start, stop[, step])
        if is_prime(divisor):
            # Step 4: Check if the number is divisible by any prime numbers
            if number % divisor == 0: #注意%是看余数！，没有余数说明被整除
                return False
    return True

def has_no_integer_square_root(num):
    sqrt_num = math.sqrt(num)
    return not sqrt_num.is_integer() #.is_integer 是判断是否为整数的方法，是则是T，否为F；前面加上not使结果反转，是整数F，不是整数T