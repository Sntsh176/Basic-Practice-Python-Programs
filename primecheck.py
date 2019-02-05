"""
This will check if the number is prime
"""

num = int(input("Please enter a number to check if Prime ?"))

div = [ i for i in range(2,int(num/2) if num % i == 0]

if len(div) == 0:
	Print("The number is Prime")
else:
	print("The Given number is not a prime Number, PFB the divisors :")
	print(div)
	