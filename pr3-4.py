#Write Python program to find and print factorial of a number
import math

def fact(n):
    return (math.factorial(n))

num = int(input('Enter the number:'))
factorial = fact(num)
print('Factorial of', num, 'is', factorial)