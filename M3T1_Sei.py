# CTI 110
# M3T1 Area of Rectangles
# Vincent Sei
# September 9, 2017

# Program asks the user for the lenght and width of two rectangles. It also
# tells the user which which rectangle has the greater area, or if the two
# rectangles have equal area.

lengthRectangle1 = float(input("Enter length of rectangle1:"))
widthRectangle1 = float(input("Enter width of rectangle1:"))
lengthRectangle2 = float(input("Enter length of rectangle2:"))
widthRectangle2 = float(input("Enter width of rectangle2:"))
areaRectangle1  = lengthRectangle1 * widthRectangle1
areaRectangle2  = lengthRectangle2 * widthRectangle2

if areaRectangle1 > areaRectangle2:
    print("\nArea of Rectangle1 is larger than Area of Rectangle2")
elif areaRectangle2 > areaRectangle1:
    print("\nArea of Rectangle2 is larger than Area of Rectangle1")
else:
     print("\nBoth rectangles have equal area")







