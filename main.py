# Phillip Hajjar
# Sprint 2 of Integration project
# This program will provide examples of standard conditional and iterative structures,
# the definition of functions, and parameter passing
import time
import math

sprint_1 = input("If you would like to see the first sprint of"
                 "The Student Guide for Success in Python Handbook, type yes:   ")
if sprint_1 == 'yes':
    print("Welcome to The Student Guide for Success in Python Handbook")
    # print is the function that prints the specific message on the screen
    input1 = float(input("Input a whole number >10:  "))
    # input is the function that allows to reader to input a value
    if input1 < 10:
        # if statements decide whether certain statements need to be executed or not.
        print('That number was less than 10:(')
        exit()
        # exit kills program
    input2 = float(input("Input a whole number <3:  "))
    if input2 > 3:
        print('That number was greater than 3:(')
        exit()
    a = int(input1)
    b = int(input2)
    # Tyler gave great advice to make an if statement is someone inputs a value less than 10, it'll print the statement
    # 'That number was less than 10:(' and then kill the program above we turned the input value into an integer
    # therefore we can use basic calculations on the inputs
    print("Below i will demonstrate numeric operators and their functions with two values of your choice.")
    print(
        "The first numeric operator we will use is '**' which is known as exponentiation, it places 'a' to the power "
        "of 'b'")
    print("a**b = ", a ** b)
    time.sleep(2)
    # this is an example of Exponentiation
    print(
        '________________________________________________________________________________________________')
    print(
        "The next numeric operator we will use is '*', unlike the operator above, this operator is just "
        "multiplication of 'a' and 'b'")
    print("a*b = ", a * b)
    time.sleep(2)
    # this is an example of Multiplication
    print(
        '_____________________________________________________________________________________________')
    print("Our next numeric operator is '/', this operator divides your two values by each other")
    print("a/b = ", a / b)
    time.sleep(2)
    # this is an example of division
    print(
        '______________________________________________________________________________________________')
    print("Our next numeric operator is '%', at first I believed this was a way to divide two values.")
    print(
        "Instead the '%' numeric operator is called the Modulus, which is the remainder of the division of 'a' value "
        "by the 'b'.")
    print("a%b = ", a % b)
    time.sleep(2)
    # this if an example of Modulus
    print(
        '_______________________________________________________________________________________________')
    print("The next numeric operator we are going look at is '//' which is called floor division.")
    print(
        "Floor division(which always results in a whole number)follows normal division rules, but it rounds down to "
        "the nearest whole number with no remainder.")
    print("a//b = ", a // b)
    time.sleep(2)
    # this is an example of floor division
    print(
        '________________________________________________________________________________________________')
    print(
        "The next two numeric operators are very simple to grasp, these are the adding and subtracting operators, "
        "these look like '+' and '-'.")
    print("They do example what you would think, add and subtract.")
    print("a+b = ", a + b)
    print("a-b = ", a - b)
    time.sleep(2)
    # these are the adding and subtracting operators
    print(
        '_______________________________________________________________________________________________')
    # below I will demonstrate string operators such as '+' and '*' with users name
    print("Now i will demonstrate string operators and their functions")
    firstname = input("Input your first name:  ")
    lastname = input("Input your last name:  ")
    # Here I asked the user to input their first and last name
    print("Thank you " + firstname + "!!!")
    time.sleep(2)
    print(
        '_________________________________________________________________________________________________________')
    print("The two string operators we will look at in this handbook is '*' and '+'.")
    print(
        "At first I thought these operators had the same function as above, but they dont. They are similar although "
        "are not the same.")
    print("The '+' operator combines the two strings into one string.")
    print("For example: your firstname + your last name = ", firstname + lastname)
    time.sleep(2)
    # Here I used an example of the '+' string operator
    print(
        '____________________________________________________________________________________________________')
    print("The '*' operator does not multiply the strings, but copies them ,x, many times.")
    print("For example: your firstname*10 = ", firstname * 10)
    time.sleep(2)
    # Here I used an example of the '*' string operator
    print(
        '______________________________________________________________________________________________________')
    print(" Now i will explain the 'sep' and 'end' arguments in print statements")
    print("The end parameter is used to append any string at the end of the output of the print statement in python.")
    print("For example: this is the outcome of the 'end' argument: ")
    print("your first name is " + firstname, end='\n')
    print(lastname)
    print("the 'end' argument moved your last name to the next line")
    time.sleep(2)
    # here I used and explained the end argument
    print(
        '_________________________________________________________________________________________________________')
    print("the 'sep' argument passed to the program can be separated by different values.")
    print("For example: your first name + your last name separated with a hi looks like:")
    print("(firstname),(lastname),sep='hi'")
    print(firstname, lastname, sep=' hi ')
    time.sleep(2)
    # here I used and explained the sep argument
    print('___________________________________________________________________')
else:
    print("Welcome to Sprint two of the Integration Project")
print("We will begin sprint two of The Student Guide For Success in Python Handbook with shortcut operators")
print("Shortcut operators are used to do simple mathematics equations in a shorter amount of time")
number_one = int(input("For example, input a whole numbers:  "))
# here I asked for a whole number to use in later lines of code
number_two = int(input("Perfect, input a second whole number:  "))
# here I asked for another whole number to use in later lines of code
print("Thank you!!! ill use the '+=' operator as an example.")
count = number_one
count += number_two
# The += operator is a shortcut operator
print("Number one += Number two ==", count)
time.sleep(2)
# time.sleep(2) makes the program run in section every 2 seconds. The 2 seconds comes
# from what I input into the parenthesis
print('____________________________________________________________')
print("Now I will explain if, elif, and else statements. These are my favorite to use!")
print("If statements are used to guides a program to make decisions based on specified criteria. The IF statement ")
print("executes one set of code if a specified condition is met (TRUE) or another set of code evaluates to FALSE.")
# I got this information from Corporate Finance Institution
print("If-Else statements are used if something can either be true or false. The computer will check to see if the ")
print("information inside the if statement is true. If it is not true, it'll skip to the else statement and run that ")
print("code. If there is no else statement, the computer will just skip the if statements and go to next line of code ")
time.sleep(2)
print('____________________________________________________________')
print("An example of an if statement would be, if I asked you your age, and if your age is less than 18, "
      "I print 'child', but if your age is greater than 18, I print 'adult'.")
age = int(input("What is your age?:  "))
if age < 18:
    print("your a baby")
elif age >= 18:
    print("your a adult")
else:
    print("I dont know your age:(")
# this is an example of an if statement
time.sleep(2)
print('____________________________________________________________')
print("Next we will discuss, Relation Operators. This section will be super short. Ill use your previous numbers for "
      "the example")
print("Relation Operators are used for comparing the values.")
print("The main Relation Operators are ==, !=, >, <, <=, and >=")
time.sleep(2)
print('____________________________________________________________')
compare_one = number_one + number_two
# here I used to value the user input in earlier code
print("The first one we will use is '=='")
# == mean is equal too
print("number one + number two ==: ", compare_one)
time.sleep(2)
print('____________________________________________________________')
print("The next operator we will use is !=")
# != means is not equal too
print("number_one + number_two != 102938:  ", number_one + number_two != 102938)
time.sleep(2)
print('____________________________________________________________')
print("The next operator we will use is >=")
# >= means greater than or equal too
print("number_one >= number_two:  ", number_one >= number_two)
time.sleep(2)
print('____________________________________________________________')
print("Next we will take a look at Boolean Operators, these are used to check and see if a expression is true or false")
print("The Boolean Operators are not, and, and or")
print("The operator 'not' will return a value of true of false depending on your number one and two values.")
print("number_one is not number_two:  ", number_one is not number_two)
# is not operator means exactly what it looks like
time.sleep(2)
print('____________________________________________________________')
print("The operator 'and' will return a value of true or false depending on your code")
print("For example, number one > 1 and number two < 100: ", number_one > 1 and number_two < 100)
# and evaluates both and if both aren't correct, its false
time.sleep(2)
print('____________________________________________________________')
print("The operator 'and' will, you guessed it return a value of true or false depending on your code")
print("For example, number one > 1 or number two < 100: ", number_one > 1 or number_two < 100)
# or evaluates both and if at least 1 is correct it is true
time.sleep(2)
print('____________________________________________________________')
print("Next we will be discussing, in my opinion, the most difficult")
print("of programming, Standard iterative structures(loops)")
time.sleep(2)
print('____________________________________________________________')
print("The fist type of loop we will look at are While Loops!!!")
print("While loops are defined as a control flow statement which allows code to be executed repeatedly, depending on "
      "whether a condition is satisfied or not. As long as some condition is true, 'while' repeats everything inside "
      "the loop block. It stops executing the block if and only if the condition fails.")
# got this information from study.com
time.sleep(2)
print('____________________________________________________________')
print("A example of a while loop could be me giving you 3 trys to guess a letter, the letter will be 'a'. but the "
      "while loop allows us to run a certain code a fixed amount of times(3)")
x = 0
while x < 3:
    x = x + 1
    letter = input("Pick a letter(answer is 'a')")
    if letter == 'a':
        print('Correct you Got it!!!!')
    else:
        print("try again :(")
        # This is an example of a While loop
time.sleep(2)
print('____________________________________________________________')
print("The next type of loop we will look at is For Loops!!!")
print("For loops are a set of instructions that is repeated, or iterated, for every value in a sequence. Sometimes "
      "for-loops are referred to as definite loops because they have a predefined begin and end as bounded by the "
      "sequence.")
time.sleep(2)
print('____________________________________________________________')
print("An example of a for loop could look like this ")
print("x = 0")
print("for i in range (3)")
print("sum = sum + 1")
print('sum')
total_loop = 0
# below is a for loop, but it has a range function as well. That function ranges from 0,1, and 2.
for i in range(3):
    total_loop = total_loop + 1
    print(total_loop)
print("See, this programs simply adds up by one for 3 iterations.")
time.sleep(2)
print('____________________________________________________________')
print("Now we will discuss function definitions, these are used to create or define a function")
print('A function definition could be used to determine the area of a circle and its diameter with a radius of your '
      'choosing')
print("First you would define how to calculate area, then you go to define the main function where you grab the users "
      "inputs and print the information needed.")
print("In this case the definition of calculateArea is needed in the main function so, that function is called to get "
      "the value of area.")
print("The lone 'main()' at the bottom is the glue to this whole program, without it the program will not run.")


# def is used to define (calculateArea) so when it is called in the main function, it has a value
def calculateArea(radius):
    area = pow(radius, 2) * math.pi
    return area


def main():
    radius = (int(input("choose a number between 1 and 10:  ")))
    diameter = radius * 2
    print(float(format(calculateArea(radius), '.2f')))
    print(format(diameter, '.2f'))


# this is my code from hackerrank
# main() is how we work out way into the defined main() function, without it, the whole code would not run
main()
time.sleep(2)
print('____________________________________________________________')
print("I'd like to thank you participating in The Student Guide For Success in Python Handbook!!!")
print("I hope that enjoyed the activities and i hope that you now have a better grasp on python programming.")
print("*I would like to thank Professor Osheroff for providing his students with all the means necessary to be "
      "successful in the beginning stages of Computer Science")
print("*I would also like to thank our Teaching Assistant Tyler for the amazing advice which helped me kick start "
      "this Student Guide for Success in Python Handbook")
