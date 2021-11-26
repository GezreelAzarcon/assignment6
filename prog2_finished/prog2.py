#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)

import random

#For question number one
num1 = random.randrange(0, 99)
num2 = random.randrange(0, 99)
#For question number two
num3 = random.randrange(0, 99)
num4 = random.randrange(0, 99)
#For question number three
num5 = random.randrange(0, 99)
num6 = random.randrange(0, 99)
#For question number four
num7 = random.randrange(0, 99)
num8 = random.randrange(0, 99)
#For question number five
num9 = random.randrange(0, 99)
num0 = random.randrange(0, 99)
#For question number six
num11 = random.randrange(0, 99)
num22 = random.randrange(0, 99)
#For question number seven
num33 = random.randrange(0, 99)
num44 = random.randrange(0, 99)
#For question number eight
num55 = random.randrange(0, 99)
num66 = random.randrange(0, 99)
#For question number nine
num77 = random.randrange(0, 99)
num88 = random.randrange(0, 99)
#For question number 10
num99 = random.randrange(0, 99)
num00 = random.randrange(0, 99)

def additionQuiz():
    #Extra input validation
    while True:
        add1 = (input(f'What is {num1} + {num2}? '))
        if add1.isalpha():
            print('Numbers Only!')
        elif not add1.isdigit():
            print('Numbers Only!')
        elif add1.isdigit():
            break
    add1 = int(add1)
    ans1 = num1 + num2
    if add1 == ans1:
        print('Correct!')
        scr1 = 1
    else:
        print('Wrong!')
        scr1 = 0
    while True:
        add2 = (input(f'What is {num3} + {num4}? '))
        if add2.isalpha():
            print('Numbers Only!')
        elif not add2.isdigit():
            print('Numbers Only!')
        elif add2.isdigit():
            break
    add2 = int(add2)
    ans2 = num3 + num4
    if add2 ==  ans2:
        print('Correct!')
        scr2 = 1
    else:
        print('Wrong!')
        scr2 = 0
    while True:
        add3 = (input(f'What is {num5} + {num6}? '))
        if add3.isalpha():
            print('Numbers Only!')
        elif not add3.isdigit():
            print('Numbers Only!')
        elif add3.isdigit():
            break
    add3 = int(add3) 
    ans3 = num5 + num6
    if add3 == ans3:
        print('Correct!')
        scr3 = 1
    else:
        print('Wrong!')
        scr3 = 0
    while True:
        add4 = (input(f'What is {num7} + {num8}? '))
        if add4.isalpha():
            print('Numbers Only!')
        elif not add4.isdigit():
            print('Numbers Only!')
        elif add4.isdigit():
            break
    add4 = int(add4)
    ans4 = num7 + num8
    if add4 == ans4:
        print('Correct!')
        scr4 = 1
    else:
        print('Wrong!')
        scr4 = 0
    while True:
        add5 = (input(f'What is {num9} + {num0}? '))
        if add5.isalpha():
            print('Numbers Only!')
        elif not add5.isdigit():
            print('Numbers Only!')
        elif add5.isdigit():
            break
    add5 = int(add5)
    ans5 = num9 + num0
    if add5 == ans5:
        print('Correct!')
        scr5 = 1
    else:
        print('Wrong!')
        scr5 = 0
    while True:
        add6 = (input(f'What is {num11} + {num22}? '))
        if add6.isalpha():
            print('Numbers Only!')
        elif not add6.isdigit():
            print('Numbers Only!')
        elif add6.isdigit():
            break
    add6 = int(add6)
    ans6 = num11 + num22
    if add6 == ans6:
        print('Correct!')
        scr6 = 1
    else:
        print('Wrong!')
        scr6 = 0
    while True:
        add7 = (input(f'What is {num33} + {num44}? '))
        if add7.isalpha():
            print('Numbers Only!')
        elif not add7.isdigit():
            print('Numbers Only!')
        elif add7.isdigit():
            break
    add7 = int(add7)
    ans7 = num33 + num44
    if add7 == ans7:
        print('Correct!')
        scr7 = 1
    else:
        print('Wrong!')
        scr7 = 0
    while True:
        add8 = (input(f'What is {num55} + {num66}? '))
        if add8.isalpha():
            print('Numbers Only!')
        elif not add8.isdigit():
            print('Numbers Only!')
        elif add8.isdigit():
            break
    add8 = int(add8)
    ans8 = num55 + num66
    if add8 == ans8:
        print('Correct!')
        scr8 = 1
    else:
        print('Wrong!')
        scr8 = 0
    while True:
        add9 = (input(f'What is {num77} + {num88}? '))
        if add9.isalpha():
            print('Numbers Only!')
        elif not add9.isdigit():
            print('Numbers Only!')
        elif add9.isdigit():
            break
    add9 = int(add9)
    ans9 = num77 + num88
    if add9 == ans9:
        print('Correct!')
        scr9 = 1
    else:
        print('Wrong!')
        scr9 = 0
    while True:
        add0 = (input(f'What is {num99} + {num00}? '))
        if add0.isalpha():
            print('Numbers Only!')
        elif not add0.isdigit():
            print('Numbers Only!')
        elif add0.isdigit():
            break
    add0 = int(add0)
    ans0 = num99 + num00
    if add0 == ans0:
        print('Correct!')
        scr0 = 1
    else:
        print('Wrong!')
        scr0 = 0

    #Every question have an scr(score) value. 
    #If the scr value is 1 then it is correct, if 0 then it is wrong.
    #The program then gets the sum of all scr numbers of each question.
    scr = scr1 + scr2 + scr3 + scr4 + scr5 + scr6 + scr7 + scr8 + scr9 + scr0
    return scr

scr = additionQuiz()
#The scr(score) values' total is the total score.
print(f'Your score is {scr}/10')









