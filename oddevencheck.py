# odd even  number check and if is divisible by 4

number = int(input("Please enter a number : "))

if number % 2 == 0:
	if number % 4 == 0:
		print(number,"Number is Even and divisible by 4")
	else:
		print(number, "Number is even ")
else:
	print(number, "Number is Odd ")

num = int(input("Please enter another number : "))
check = int(input("Please enter one more number : "))

if num % check == 0
	print(num , "is divisible by",check)
else:
	print(num , "is not divisible by",check)