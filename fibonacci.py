"""
To find the n Fibonacci number 
"""

def fibo(num):
	fibo = [0,1]
	if num <= 1:
		return fibo[0]
	elif num <= 2:
		return fibo
	else:
		for i in range(2,num):
			fibo.append(fibo[-1] + fibo[-2])
		return fibo

num = int(input())
fibo(num)