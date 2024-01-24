my_list = [1, 'Hello', 3.14]
print(my_list)
print(my_list[0]) #注意python里的数字是从0开始算，数数第一个是0

nested_list = [[1,2,3], [4,5,6], [7,8,9], ["hello", "world"]]
print(nested_list)
print(nested_list[-1]) #倒着数就没有0占位了
print(nested_list[0][0])

fruits = ["apple", "banana", "orange"]
message = "my favorate fruit is {}".format(fruits[2]) #发现用f+{}的话需要提前定义，.format就可以用index里的内容，以后用这个
print(message)

fruits.append("mango") #在index末尾添加

fruits.insert(1, "kiwi") #在列表中间任选位置插入新东西
print(fruits)

other_fruits = ["cherry", "pear"]
fruits.extend(other_fruits) #在一个列表末尾加上另一个列表
print(fruits)

fruits.remove("pear")
fruits.pop(3) #可以确定删除目标
print(fruits)
del fruits[0] #可以确定删除目标
print(fruits)

fruits.clear()
print(fruits)

numbers = [2, 3, 1, 5, 9, 2, 1, 8]
sorted_numbers = sorted(numbers) #此方案不会改变原始数据的排序
print(sorted_numbers)

numbers.sort()
print(numbers) #此方案会改变原始数据的排序

numbers.reverse()
print(numbers)

fruits = ["apple", "banana", "orange", "kiwi"]
fruits.sort(key=len) #key=表示按什么样的顺序排，len代表依照字母长度排序
print(fruits)

