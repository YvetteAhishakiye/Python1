#Write a program starting with these three lines that asks the user for their homework grade, exam grades, and discussion grades and prints out their total grade in the class
homework = float(input("Enter your homework grade: "))
print(type(homework))
hw_weight = homework * 0.4
Exam = float(input("Enter your Exam grade: "))
Exam_weight = Exam * 0.5
Discussion = float(input("Enter your discussion grade: "))
Discussion_weight = Discussion * 0.1
Total_grade = Discussion_weight + Exam_weight + hw_weight
print(f"The total weighted grade for you is: {Total_grade} " )

#Write a Python program that assigns the principal amount of $10000 to variable P, assign to n the value 12, and assign to r the interest rate of 8%. Then have the program prompt the user for the number of years t that the money will be compounded for. Calculate and print the final amount after t years
p = 10000
N = 12
R = 0.08
t = float(input("Enter number of years: "))
amount = p * (1 + R / N) ** (N * t)
print(f" The final amount is {amount}")

#Write a function called calculateGPA that takes a numerical score (out of 100) and returns the GPA. See Ashesi grading policy for the scores and their GPAs.
# Write another function called getHonours that takes a GPA and returns the corresponding honours.

def calculateGPA():
    score = float(input("Enter your math score: "))

    if 80 <=score <= 100:

        return "4.0"

    elif 75 <= score < 80:

        return "3.5"

    elif 70 <= score < 74:

        return "3.0"

    elif 65 <= score < 69:

        return "2.50"

    elif 60 <= score < 65:

        return "2.0"

    elif 55 <= score < 59:

        return "1.5"

    elif 50 <= score < 54:

        return "1.0"

    else:

        return 0.0


gpa = calculateGPA()

gpa = float(gpa)

print(f'your gpa is: {gpa} ')


def getHonours():
    calculateGPA()

    if 3.85 <= gpa <= 4.0:

        return " Summa cumma laude"

    elif 3.70 <= gpa <= 3.84:

        return "Magna Cumma laude"

    elif 3.50 <= gpa <= 3.69:

        return "cumma laude"

    else:

        return "none"


honors = getHonours()

print(f' your honor is {honors}')

#Write a Python program that calculates the area of a circle based on the radius entered by the user.
radius = float(input("Enter the radius: "))
import math
Pi = math.pi
Area = Pi * (radius)**2
print(f'the area is {Area}')

# Write a function named is_triangle that takes three integers as arguments, and that returns either True or False depending on whether you can or cannot form a triangle from sticks with the given lengths.
# Write a function that prompts the user to input three stick lengths, converts them to integers, and uses is_triangle to check whether sticks with the given lengths can form a triangle. It then prints an appropriate message giving the answer to the user. (3 marks)

def is_triangle(a, b, c):
    if a+b<c or a+c<b or b+c<a :
        return False
    else:
        return True
    is_triangle(a, b, c)
def input_Lengths():
    a = float(input("Enter the first number: "))
    b = float(input("Enter the second number: "))
    c = float(input("Enter the third number: "))
    result= is_triangle(a, b, c)

    if result:
        print("A triangle can be formed")
    else:
        print("A triangle can not be formed")
input_Lengths()
