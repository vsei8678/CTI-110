# CTI-110
# M5HW1: Distance Traveled
# Vincent Sei
# October 16, 2017

speedVehicle = float(input("What is the speed of the vehicle in mph?: "))
timeTraveled = int(input("How many hours has it traveled?: "))

print("\nHour", "\t Distance Traveled")
print("-" * 26)
for Hour in range(1,timeTraveled+1):
        distanceTraveled = speedVehicle*Hour
        print(Hour, "\t", distanceTraveled)
