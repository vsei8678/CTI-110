
# CTI-110
# M6HW1: Test Average and Grades
# Vincent Sei
# November 11, 2017

def main():

# Declare Variables

    test1 = 0
    test2 = 0
    test3 = 0
    test4 = 0
    test5 = 0
    average = 0

# Ask user to enter test grades

    test1 = float(input("Please enter test 1 grade: "))
    test2 = float(input("Please enter test 2 grade: "))
    test3 = float(input("Please enter test 3 grade: "))
    test4 = float(input("Please enter test 4 grade: "))
    test5 = float(input("Please enter test 5 grade: "))

    

# Calculate average test grade

    average = calc_average(test1, test2, test3, test4, test4)
 
# Format and display the result


    print("\nTest Grade\tLetter Grade")
    
    print("======================================")
    print("test 1 :\t", test1, "\t\t", determine_grade(test1))
    print("test 2 :\t", test2, "\t\t", determine_grade(test2)) 
    print("test 3 :\t", test3, "\t\t", determine_grade(test3)) 
    print("test 4 :\t", test4, "\t\t", determine_grade(test4)) 
    print("test 5 :\t", test5, "\t\t", determine_grade(test5)) 
    print("======================================")

    print("Average Score:\t", average, "\t\t", determine_grade(average))
    
def calc_average(test1, test2, test3, test4, test5):
    return (test1 + test2 + test3 + test4 + test5) / 5.0

def determine_grade(testGrade):
    if testGrade >= 90:
       return "A"
    elif testGrade >= 80:
        return "B"
    elif testGrade >= 70:
        return "C"
    elif testGrade >= 60:
        return "D"
    else:
        return "F"
    
main ()






                    

                    


