# CTI-110
# M3HW2: Software Sales
# Vincent Sei
# September 22, 2017

# Write a program that asks the user to enter the number of packages.The program
# should then display the amount of the discount(if any) and the total purchase
# cost with the discount applied.

numberPackages = int(input("Enter the number of packages bought;"))

packagePrice = 99

if numberPackages < 10:
    discount = 0
elif numberPackages < 20:
    discount = 0.1
elif numberPackages < 50:
           discount = 0.20
elif numberPackages < 100:
           discount = 0.30
else:
           discount = 0.40
subtotal = numberPackages * packagePrice
discountAmount = discount * subtotal
total = subtotal - discountAmount
print("\n Amount of discount: $" + format(discountAmount,",.2f") + \
      "\n Total Amout: $" + format(total,",.2f"))



