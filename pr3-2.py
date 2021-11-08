#Write a Python program to add all the numbers entered by a user until user enters 0
print('Input numbers to calculate their sum. Input 0 to stop.')
a = 0
sum = 0
integer = 1
while integer !=0:
    integer = int(input(''))
    sum = sum + integer
    a += 1
    if a == 0:
        print('Input new numbers : ')
    else:
        print('The sum is : ', sum)