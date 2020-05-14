import datetime
import time

# yyyy= 2020
# M = 5
# d = 10
# h = 20
# m = 32

def unixPeriod(yyyy, M, d, h, m):
    dt = datetime.datetime(yyyy, M, d, h, m)
    unixTime = time.mktime(dt.timetuple())
    return str(unixTime)

def period(yyyy, M, d):
    return "%s-%s-%s" % (yyyy, M, d)

a = 1
b = 1
c = 1
while a == 1:
    sYear = int(input("Enter the start YEAR of the data (in form yyyy): "))
    years = range(1970, 2021)
    if (sYear not in years):
        print()
        print("enter a valid year")
        print()
        a = 1
    else:
        a = 0
while b == 1:
    sMonth = int(input("Enter the start MONTH of the data (no leading zero please): "))
    months = range(1, 13)
    if (sMonth not in months):
        print()
        print("enter a valid month")
        print()
        b = 1
    else:
        b = 0
while c == 1:
    sDay = int(input("Enter the start DAY of the data: "))
    days = range(1, 32)
    if (sDay not in days):
        print()
        print("enter a valid day")
        print()
        c = 1
    else:
        c = 0

sHour = 0
sMinute = 0

x = 1
y = 1
z = 1

while  x == 1:
    eYear = int(input("Enter the end YEAR of the data (in form yyyy): "))
    years = range(1970, 2021)
    if (eYear not in years):
        print()
        print("enter a valid year")
        print()
        x = 1
    else:
        x = 0
while y == 1:
    eMonth = int(input("Enter the end MONTH of the data (no leading zero please): "))
    months = range(1, 13)
    if (eMonth not in months):
        print()
        print("enter a valid month")
        print()
        y = 1
    else:
        y = 0
while z == 1:
    eDay = int(input("Enter the end DAY of the data: "))
    days = range(1, 32)
    if (eDay not in days):
        print()
        print("enter a valid day")
        print()
        z = 1
    else:
        z = 0
eHour = 0
eMinute = 0

sHour = 0
sMinute = 0

period1 = unixPeriod(sYear, sMonth, sDay, sHour, sMinute)
period2 = unixPeriod(eYear, eMonth, eDay, eHour, eMinute)

startDate = period(sYear, sMonth, sDay)
endDate = period(eYear, eMonth, eDay)

def monthDifference(y1, y2, m1, m2):
    diff = (y2 - y1) * 12 + (m2 - m1)
    return diff

monthDiff = monthDifference(sYear, eYear, sMonth, eMonth)
 
