import time

print("Input 'start' to start a programm")
start = input()
#while 
while start == "start":
    #file_check = open("lastDate.txt", 'r')
    #if file_check 

        # determine the Meeting date
    print("Input meeting date in formate DD.MM.YYYY")
    time_string = input()
    print("Input meeting time in formate HH:MM or just press Enter to set time 12:00")
    date_string = input()
    if date_string == "":
        date_string = "12:00"
    datetime = time_string + " " + date_string

    t = time.strptime(datetime, "%d.%m.%Y %H:%M")
    print("Meeting date:", time_string)

    # determine the local date
    nowPrint = time.strftime("%d %B, %Y %H:%M", time.localtime())
    print("Your local time:", nowPrint)

    # Count
    localNum = int(round(time.time()))

    seconds_remain = int(time.mktime(t))
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
    if days != 0 and hours != 0:
        print("Whole hours to the meeting:", hours)

    minutes = countback // minute
    if days != 0 and hours != 0 and minutes != 0:
        print("Whole minutes to the meeting:", minutes)

    seconds = countback // second
    if days != 0 and hours != 0 and minutes != 0 and seconds != 0:
        print("Whole seconds to the meeting:", seconds)

    # Time to meeting
    hrsTo = (countback % day) // hour
    minTo = (countback % hour) // minute
    secTo = (countback % minute)
    print("It remains quite a bit:", days, "days,", hrsTo,
      "hours,", minTo, "minutes,", secTo, "seconds.")

    # Save last date
    print("Do you want to save last meeting date?")
    print("Press 'save' to save or just press Enter to continue:")
    save_file = input()
    if save_file == "save":
        myFile = open("lastDate.txt", 'w')
        myFile.write(datetime)
        myFile.close()
    #end
    end = input("Press 'q' to quit or just press Enter to continue: ")
    if end =="q":
        break
    else:
        break
#elif start == "exit":
#
#else :
    #print("Unknown input, pless try one more time")