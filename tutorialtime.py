import math

SECTOHOUR = 0.0002777778
MINTOHOUR = 0.0166666667

def askInput():

    timearray = []

    #input function always returns string so convert to int
    hour = int(input("\nPlease input the Hours for the tutorial or enter -1 to quit.\n"))

    if hour == -1:
        return 0
    else:
        minute = float(input("Minutes: "))
        sec = float(input("Seconds: "))
        getHour = converttohour(hour,minute,sec)
        dt = doubleTime(getHour)
        timearray.append(dt)

    return timearray

def converttohour(hour,minute,sec):
    regTime = hour + minute*MINTOHOUR + sec*SECTOHOUR
    return regTime

def doubleTime(regTime):
    x2 = input("Do you want to double the time? (y/n) ")
    if x2 == "y" or x2 == "Y":
        x2time = 2 * regTime
        return x2time
    else:
        return regTime

def main():
    #calculate tutorial hours


    index = 0
    total = 0

    hours = askInput() 
    
    while hours != 0 and len(hours) > 0:
        total += hours[index]
        hours = askInput()

    calcmin = float(total % 1) / 60
    print("This tutorial will take you", int(total), "hours and", calcmin, "minutes to finish\n")
    print("goodbye")

    return 0

main()
