# from datetime import date , time , datetime
# today_date = date.today()
# print("Today's date is" , today_date)
# current_time = datetime.now()
# print("Today's date is" , current_time)

#calender
import calendar
y = int(input('Enter the year: '))
m = int(input('Enter the month: '))
print(calendar.month(y , m))
