# CTI-110
# M5HW2:Running Total
# Vincent Sei
# October 16, 2017

total = 0
inputNumber = float(input("Enter a number: "))
while inputNumber > -1:
    total = total + inputNumber
    inputNumber = float(input("Enter the next number: "))
print("Total: " , total)
