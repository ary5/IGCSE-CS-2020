import time, math

Day = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
PPH = [2,10,10,10,10,10,3]
MaxStay = [8,2,2,2,2,2,4]
Available = ["8","9","10","11","12","13","14","15","16","17","18","19","20","21","22","23"]
TotalPrice = 0
moduloloop = 1
hourloop = 1
frequentloop = 1
enoughPaid = 1
verify = 0
Frequent = False
dayloop = 0
totalRev = 0

#day input

DayIn = input("Enter the day: ")
DayIn = DayIn[0].upper() + DayIn[1:].lower()
while DayIn not in Day:
    DayIn = input("Invalid input, please try again: ")
    DayIn = DayIn[0].upper() + DayIn[1:].lower()
order = Day.index(DayIn)

#arrival input
while dayloop == 0:
    moduloloop = 1
    hourloop = 1
    frequentloop = 1
    verify = 0
    enoughPaid = 1
    Frequent = False
    print("Enter time of arrival in the 24 hour system")
    print("An example would be 8 for 8 AM and 16 for 4 PM")
    Arrival = input("--> ")
    while (Arrival) not in Available:
      print("Input not valid, try again")
      Arrival =  input("-->")
      
    print("Do you have a frequent parking number? Enter 'Y' or 'N'")
    ParkNum = input("--> ")
    while frequentloop == 1:
      if ParkNum[0].lower() == "y":
        while moduloloop == 1:
          checkdigit = input("Enter your parking number: ")
          total = 0
          digit = False
          while digit == False:
            if (checkdigit.isdigit() == True) or  (checkdigit[0:3].isdigit() == True and checkdigit[4] == "X"):
                while len(checkdigit) != 5:
                    print("Invalid input")
                    print("Would you like to try again?")
                    again = input("-->")
                    if again[0].lower() == "n":
                      Frequent = False
                      moduloloop = 0
                      frequentloop = 0
                      break
                    else:
                      checkdigit = input("Enter your parking number: ")
                digit = True
            else:
                print("Invalid input")
                print("Would you like to try again?")
                again = input("-->")
                if again[0].lower() == "n":
                  Frequent = False
                  moduloloop = 0
                  frequentloop = 0
                  break
                else:
                  checkdigit = input("Enter your parking number: ")
          for x in range(4):
            total = total +  int(checkdigit[x]) * (x+2)

          check = str(total%11)

          if check == "10":
            check = "X"

          if checkdigit[4] != check:
            print("Parking number not accepted")
            print("Would you like to try again?")
            again = input("--> ")
            if again[0].lower() == "n":
              Frequent = False
              moduloloop = 0
              frequentloop = 0
              break
            else:
              print("Resetting")
              time.sleep(0.5)
          else:
            print("Parking number accepted")
            Frequent = True
            moduloloop = 0
            frequentloop = 0
      elif ParkNum[0].lower() == "n":
        Frequent = False
        frequentloop = 0
      else:
        ParkNum = input("Invalid input, please enter Y or N: ")


    while hourloop == 1:
      Hours = input("Enter the time you will stay in hours: ")
      if int(Arrival) >= 16:
        if (Hours.isdigit() == True) and (int(Arrival)+ int(Hours) <= 24):
          if Frequent == False:
            TotalPrice = 2
            hourloop = 0
          elif Frequent == True:
            TotalPrice = 1
            hourloop = 0
        else:
          print("Invalid input, please try again")
          
      elif int(Arrival) + int(Hours) > 16:
          if Frequent == False:
             TotalPrice = (16 - int(Arrival))*PPH[order]
             TotalPrice = TotalPrice + 2
             hourloop = 0
          if Frequent == True:
              TotalPrice = ((16 - int(Arrival))*PPH[order])*0.9
              TotalPrice = TotalPrice + 1
              hourloop = 0
      else:
        if (Hours.isdigit() == True) and int(Hours) <= MaxStay[order]:
          if Frequent == False:
            TotalPrice = int(Hours) * PPH[order]
            hourloop = 0
          else:
            TotalPrice = 0.9 * (int(Hours) * PPH[order])
            hourloop = 0
        elif (Hours.isdigit() == True) and Hours != MaxStay[order]:
          print("The maximum stay for",Day[order],"is",MaxStay[order],"hours")
        else:
          print("Invalid input, please try again")

    leave = int(Arrival) + int(Hours)

#Display

    print("Day:", DayIn)
    print("Time arrived:", Arrival)
    print("Hours staying:", Hours)
    print("Time leaving:", leave)
    if Frequent == True:
      print("Discount applied")
      if int(Arrival) >= 16:
        print("Price before discount: 2")
        print("Price after discount:", TotalPrice)
      else:
        print("Price after discount:", TotalPrice)
    else:
      print("No discount applied")
      print("Your price is:", TotalPrice)
    while enoughPaid == 1:
        paid = float(input("How much will you pay"))
        if paid >= TotalPrice:
            enoughPaid = 0
            totalRev = totalRev + paid
        if paid < TotalPrice:
            print("The amount you have entered is less than the price")
    dayEnd = input("Has day ended? Enter Y or N")
    if dayEnd == "Y":
        dayloop = 1
        print("Total revenue for today is", totalRev)
