import time

#determine the Meeting date

print("Input meeting date in formate DD.MM.YYYY HH:MM")
time_string = input()

t = time.strptime(time_string, "%d.%m.%Y %H:%M")
result = time.mktime(t)

print("Meeting date:", time_string)

#determine the local date
named_tuple = time.localtime()
nowPrint = time.strftime("%d %B, %Y %H:%M", named_tuple)

print("Your local time:", nowPrint)

#Count
localNum = int(round(time.time()))

seconds_remain = int(result)
countback = abs(localNum - seconds_remain)
    
#Captain Obvious
second = 1
minute = 60 * second
hour = 60 * minute
day = 24 * hour
#
print("\n")
days = countback // day
print("Whole days to the meeting:", days)

hours = countback  // hour
print("Whole hours to the meeting:", hours)

minutes = countback  // minute
print("Whole minutes to the meeting:", minutes)

seconds = countback // second
print("Whole seconds to the meeting:", seconds)

###Time to meeting
hrsTo = (countback % day) //hour
minTo = (countback % hour) //minute
secTo = (countback % minute)
print("It remains quite a bit:", days,"days,", hrsTo, "hours,", minTo, "minutes,", secTo, "seconds.")

