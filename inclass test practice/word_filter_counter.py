def word_filter_counter(text, filter_words):
    
    # 将文本中的标点符号替换为空格，并将所有单词转换为小写(因为题干中有大小写不一致的问题), .join 把句子里的间隔符号去掉（因为有的文字跟着标点符号不利于识别），.isalnum用于判断是否是数字或者字母
    cleaned_text = ''.join(char if char.isalnum() else ' ' for char in text).lower()#第一个''中间没有空格，是不加入其他东西的指代，第二个' '中间有空格意为如果内容不是文字就用空格替换
    
    # 将文本拆分为单词列表
    words = cleaned_text.split()
    
    # 初始化一个字典用于存储过滤后的单词及其出现次数
    filtered_word_counts = {}
    
    # 遍历过滤词列表
    for filter_word in filter_words:
        # 统计文本中过滤词的出现次数
        count = words.count(filter_word.lower())
        
        # 将结果添加到字典中
        filtered_word_counts[filter_word] = count
    
    # 返回结果字典
    return filtered_word_counts

# 示例测试用例
print(word_filter_counter("Hello world, hello!", ["hello"]))  # 输出: {'hello': 2}
print(word_filter_counter("The quick brown fox.", ["the"]))   # 输出: {'the': 1}
print(word_filter_counter("Is this real life? Is this just fantasy?", ["is", "this", "just"]))  # 输出: {'is': 2, 'this': 2, 'just': 1}
print(word_filter_counter("Do we see the big picture or just small details?", ["we", "the", "or"]))  # 输出: {'we': 1, 'the': 1, 'or': 1}

    

