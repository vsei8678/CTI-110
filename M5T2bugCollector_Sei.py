# CTI-110
# M5T2: Bug Collector
# Vincent Sei
# October 21, 2017

numberofDays = 7
totalBugsCollected = 0

for day in range(1, numberofDays + 1):
    bugsCollected = int(input("How many bugs were collected for the day " +\
                                    str(day) + ": "))
    totalBugsCollected  += bugsCollected  
print("Total number of bugs collected for all", numberofDays, "days is", \
       totalBugsCollected ) 
