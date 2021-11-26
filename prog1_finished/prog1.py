#Program 1: Number Sorter
#Create a program that ask 4 numbers. 
#Print the 4 numbers from highest to lowest using only if-else statement.

print('Input four numbers.')
#with extra input validation
while True:
    num11 = (input('Number 1: '))
    if num11.isalpha():
        print('Numbers Only!')
    elif not num11.isdigit():
        print('Numbers Only!')
    elif num11.isdigit():
        break
while True:
    num22 = (input('Number 2: '))
    if num22.isalpha():
        print('Numbers Only!')
    elif not num22.isdigit():
        print('Numbers Only!')
    elif num22.isdigit():
        break
while True:
    num33 = (input('Number 3: '))
    if num33.isalpha():
        print('Numbers Only!')
    elif not num33.isdigit():
        print('Numbers Only!')
    elif num33.isdigit():
        break
while True:
    num44 = (input('Number 4: '))
    if num44.isalpha():
        print('Numbers Only!')
    elif not num44.isdigit():
        print('Numbers Only!')
    elif num44.isdigit():
        break

num1 = int(num11) #added to convert to integer
num2 = int(num22) #added to convert to integer
num3 = int(num33) #added to convert to integer
num4 = int(num44) #added to convert to integer

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
    if num1 >= num2 and num1 >= num4:
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

print()
print("From highest to lowest.")
print(f'==> {first}')
print(f'==> {second}')
print(f'==> {third}')
print(f'==> {fourth}')
