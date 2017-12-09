
# November 8, 2017
# CTI-110 M6T1_KilometersToMiles
# Vincent Sei

# Write a program that asks the user to entera distance in kilometers
# and then converts that distance to miles. 
# This is the conversion formula: Miles = kilometers * 0.6214

def main():
# Declare variable
  userKilometerInput = 0
  miles = 0


  userKilometerInput = float(input("Please enter the distance in kilometers: "))

  show_miles(userKilometerInput)
def show_miles(userKilometerInput ):
  miles = userKilometerInput * 0.6214

  print(userKilometerInput," kilometers is equivalent to", \
        format(miles,".2f"),"miles")

main()
    
