# CTI-110
# M2HW2 (Module 2, Homework 2) - Tip, Tax, and Total
# Vincent Sei
# September 2, 2017

# Program calculates the total cost of a meal purchased at a restaurant.

foodCost = float(input("please enter the charge of the food:"))
tipAmnt = 0.18*foodCost
salesTax = 0.07*foodCost
totalCost = foodCost+tipAmnt+salesTax
print("foodCost:$"+format(foodCost,",.2f"),"tipAmnt:$"+format(tipAmnt,",.2f"),\
      "salesTax:$"+format(salesTax,".2f"),\
      "totalCost:$"+format(totalCost,",.2f"),sep="\n")
      
