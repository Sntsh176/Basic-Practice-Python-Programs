# It will check if the number is Palindrome 
# In python it is very easy using List slicing 

print ("Here will check if the String is Palindrome")
input_string = input("please enter the string : ")

if input_string.lower() == input_string[::-1].lower(): #here we have reverse the string and matching it
    print("The given string is palindrome")
else:
    print("The given string is NOT palindrome")
	