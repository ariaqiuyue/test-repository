import datetime

def date_passed(todays_date, scheduled_date):
    if todays_date < scheduled_date:
        return print("date is yet to pass")
    if todays_date == scheduled_date:
        return print("date is today")
    else:
        return print("date has passed")
    
    
print(date_passed("26th March", "25th March"))
print(date_passed("26th March", "26th March"))
print(date_passed("26th March", "27th March"))

    
   

# Test cases
date_passed("26th March", "25th March")  # Expected: Scheduled date has passed
date_passed("26th March", "26th March")  # Expected: Scheduled date is today
date_passed("26th March", "27th March")  # Expected: Scheduled date is yet to pass
