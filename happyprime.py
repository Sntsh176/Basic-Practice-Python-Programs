"""
the below code will read data from file
and find if the number is Happy or Prime
"""

# !/use/bin/env python3
# https://www.practicepython.org/exercise/2014/12/14/23-file-overlap.html

if __name__ == "__main__":
	with open('happy.txt', 'r') as open_file:
		text=open_file.read()
		
	with open('prime.txt', 'r') as open_file:
		text2=open_file.read()
	
	list_happy = map(int,text.split(","))
	list_prime = map(int,text2.split(","))
	
	print "Happy Numbers:" 
	print list_happy
	print "\nPrime Numbers:"
	print list_prime
	print "\nOverlap:"
	print sorted(list(set(list_happy)&set(list_prime)))