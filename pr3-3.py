#Write a Python Program to reverse a number. For example, if user enters 123 as input then 321 is printed as output.
n = int(input(''))
rev = 0
while(n > 0):
	a = n % 10
	rev = rev * 10 + a
	n = n // 10

print(rev)

