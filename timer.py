import time

# determine the Meeting date
print("Input meeting date in formate DD.MM.YYYY")
time_string = input()
print("Input meeting time in formate HH:MM or just press Enter to set time 12:00")
date_string = input()
if date_string == "":
    date_string = "12:00"
datetime = time_string + " " + date_string

t = time.strptime(datetime, "%d.%m.%Y %H:%M")
result = time.mktime(t)

print("Meeting date:", time_string)

# determine the local date
named_tuple = time.localtime()
nowPrint = time.strftime("%d %B, %Y %H:%M", named_tuple)

print("Your local time:", nowPrint)

# Count
localNum = int(round(time.time()))

seconds_remain = int(result)
countback = abs(localNum - seconds_remain)

# Captain Obvious
second, minute = 1, 60
hour = 60 * minute
day = 24 * hour
#
print("\n")

days = countback // day
if days != 0:
    print("Whole days to the meeting:", days)

hours = countback // hour
if hours != 0:
    print("Whole hours to the meeting:", hours)

minutes = countback // minute
if minutes != 0:
    print("Whole minutes to the meeting:", minutes)

seconds = countback // second
if seconds !=0:
    print("Whole seconds to the meeting:", seconds)

# Time to meeting
hrsTo = (countback % day) // hour
minTo = (countback % hour) // minute
secTo = (countback % minute)
print("It remains quite a bit:", days, "days,", hrsTo,
      "hours,", minTo, "minutes,", secTo, "seconds.")