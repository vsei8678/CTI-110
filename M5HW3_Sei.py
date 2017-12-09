# CTI-110
# M5HW3:Factorial
# Vincent Sei
# October 16, 2017

inputNumber = int(input("Enter a nonnegative number: "))
factorial = 1
for userNumber in range(1, inputNumber+1):
    factorial = factorial * userNumber
print("The factorial of", inputNumber, "is", factorial)
