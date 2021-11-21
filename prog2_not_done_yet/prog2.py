#Create a program that automatically generate two random numbers to add (0 to 99)
#Let the user answer and evaluate if the user has the correct answer
#The program will ask the user 10 addition operation
#Display the result summary of the 10 operations (ex 9/10)
import random

num1 = random.randrange(0, 99)
num2 = random.randrange(0, 99)
num3 = random.randrange(0, 99)
num4 = random.randrange(0, 99)
num5 = random.randrange(0, 99)
num6 = random.randrange(0, 99)
num7 = random.randrange(0, 99)
num8 = random.randrange(0, 99)
num9 = random.randrange(0, 99)
num0 = random.randrange(0, 99)
num11 = random.randrange(0, 99)
num22 = random.randrange(0, 99)
num33 = random.randrange(0, 99)
num44 = random.randrange(0, 99)
num55 = random.randrange(0, 99)
num66 = random.randrange(0, 99)
num77 = random.randrange(0, 99)
num88 = random.randrange(0, 99)
num99 = random.randrange(0, 99)
num00 = random.randrange(0, 99)

def additionQuiz():
    add1 = float(input(f'What is {num1} + {num2}? '))
    ans1 = num1 + num2
    if add1 == ans1:
        print('Correct!')
        scr1 = 1
    else:
        print('Wrong!')
        scr1 = 0
    add2 = float(input(f'What is {num3} + {num4}? '))
    ans2 = num3 + num4
    if add2 ==  ans2:
        print('Correct!')
        scr2 = 1
    else:
        print('Wrong!')
        scr2 = 0
    add3 = float(input(f'What is {num5} + {num6}? '))
    ans3 = num5 + num6
    if add3 == ans3:
        print('Correct!')
        scr3 = 1
    else:
        print('Wrong!')
        scr3 = 0
    add4 = float(input(f'What is {num7} + {num8}? '))
    ans4 = num7 + num8
    if add4 == ans4:
        print('Correct!')
        scr4 = 1
    else:
        print('Wrong!')
        scr4 = 0
    add5 = float(input(f'What is {num9} + {num0}? '))
    ans5 = num9 + num0
    if add5 == ans5:
        print('Correct!')
        scr5 = 1
    else:
        print('Wrong!')
        scr5 = 0
    add6 = float(input(f'What is {num11} + {num22}? '))
    ans6 = num11 + num22
    if add6 == ans6:
        print('Correct!')
        scr6 = 1
    else:
        print('Wrong!')
        scr6 = 0
    add7 = float(input(f'What is {num33} + {num44}? '))
    ans7 = num33 + num44
    if add7 == ans7:
        print('Correct!')
        scr7 = 1
    else:
        print('Wrong!')
        scr7 = 0
    add8 = float(input(f'What is {num55} + {num66}? '))
    ans8 = num55 + num66
    if add8 == ans8:
        print('Correct!')
        scr8 = 1
    else:
        print('Wrong!')
        scr8 = 0
    add9 = float(input(f'What is {num77} + {num88}? '))
    ans9 = num77 + num88
    if add9 == ans9:
        print('Correct!')
        scr9 = 1
    else:
        print('Wrong!')
        scr9 = 0
    add0 = float(input(f'What is {num99} + {num00}? '))
    ans0 = num99 + num00
    if add0 == ans0:
        print('Correct!')
        scr0 = 1
    else:
        print('Wrong!')
        scr0 = 0
    scr = scr1 + scr2 + scr3 + scr4 + scr5 + scr6 + scr7 + scr7 + scr8 + scr9 + scr0
    return scr

scr = additionQuiz()
print(f'Your score is {scr}/10')









