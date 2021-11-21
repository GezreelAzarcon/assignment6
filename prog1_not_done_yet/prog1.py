#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.
import sys

print('Input four numbers.')
while True:
    num1 = (input('Number 1: '))
    if num1.isalpha():
        print('Numbers Only!')
    else:
        break
while True:
    num2 = (input('Number 2: '))
    if num2.isalpha():
        print('Numbers Only!')
    else:
        break
while True:
    num3 = (input('Number 3: '))
    if num3.isalpha():
        print('Numbers Only!')
    else:
        break
while True:
    num4 = (input('Number 4: '))
    if num4.isalpha():
        print('Numbers Only!')
    else:
        break
    (float(num1,num2,num3,num4))
if num1 >= num2 and num1 >= num3 and num1 >= num4:
    first = num1
    if num2 >= num3 and num2 >= num4:
        second = num2
        if num3 >= num4:
            third = num3
            fourth = num4
        elif num4 >= num3:
            third = num4
            fourth = num3
    elif num3 >= num2 and num3 >= num4:
        second = num3
        if num2 >= num4:
            third = num2
            fourth = num4
        elif num4 >= num2:
            third = num4
            fourth = num2
    elif num4 >= num2 and num4 >= num3:
        second = num4
        if num3 >= num2:
            third = num3
            fourth = num2
        elif num2 >= num3:
            third = num2
            fourth = num3
        
elif num2 >= num1 and num2 >= num3 and num2 >= num4:
    first = num2
    if num1 >= num3 and num1 >= num4:
        second = num1
        if num3 >= num4:
            third = num3
            fourth = num4
        elif num4 >= num3:
            third = num4
            fourth = num3
    elif num3 >= num1 and num3 >= num4:
        second = num3
        if num1 >= num4:
            third = num1
            fourth = num4
        elif num4 >= num1:
            third = num4
            fourth = num1
    elif num4 >= num2 and num4 >= num3:
        second = num4
        if num3 >= num1:
            third = num3
            fourth = num1
        elif num1 >= num3:
            third = num1
            fourth = num3

elif num3 >= num1 and num3 >= num2 and num3 >= num4:
    first = num3
    if num1 >= num3 and num1 >= num4:
        second = num1
        if num2 >= num4:
            third = num2
            fourth = num4
        elif num4 >= num2:
            third = num4
            fourth = num2
    elif num2 >= num1 and num2 >= num4:
        second = num2
        if num1 >= num4:
            third = num1
            fourth = num4
        elif num4 >= num1:
            third = num4
            fourth = num1
    elif num4 >= num2 and num4 >= num3:
        second = num4
        if num1 >= num2:
            third = num1
            fourth = num2
        elif num2 >= num1:
            third = num2
            fourth = num1

elif num4 >= num1 and num4 >= num2 and num4 >= num3:
    first = num4
    if num1 >= num3 and num1 >= num2:
        second = num1
        if num2 >= num3:
            third = num2
            fourth = num3
        elif num3 >= num2:
            third = num3
            fourth = num2
    elif num2 >= num1 and num2 >= num3:
        second = num2
        if num1 >= num3:
            third = num1
            fourth = num3
        elif num3 >= num1:
            third = num3
            fourth = num1
    elif num3 >= num2 and num3 >= num1:
        second = num3
        if num1 >= num2:
            third = num1
            fourth = num2
        elif num2 >= num1:
            third = num2
            fourth = num1

print("From highest to lowest.")
print(f"==>:{first}")
print(f"==>:{second}")
print(f"==>:{third}")
print(f"==>:{fourth}")
