# November 09, 2017
# CTI-110
# M6T2-Inches to feet converter
# Vincent Sei


# Write a program that asks the user to enter a distance in feet,
# and prints that same distance in inches.
# This is the conversion formula, of course: inches = feet * 12

def main():
    # Declare the variables
    
    feet = 0
    inches = 0


    
    # User number in feet input
    userNumberFeet = float(input("Please enter the number of feet: "))
    # output number of inches
    inches = feet_to_inches(userNumberFeet)
    print(userNumberFeet, " feet converted to inches is", format( inches,\
         ".2f"), "inches")
    
def feet_to_inches(userNumberFeet):
    inches = 12* userNumberFeet
    return inches
main()
