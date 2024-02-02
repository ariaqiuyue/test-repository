def is_leap_year(year):
    if year % 4 == 0:  # 如果年份能被4整除
        if year % 100 == 0:  # 如果年份是世纪年
            if year % 400 == 0:  # 如果是世纪年且能被400整除
                return True  # 是闰年
            else:
                return False  # 不是闰年
        else:
            return True  # 不是世纪年但能被4整除，是闰年
    else:
        return False  # 不能被4整除，不是闰年
    #整个是外到里一层一层对应的
    # = 用于赋值，而 == 用于比较相等性